#!/usr/bin/env python3

import networkx as nx
import matplotlib.pyplot as plt
from pulp import *

max_group_size = 5


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


def data_to_graph(data):
    people_names = data.keys()

    G = nx.DiGraph()
    for person in people_names:
        for concept, assignment in data[person].items():
            if assignment == "L":
                G.add_edge("source", "learning::" + person, capacity=1)
                G.add_edge(
                    "learning::" + person, "concept::" + concept, capacity=1)

            elif assignment == "T":
                G.add_edge(
                    "concept::" + concept, "teaching::" + person, capacity=5)
                G.add_edge("teaching::" + person, "drain", capacity=5)
    return G


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

    G = data_to_graph(data)

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
    for person in people_names:
        # a and b are nodes representing this person
        a = edges_in(all_vars, "teaching::" + person)
        b = edges_out(all_vars, "learning::" + person)
        prob += (lpSum(a) + lpSum(b) <= 1,
            "person_is_never_teaching_one_and_learning_other_" + person)
        print(">>", person, a, b)

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
