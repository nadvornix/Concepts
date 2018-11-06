# Implementations of network flow:

- (choosen) https://networkx.github.io/documentation/networkx-1.10/reference/algorithms.flow.html
- https://developers.google.com/optimization/flow/maxflow
- https://graph-tool.skewed.de/static/doc/flow.html
- https://github.com/pmneila/PyMaxflow
- http://igraph.org/redirect.html

It is possible to solve this as an integer linear programming problem. That may be a more general approach.

# Installation:

```
sudo apt install python-pydot python-pydot-ng graphviz libgraphviz-dev
pip install -r requirements.txt
```
# TODO:
- invent better name

# my notes::
- design user interface
- design server architecture
- put it all together


constraints:
- randomize (? - to have multiple possible sets)
- indiference

- priority (co by učili více/méně rádi)
- multiple rounds v kt. stejní lidi neučí ve všech.
- check: learning set != teaching set

- multiple rounds
- in multiple rounds teach/learn one thing only once.
- no free people
  - automatic low-priority (cap 0.001) edges everybody -> learning everything

- nejsou skupiny o jednom člověku.
  - automatic.

MAYBE (future version):
- same topic taught in multiple groups at once
