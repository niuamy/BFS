graph = {
    'l' : ['p','q'],
    'm' : ['l','n'],
    'n' : ['r'],
    'p' : ['r','w'],
    'q' : ['m','r'],
    'r' : [],
    'w' : []
}

queue = []
visited = []
distance = []
def bfs (visited, graph, source):
    queue.append(source)
    while len(queue) > 0:
        vertex = queue.pop(0)
        visited.append(vertex)
        for neighbor in graph[vertex]:
            if (neighbor not in visited) and (neighbor not in queue):
                queue.append(neighbor)

def distances(graph, source, distance):
    children = []
    grandchildren = []
    distance.append(0)
    visited = [source]
    time = 1
    for neighbor in graph[source]:
        children.append(neighbor)
    while len(children) > 0:
        distance.append(time)
        child = children.pop(0)
        visited.append(child)
        for neighbor in graph[child]:
            if (neighbor not in visited) and (neighbor not in grandchildren):
                grandchildren.append(neighbor)
        if len(children) == 0:
            children = grandchildren.copy()
            grandchildren = []
            time +=1

bfs(visited,graph,'l')
distances(graph,'l',distance)
i=0
while i < len(visited):
    print(visited[i] + ' : ' + str(distance[i]))
    i+=1
