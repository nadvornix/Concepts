#!/usr/bin/env python3

from itertools import groupby
import re
import networkx as nx
import matplotlib.pyplot as plt
from pulp import *

max_group_size = 5
num_rounds = 3


def unique(l):
    return list(set(l))


def arc_to_string(t):
    """t is a tuple (from, to). It returns 'from-to'"""
    return "___".join(t)


def edge_to_str(from_, to):
    return from_ + "___" + to


# N: používám názvy variables a vars.
def edges_out(vars, node):
    """filters edges from vars that are going out of node."""
    # N: stupid varname
    result = []
    for var_name, var in vars.items():
        from_, to = var_name.split("___")
        if node in from_:
            result.append((var_name, var))
    return dict(result)


def edges_in(vars, node):
    # N: stupid varname
    result = []
    for var_name, var in vars.items():
        from_, to = var_name.split("___")
        if node in to:
            result.append((var_name, var))
    return dict(result)


def data_to_graph(data, num_rounds):
    people_names = data.keys()

    G = nx.DiGraph()
    for round in range(num_rounds):
        round_str = "round-%s::" % round

        for person in people_names:
            for concept, assignment in data[person].items():
                if assignment == "L":
                    G.add_edge("source", round_str+"learning::" + person, capacity=1)
                    G.add_edge(
                        round_str+"learning::" + person, round_str+"concept::" + concept, capacity=1)

                elif assignment == "T":
                    G.add_edge(
                        round_str+"concept::" + concept, round_str+"teaching::" + person, capacity=5)
                    G.add_edge(round_str+"teaching::" + person, "drain", capacity=5)

    return G

def var_to_name(var_name):
    return re.match('.*name::([a-zA-Z]+)', var_name).group(1)

def filter_vars(all_vars, regex):
    return {var_name: var for var_name, var in all_vars.items() if re.match(regex, var_name)}

def main():
    data = {
        "name::John": {
            "5": "T",
            "2": "L",
            "3": "I"
        },
        "name::Mary": {
            "2": "T",
            "5": "I"
        },
        "name::Alice": {
            "5": "L",
            "3": "T",
        }
    }

    G = data_to_graph(data, num_rounds)

    nx.draw_networkx(G)
    plt.savefig("pokus.png")

    nodes = list(G.nodes)

    prob = LpProblem("ConceptMatching", LpMaximize)

    # edges with possible value 0/1. Ie: nearly all of them.
    binary_edges = [
        edge_to_str(from_, to) for from_, to in G.edges if to != "drain"
    ]
    binary_vars = LpVariable.dicts(
        'var_binary', binary_edges, lowBound=0, upBound=1, cat=LpInteger)

    # N: this is a stupid var name
    draining_edges = [
        edge_to_str(from_, to) for from_, to in G.edges if to == "drain"
    ]

    larger_vars = LpVariable.dicts(
        'var_binary', draining_edges, lowBound=0, upBound=max_group_size,
        cat=LpInteger)

    all_vars = dict(binary_vars, **larger_vars)

    # edges_in = edges_out
    for node in nodes:
        if node not in ("source", "drain"):
            e_in = edges_in(all_vars, node)
            e_out = edges_out(all_vars, node)
            print(node, e_in, e_out)
            prob += lpSum(e_in) == lpSum(e_out), "flow_constraint_" + node

    # adding additional constrants:
    # teacher of one group cannot be in second group:
    people_names = data.keys()
    for round in range(num_rounds):
        round_str = "round-%s::" % round
        for person in people_names:
            # a and b are nodes representing this person
            a = edges_in(all_vars, round_str+"teaching::" + person)
            b = edges_out(all_vars, round_str+"learning::" + person)
            prob += (lpSum(a) + lpSum(b) <= 1,
                round_str+"person_is_never_teaching_one_and_learning_other_" + person)
            print(">>", person, a, b)

    # forbid repeating of same topic for same people in multiple rounds:
    learning_vars = filter_vars(all_vars, '.*learning.*concept')
    people = groupby(sorted(learning_vars.keys(), key=var_to_name), var_to_name)

    # N: stupid var names
    for key, edge_group in people:
        edge_group_list = list(edge_group)
        vars = []
        for var_name in edge_group_list:
            vars.append(all_vars[var_name])

        # vars = [all_Vars[var_name] for var_name in edge_group_list]
        prob += (lpSum(vars) <= 1,
            key+" can learn this concept only once")


    # so far, drain was only a string and we had variables for edges.
    drain = LpVariable("drain", lowBound=0)

    prob += lpSum(larger_vars) == drain, "into_drain"

    prob += drain, "obj"
    prob.writeLP("test1.lp")
    prob.solve()

    print("Status:", LpStatus[prob.status])

    # Print the value of the variables at the optimum
    for v in prob.variables():
        print(v.name, "=", v.varValue)

    # Print the value of the objective
    print("objective=", value(prob.objective))


if __name__ == "__main__":
    main()
