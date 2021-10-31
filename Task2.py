INF = 1000

rooms = ["Cafetaria", "Admin", "Storage", "Weapons", "Medbay",
         "O2", "Navigations", "Shield", "Communications", "Electrical",
         "Lower E.", "Security", "Reactor", "Upper E."]

Crewmate = [[0, 2, 2, 1, 2, INF, INF, INF, INF, INF, INF, INF, INF, 4],
            [2, 0, 2, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF],
            [2, 2, 0, INF, INF, INF, INF, 3, 3, 3, 6, INF, INF, INF],
            [1, INF, INF, 0, INF, 2, 5, 7, INF, INF, INF, INF, INF, INF],
            [2, INF, INF, INF, 0, INF, INF, INF, INF, INF, INF, INF, INF, 4],
            [INF, INF, INF, 2, INF, 0, 5, 7, INF, INF, INF, INF, INF, INF],
            [INF, INF, INF, 5, INF, 5, 0, 6, INF, INF, INF, INF, INF, INF],
            [INF, INF, 3, 7, INF, 7, 6, 0, 2, INF, INF, INF, INF, INF],
            [INF, INF, 3, INF, INF, INF, INF, 2, 0, INF, INF, INF, INF, INF],
            [INF, INF, 3, INF, INF, INF, INF, INF, INF, 0, 5, INF, INF, INF],
            [INF, INF, 6, INF, INF, INF, INF, INF, INF, 5, 0, 3, 3, 5],
            [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 3, 0, 2, 3],
            [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 3, 2, 0, 3],
            [4, INF, INF, INF, 4, INF, INF, INF, INF, INF, 5, 3, 3, 0]]

Imposter = [[0, 0, 2, 1, 2, 4, 4, 2, INF, INF, INF, INF, INF, 4],
            [0, 0, 2, 4, INF, 4, 4, 2, INF, INF, INF, INF, INF, INF],
            [2, 2, 0, INF, INF, INF, INF, 3, 3, 3, 6, INF, INF, INF],
            [1, 4, INF, 0, INF, 2, 0, 7, INF, INF, INF, INF, INF, INF],
            [2, INF, INF, INF, 0, INF, INF, INF, INF, 0, INF, 0, INF, 4],
            [4, 4, INF, 2, INF, 0, 5, 7, INF, INF, INF, INF, INF, INF],
            [4, 4, INF, 0, INF, 5, 0, 0, INF, INF, INF, INF, INF, INF],
            [2, 2, 3, 7, INF, 7, 0, 0, 2, INF, INF, INF, INF, INF],
            [INF, INF, 3, INF, INF, INF, INF, 2, 0, INF, INF, INF, INF, INF],
            [INF, INF, 3, INF, 0, INF, INF, INF, INF, 0, 5, 0, INF, INF],
            [INF, INF, 6, INF, INF, INF, INF, INF, INF, 5, 0, 3, 0, 5],
            [INF, INF, INF, INF, 0, INF, INF, INF, INF, 0, 3, 0, 2, 3],
            [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, 2, 0, 0],
            [4, INF, INF, INF, 4, INF, INF, INF, INF, INF, 5, 3, 0, 0]]


def floyd_warshall(matrix, next_room):
    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][k] == INF or matrix[k][j] == INF:
                    continue
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                    next_room[i][j] = next_room[i][k]


def initialise(vertex, graph, next_room, dist):
    for i in range(vertex):
        for j in range(vertex):
            dist[i][j] = graph[i][j]
            # No edge between node
            # i and j
            if graph[i][j] == INF:
                next_room[i][j] = -1
            else:
                next_room[i][j] = j


def construct_path(u, v, next_room):
    # If there's no path between
    # node u and v, simply return
    # an empty array
    if next_room[u][v] == -1:
        return {}

    # Storing the path in a vector
    path = [u]
    while u != v:
        u = next_room[u][v]
        path.append(u)

    return path


def print_path(path, dist):
    n = len(path)
    print("Path : ", end="")
    for i in range(n - 1):
        print(rooms[path[i]], end=" -> ")
    print(rooms[path[n - 1]])
    print(f"Distance : {dist[path[0]][path[n-1]]}")


next_crewmate = [[-1 for i in range(len(rooms))] for i in range(len(rooms))]
next_imposter = [[-1 for i in range(len(rooms))] for i in range(len(rooms))]

dist_crewmate = [[-1 for i in range(len(rooms))] for i in range(len(rooms))]
dist_imposter = [[-1 for i in range(len(rooms))] for i in range(len(rooms))]

initialise(len(rooms), Crewmate, next_crewmate, dist_crewmate)
floyd_warshall(dist_crewmate, next_crewmate)

initialise(len(rooms), Imposter, next_imposter, dist_imposter)
floyd_warshall(dist_imposter, next_imposter)


def run_task2():
    print()
    print("*"*80)
    print("SHORTEST PATH")
    print("*"*80)
    print()
    for i in range(len(rooms)):
        print(f"Room {i} : {rooms[i]}")
    print()
    while True:
        source = input("Enter a Source Room Number : ")
        if not source.isdigit():
            print("INVALID SOURCE ROOM!")
            continue
        source = int(source)
        if source not in range(len(rooms)):
            print("INVALID SOURCE ROOM!")
        else:
            break

    while True:
        destination = input("Enter a Destination Room Number : ")
        if not destination.isdigit():
            print("INVALID DESTINATION ROOM!")
            continue
        destination = int(destination)
        if destination not in range(len(rooms)):
            print("INVALID DESTINATION ROOM!")
        else:
            break

    print()
    print("*"*80)
    print()
    print(f"Shortest path from {rooms[source]} to {rooms[destination]}: for Crewmate")
    path = construct_path(source, destination, next_crewmate)
    print_path(path, dist_crewmate)
    print()
    print(f"Shortest path from {rooms[source]} to {rooms[destination]}: for Imposter")
    path = construct_path(source, destination, next_imposter)
    print_path(path, dist_imposter)
    print()
    print("*"*80)
