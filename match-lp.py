#!/usr/bin/env python3

import networkx as nx
import matplotlib.pyplot as plt
from pulp import *

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
people_names = data.keys()

concepts = []
for assingment_dict in data.values():
    for concept_name in assingment_dict:
        concepts.append(concept_name)


def unique(l):
    return list(set(l))


concepts = unique(concepts)

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

nx.draw_networkx(G)
plt.savefig("pokus.png")

nodes = list(G.nodes)
edges = list(G.edges)

arcs = list(G.edges)  # N: sometimes I call it arcs, sometime edges


def arc_name(t):
    """t is a tuple (from, to). It returns 'from-to'"""
    return "___".join(t)


arc_names = [arc_name(arc) for arc in arcs]


def arcs_by_prefix(arc_names, prefix):
    return [arc_name for arc_name in arc_names if arc_name.startswith(prefix)]


def vars_by_suffix(variables, suffix):
    # N: tyhle dvě funkce by šli sjednotit. A předělat na obecnější filter if..
    return {k: v for k, v in variables.items() if k.endswith(suffix)}


def vars_by_prefix(variables, prefix):
    return {k: v for k, v in variables.items() if k.startswith(prefix)}


prob = LpProblem("ConceptMatching", LpMaximize)


def edge_to_str(from_, to):
    return from_ + "___" + to


# N: používám názvy variables a vars.
def edges_out(variables, node):
    # N: stupid varname
    result = []
    for var_name, var in variables.items():
        from_, to = var_name.split("___")
        if node in from_:
            result.append((var_name, var))
    return dict(result)


def edges_in(variables, node):
    # N: stupid varname
    result = []
    for var_name, var in variables.items():
        from_, to = var_name.split("___")
        if node in to:
            result.append((var_name, var))
    return dict(result)


binary_edges = [
    edge_to_str(from_, to) for from_, to in G.edges if to != "drain"
]
binary_vars = LpVariable.dicts(
    'var_binary', binary_edges, lowBound=0, upBound=1, cat=LpInteger)

# N: this is a stupid var name
larger_edges = [
    edge_to_str(from_, to) for from_, to in G.edges if to == "drain"
]

larger_vars = LpVariable.dicts(
    'var_binary', larger_edges, lowBound=0, upBound=5,
    cat=LpInteger)  # N: 5 == maximum size of group. Put into a constant.

all_vars = dict(binary_vars, **larger_vars)

# edges_in = edges_out
for node in nodes:
    if node not in ("source", "drain"):
        e_in = edges_in(all_vars, node)
        e_out = edges_out(all_vars, node)
        print(node, e_in, e_out)
        prob += lpSum(e_in) == lpSum(e_out), "flow_constraint_" + node

# teacher of one group cannot be in second group:
for person in people_names:
    # a and b are nodes representing this person
    a = edges_in(all_vars, "teaching::" + person)
    b = edges_out(all_vars, "learning::" + person)
    prob += lpSum(a) + lpSum(
        b) == 1, "person_is_never_teaching_one_and_learning_other_" + person
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

# x = LpVariable.dicts('teaching', possible_tables, lowBound=0, upBound=1, cat=pulp.LpInteger)
