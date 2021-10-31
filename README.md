# Among Us and Graph Theory
We are analysing the AMONG US game using 3 different tasks:- 

* Task 1: Possible Imposters 
* Task 2: Shortest Path between two rooms 
    * Shortest Path for Crewmates
    * Shortest Path for Imposters
* Task 3: Secure last task for Crewmates 

## Task 1: Possible Imposters
* 10 players (8 crewmates + 2 imposters) 
* Condition – Both the imposters can’t move together
* The model for the graph will be an undirected and unweighted graph
    * Node will be the players
    * Edges will represent if players have seen each other.
* We can list out all the possible imposters using the GRAPH COLORING technique 

## Task 2: Shortest Path between two rooms 
* The model of the map will be an undirected and weighted graph
    * Nodes will be the rooms 
    * Weight will be the distance between two rooms
* Using Floyd–Warshall algorithm to compute minimum distance and path between two rooms

## Task 3: Secure the last Task (Hamiltonian Path)
* To secure the last task crewmates will want to form a pack
* For this the model of the map will be an undirected and unweighted graph
    * Nodes will be the rooms
    * Edges will be the path between the rooms
* To solve this problem, we choose to implement the Hamiltonian path as we want a path where each room is visited exactly once