#!/usr/bin/env python3

import networkx as nx
import matplotlib.pyplot as plt

data = {
    "name::John": {
        "5": "T",
        "2": "L",
        "3": "I"
    },
    "name::Mary": {
        "2": "T",
        "5": "I"
    }
}

G = nx.DiGraph()

for person in data.keys():
    for concept, assignment in data[person].items():
        if assignment == "L":
            G.add_edge("source", "learning::" + person, capacity=1)
            G.add_edge(
                "learning::" + person, "concept::" + concept, capacity=1)

        elif assignment == "T":
            G.add_edge(
                "concept::" + concept, "teaching::" + person, capacity=1)
            G.add_edge("teaching::" + person, "drain", capacity=1)

nx.draw_networkx(G)
plt.savefig("pokus.png")

flow = nx.max_flow_min_cost(G, "source", "drain")

# flow = dir(filter(lambda , flow: v>0 flow.items()))
filtered_flow = {}
for from_, to in flow.items():
    non_empty_edges = dict(filter(lambda x: x[1] > 0, to.items()))
    if non_empty_edges:
        filtered_flow[from_] = non_empty_edges

# print(filtered_flow)

flow = filtered_flow

for concept in filter(lambda key: key.startswith("concept"), flow.keys()):
    print("{teacher} is teaching {concept} to".format(
        teacher=list(flow[concept].keys())[0],
        concept=concept.split("::")[-1]))

    for key, to in flow.items():
        if concept in flow[key]:
            print(key.split("::")[-1])
