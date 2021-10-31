from Graph import Graph
from networkx.generators.random_graphs import erdos_renyi_graph


def color_graph(graph_):
    """
    :param graph_:
    :return:
    """
    return {
        vertex: {
            other_vertex: (
                0 if other_vertex == vertex or other_vertex in graph_.dictionary[vertex] else 1
            )
            for other_vertex in graph_.vertices()
        } for vertex in graph_.vertices()
    }


def possible_imposter(colorgraph, player):
    print(f"If the first imposter is PLAYER {player}, the other imposter is one of these players : ")
    for other_players in colorgraph[player]:
        if colorgraph[player][other_players] == 1:
            print(other_players, end=" ")
    print()


def generate_graph():
    """
    Generate a Random graph
    :return:
    """
    graph = {}
    for i in range(10):
        graph[str(i)] = []

    n = 10
    p = 0.45
    g = erdos_renyi_graph(n, p)
    for edge in g.edges:
        vertex1, vertex2 = edge
        graph[str(vertex1)].append(str(vertex2))
        graph[str(vertex2)].append(str(vertex1))
    return graph


def input_graph():
    graph = {}
    for i in range(10):
        graph[str(i)] = set()

    i = 0
    while i < 10:
        print()
        print(f"Enter values for player {i} : ", end="")
        players_data = input()
        players = players_data.split()
        players = set(players)
        for player in players:
            if player not in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                print("ENTER VALID PLAYERS!")
                i -= 1
            else:
                graph[str(i)].add(player)
                graph[player].add(str(i))
        i += 1

    for i in range(10):
        graph[str(i)] = graph.get(str(i)) - {str(i)}
        graph[str(i)] = sorted(graph.get(str(i)))
    return graph


def run_task1():
    """
    Run the Task for finding POSSIBLE IMPOSTER
    :return: NULL
    """

    print()
    print("*"*80)
    print("POSSIBLE IMPOSTERS")
    print("*"*80)
    print()
    print("Choice : ")
    print("1 : Input Graph")
    print("2 : Random Graph")

    while True:
        choice = input(">> ")
        if choice not in {"1", "2"}:
            print("ENTER VALID CHOICE!")
        else:
            break

    if choice == 1:
        graph = Graph(input_graph())
    else:
        graph = Graph(generate_graph())

    print()
    print("Graph : ")
    graph.print_graph()
    print()

    colorgraph = color_graph(graph)

    set_player = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

    while True:
        dead_player = input("Enter Dead Player : ")
        if dead_player not in set_player:
            print("ENTER A VALID PLAYER!")
            continue
        break

    print()
    print("*"*80)
    print()

    if len(graph.dictionary[dead_player]) == 0:
        print("NOT ENOUGH INFORMATION!")
    else:
        for other_player in graph.dictionary[dead_player]:
            possible_imposter(colorgraph, other_player)

    print()
    print("*"*80)
