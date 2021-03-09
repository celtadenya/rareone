cities = ['Ang Mo Kio', 'Bedok', 'Bukit Batok', 'Bukit Panjang', 'Bukit Timah',
          'Clementi', 'Changi', 'Choa Chu Kang', 'Jurong', 'Mandai', 'Marina Bay',
          'Nee Son', 'Outram', 'Pasir Panjang', 'Punggol', 'Queenstown', 'Sembawang',
          'Sentosa', 'Serangoon', 'Tampines', 'Toa Payoh', 'Tuas', 'Upper Thomson', 'Woodlands']
INF = 100
N = 24

graph = [
    [INF, INF, 18, 16, INF, INF, INF, INF, INF, INF, INF, 6, INF, INF, INF, INF, INF, INF, 6, INF, INF, INF, 5, INF],
    [INF, INF, INF, INF, 22, INF, INF, INF, INF, INF, 16, INF, 16, INF, INF, INF, INF, INF, INF, 5, 13, INF, 16, INF],
    [18, INF, INF, 7, 5, 7, INF, 6, 19, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 16, INF, INF],
    [16, INF, 7, INF, 6, INF, INF, 4, INF, 15, INF, 16, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 14, 11],
    [INF, 22, 5, 6, INF, 5, INF, INF, 25, INF, INF, INF, INF, INF, INF, 9, INF, INF, INF, INF, 10, INF, 11, INF],
    [INF, INF, 7, INF, 5, INF, INF, INF, INF, INF, INF, INF, INF, 7, INF, 5, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 16, 5, 18, INF, INF,
     INF],
    [INF, INF, 6, 4, INF, INF, INF, INF, 22, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 15, INF, 11],
    [INF, INF, 19, INF, 25, INF, INF, 22, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 19, INF,
     INF],
    [INF, INF, INF, 15, INF, INF, INF, INF, INF, INF, INF, 3, INF, INF, INF, INF, 6, INF, INF, INF, INF, INF, INF, 8],
    [INF, 16, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 2, INF, INF, INF, INF, INF, INF, INF, 10, INF, INF,
     INF],
    [6, INF, INF, 16, INF, INF, INF, INF, INF, 3, INF, INF, INF, INF, INF, INF, 5, INF, INF, INF, INF, INF, INF, 9],
    [INF, 16, INF, INF, INF, INF, INF, INF, INF, INF, 2, INF, INF, INF, INF, 5, INF, 6, INF, INF, 8, INF, INF, INF],
    [INF, INF, INF, INF, INF, 7, INF, INF, INF, INF, INF, INF, INF, INF, INF, 6, INF, 8, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 8, INF, INF, INF, INF,
     INF],
    [INF, INF, INF, INF, 9, 5, INF, INF, INF, INF, INF, INF, 5, 6, INF, INF, INF, 10, INF, INF, 9, INF, 10, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, 6, INF, 5, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 5],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 6, 8, INF, 10, INF, INF, INF, INF, INF, INF, INF, INF],
    [6, INF, INF, INF, INF, INF, 16, INF, INF, INF, INF, INF, INF, INF, 8, INF, INF, INF, INF, 12, 6, INF, 8, INF],
    [INF, 5, INF, INF, INF, INF, 5, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 12, INF, 15, INF, INF, INF],
    [INF, 13, INF, INF, 10, INF, 18, INF, INF, INF, 10, INF, 8, INF, INF, 9, INF, INF, 6, 15, INF, INF, 6, INF],
    [INF, INF, 16, INF, INF, INF, INF, 15, 19, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF,
     INF],
    [5, 16, INF, 14, 11, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 10, INF, INF, 8, INF, 6, INF, INF, INF],
    [INF, INF, INF, 11, INF, INF, INF, 11, INF, 8, INF, 9, INF, INF, INF, INF, 5, INF, INF, INF, INF, INF, INF, INF]
]

class City:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.parent = -1
        self.dist = 10000

    def __cmp__(self, other):
        if self.dist > other.dist:
            return 1
        elif self.dist < other.dist:
            return -1
        return 0

    def __lt__(self, other):
        return self.dist < other.dist


vcities = []
start = ""
to = ""
startid = 0
toid = 0


def findCity(start):
    for i in range(len(cities)):
        if start == cities[i]:
            return i
    return -1


def initGraph():
    global vcities
    vcities = []

    for i in range(len(cities)):
        c = City(i, cities[i])
        vcities.append(c)


def printPath():
    global start, to, startid, toid
    print("Start from : %s" % start)
    print("To : %s" % to)
    path = ""
    # print("Toid printpath : %d " %toid)
    current = vcities[toid]
    # print("Destination : %s " % current.name)

    while current.parent != -1:
        # print("Enter here")
        path = current.name + "->" + path
        current = vcities[current.parent]

    path = current.name + "->" + path

    print("Path : %s " % path[0:-2])
    print("Total Distance : %d km" % vcities[toid].dist)


def dijkstra():
    initGraph()
    queue = []
    startcity = vcities[startid]
    startcity.parent = -1
    startcity.dist = 0
    queue.append(startcity)

    while len(queue) > 0:
        currentcity = queue.pop(0)
        currentid = currentcity.id

        for neighbour in range(len(cities)):
            if graph[currentid][neighbour] < INF and currentcity.dist + graph[currentid][neighbour] < vcities[
                neighbour].dist:
                vcities[neighbour].parent = currentid
                vcities[neighbour].dist = currentcity.dist + graph[currentid][neighbour]
                queue.append(vcities[neighbour])

        queue.sort()

    printPath()


def printCityDistance():
    # print all dist of all cities from start
    for city in vcities:
        print("Distance from start : %d to %s with id %d parent %d " % (city.dist, city.name, city.id, city.parent))


def printCityMatrix():
    print("MATRIX:")
    print("Cty\Cty", end="")
    for i in range(N):
        print("%2d " % i, end="")
    print()
    for i in range(N):
        print("%d\t" % i, end="")
        for j in range(N):
            if (graph[i][j] == INF):
                print("--  ", end="")
            else:
                print("%2d  " % (graph[i][j]), end="")
        print()
    print("Cty\Cty  ", end="")
    for i in range(N):
        print("%2d " % i, end="")
    print()
    print("LEGEND")
    for i in range(len(cities)):
        print("%d\t%s" % (i, cities[i]))


def main():
    initGraph()
    quit = False
    while not quit:
        print("CSCI203 ASSIGNMENT 3 - DIJKSTRA'S SHORTEST PATH")
        print("[1] Display City Distance Information Matrix")
        print("[2] Shortest Distance Between Two Cities")
        print("[3] Quit")
        choice = int(input("Enter your input : "))

        if choice == 1:
            # initGraph()
            # printCityDistance()
            printCityMatrix()

        elif choice == 2:
            global start, to, startid, toid
            for i in range(len(cities)):
                print("%d\t%s" % (i, cities[i]))
            start = input("Enter start city name: ")
            to = input("Enter to city name : ")
            startid = findCity(start)
            toid = findCity(to)
            while toid == -1 or startid == -1:
                print("The start/to city could not be found. Please enter it again.")
                start = input("Enter start city : ")
                to = input("Enter to city : ")
                startid = findCity(start)
                toid = findCity(to)

            dijkstra()

        else:
            quit = True


if __name__ == '__main__':
    main()

