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


def graph_diameter():
    max_diameter = 0
    for row in graph:
        diameter = len(bfs(graph, row))
        if diameter > max_diameter:
            max_diameter = diameter

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node] - visited)
    return visited

main()