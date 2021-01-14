__Directed Weighted Graph - Python__

*Authors: Tzach Itshak Ofir and Gal Braymok*



## Description
In this project we applied graphs in the Python language.
>
***The project includes the implementation of two interfaces:***

**GraphInteface:**
>
Implemented by DiGraph class. This interface is responsible for the structure of the graph and many operations.

**GraphAlgoInterface:**
>
Implemented by GraphAlgo class. In this class there are various algorithms that can be applied on graphs

**Structure:**
>
Node - represents the set of operations applicable on a node (vertex) in a (directional) weighted graph.
>
**DiGraph:**
> - `v_size` - Returns the number of vertices in this graph.
>
> - `e_size` - Returns the number of edges in this graph.
>
> - `get_all_v` - Return a dictionary of all the nodes in the Graph, each node is represented using a pair (node_id, node_data).
>
> - `all_in_edges_of_node` - Return a dictionary of all the nodes connected to (into) node_id , each node is represented using a pair (other_node_id, weight).
>
> - `all_out_edges_of_node` - Return a dictionary of all the nodes connected from id1, each node is represented using a pair (other_node_id, weight)
>
> - `get_mc` - Returns the current version of this graph, on every change in the graph state - the MC should be increased.
>
> - `add_edge` - Adds an edge to the graph (if the edge already exists or one of the nodes dose not exists the functions will do nothing).
>
> - `add_node` - Adds a node to the graph (if the node id already exists the node will not be added).
>
> - `remove_node` - Removes a node from the graph (if the node id does not exists the function will do nothing).
>
> - `remove_edge` - Removes an edge from the graph (If such an edge does not exists the function will do nothing).
>     
> - `find_edge` - Finds the index of the first occurence of an edge.
>
> - `is_node_exist` - Determines if a node exists in the graph.
>
> -  `is_in_edge` - Determines if a node is one of an edge's vertices.
>
> - `get_all_edges` - Gets all the graph's edges.
>
> - `get_nodes` - Gets all the graph's nodes.
>
> - `get_transpose` - Gets the transpose of the graph. i.e, the original graph who's all its edges are inverted.
>

**GraphAlgo:**
> - `get_graph` - Return the directed graph on which the algorithm works on.
>
> - `load_from_json` - Loads a graph from a json file.
>
> - `save_to_json` - Saves a graph from a json file.
>
> - `shortest_path` - Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm.
>
> - `connected_component` - Finds the Strongly Connected Component(SCC) that node id1 is a part of.
>
> - `connected_components` - Finds all the Strongly Connected Component(SCC) in the graph.
>
> - `plot_graph` - Plots the graph. If the nodes have a position, the nodes will be placed there. Otherwise, they will be placed in a random but elegant manner.







## Times Comparisons
<table>
  <tr>
    <th></th>
    <th>Python</th>
    <th>NetworkX</th>
    <th>Java</th>
  </tr>
  <tr>
    <td><h4>SCC</h4></td>
    <td>0.00099</td>
    <td>0.0</td>
    <td>0.01094</td>
  </tr>
  <tr>
    <td><h4>Dijkstra</h4></td>
    <td>0.0</td>
    <td>0.0</td>
    <td>0.01722</td>
  </tr>
  <tr>
    <td><h4>Plot</h4></td>
    <td>0.25981</td>
    <td>0.15708</td>
    <td>-----------</td>
  </tr>
</table>

![](ex3/Photo.jpeg)
