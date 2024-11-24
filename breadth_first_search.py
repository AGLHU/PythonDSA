# Video tutorial from Michael Sambol
# Video link: https://www.youtube.com/watch?v=HZ5YTanv5QE
# O(|V| + |E|)

from collections import deque


graph = {
  'A' : ['B', 'C'],
  'B' : ['D', 'E', 'F'],
  'C' : ['G'],
  'D' : [],
  'E' : [],
  'F' : ['H'],
  'G' : ['I'],
  'H' : [],
  'I' : []
}


def breadth_first_search(graph, node):
    visited = set()
    queue = deque()
    visited.add(node)
    queue.append(node)

    while queue:
        # popleft is O(1). For an array, pop(0) is O(n). Hence the change to deque from array.
        s = queue.popleft()
        print(s, end = ' ')

        for n in graph[s]:
            # Because visited is a set, this lookup is O(1).
            if n not in visited:
                visited.add(n)
                queue.append(n)


def main():
    breadth_first_search(graph, 'A')


main()