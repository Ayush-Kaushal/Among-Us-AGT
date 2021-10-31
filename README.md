As we have discussed we are analysing the AMONG US game 
using 3 different tasks:-
• Task 1 => Possible Imposters
• Task 2 => Shortest Path between two rooms
o Shortest Path for Crewmates
o Shortest Path for Imposters
• Task 3 => Secure last task for Crewmates
Task 1 :- Possible Imposters
• 10 players (8 crewmates + 2 imposters)
• Condition – Both the imposters can’t move together.
• The model for the graph will be an undirected and 
unweighted graph.
o Node will be the players
o Edges will represent if players have seen each 
other.
• We can list out all the possible imposters using the 
GRAPH COLORING technique.
Task 2 :- Shortest Path between two rooms
• The model of the map will be an undirected and
weighted graph
o Nodes will be the rooms
o Edges will be the path between the rooms
o Weight will be the distance between two rooms.
Here we will have two graph one for crewmates and one for 
imposters as imposters can use the vents.
• Finding minimum distance from cafeteria to all other 
rooms as Cafeteria is the central room in the game.
• To find minimum distance from Cafeteria we will use 
Dijkstra’s Algorithm.
• Finding minimum distance between any two rooms.
• To find the minimum distance path between the 
specified room we will use A* Algorithm.
o Heuristic function for crewmate’s graphs will be 
Manhattan Distance.
o Heuristic function for imposter’s graphs will be 
Euclidean Distance.
• Also, the users can specify if a path is blocked in the 
game then the Graph will be changed accordingly.
Task 3:- Secure the last Task (Hamiltonian Path)
• To secure the last task crewmates will want to form a 
pack.
• For this the model of the map will be an undirected and 
unweighted graph.
o Nodes will be the rooms.
o Edges will be the path between the rooms.
• To solve this problem, we choose to implement the 
Hamiltonian path as we want a path where each room 
is visited exactly once.