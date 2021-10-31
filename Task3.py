rooms = ["Cafetaria", "Admin", "Storage", "Weapons", "Medbay",
         "O2", "Navigations", "Shield", "Communications", "Electrical",
         "Lower E.", "Security", "Reactor", "Upper E."]

Map_Crewmate = [[0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
                [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0]]


class Step4_Graph():
    def __init__(self, vertices):
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.V = vertices

    ''' Check if this vertex is an adjacent vertex  
            of the previously added vertex and is not  
            included in the path earlier '''

    def isSafe(self, v, pos, path):
        if self.graph[path[pos-1]][v] == 0:
            return False

        for vertex in path:
            if vertex == v:
                return False

        return True

    def hamCycleUtil(self, path, pos):
        if pos == self.V:
            return True

        # Try different vertices as a next candidate
        # in Hamiltonian Cycle. We don't try for 0 as
        # we included 0 as starting point in hamCycle()
        for v in range(0, self.V):

            if self.isSafe(v, pos, path) == True:

                path[pos] = v

                if self.hamCycleUtil(path, pos+1) == True:
                    return True

                # Remove current vertex if it doesn't
                # lead to a solution
                path[pos] = -1

        return False

    def hamiltonian_cycle(self, source):
        # ''' Let us put vertex 0 as the first vertex
        #     in the path. If there is a Hamiltonian Cycle,
        #     then the path can be started from any point
        #     of the cycle as the graph is undirected '''

        path = [-1] * self.V
        path[0] = source

        if self.hamCycleUtil(path, 1) == False:
            print("Path does not exist")
            return False

        self.printSolution(path)
        return True

    def printSolution(self, path):
        print("Path Exists")
        print("Path : ", end="")
        for vertex in range(14):
            if vertex < 13:
                print(rooms[path[vertex]], end=" -> ")
            else:
                print(rooms[path[vertex]])


g = Step4_Graph(14)
g.graph = Map_Crewmate


def input_source():
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

    return source


def run_task3():
    print()
    print("*"*80)
    print("HAMILTONIAN PATH")
    print("*"*80)
    print()

    source = input_source()
    print()
    print("*"*160)
    print()
    print(rooms[source], " : ", end=" ")
    g.hamiltonian_cycle(source)
    print()
    print("*"*160)
    print()
