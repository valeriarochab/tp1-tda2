from collections import deque
import csv

def main():
    graph = {}

    with open('World.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        next(csv_reader) #remove header
        for row in csv_reader:
            if row[0] not in graph:
                graph[row[0]] = set()
            graph[row[0]].add(row[1])
    print(graph)


def graph_diameter(graph):
    max_diameter = 0
    for node in graph:
        distances = bfs(graph, node)
        max_distance = max(distances.values())
        max_diameter = max(max_diameter, max_distance)
    return max_diameter

def bfs(graph, start):
    visited = set()
    queue = deque([(start, 0)])
    distances = {start: 0}

    while queue:
        node, dist = queue.popleft()

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in distances:
                    distances[neighbor] = dist + 1
                    queue.append((neighbor, dist + 1))

    return distances

main()