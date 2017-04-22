#!/usr/bin/env python

from collections import defaultdict

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.distances[(from_node, to_node)] = distance


def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes:
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node
    if min_node is None:
      break


    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distances[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path

def create_graph(N, dists, horses):
    initial_graph = Graph()
    for i in xrange(N):
        initial_graph.add_node(i)
    for v in xrange(N):
        for u in xrange(N):
            d = dists[v][u]
            if d >= 0:
                initial_graph.add_edge(v, u, dists[v][u])
    over_graph = Graph()
    for i in xrange(N):
        over_graph.add_node(i)
    for v in xrange(N):
        distance, speed = horses[v]
        visited, _ = dijsktra(initial_graph, v)
        for u, d in visited.iteritems():
            if 0 < d <= distance:
                over_graph.add_edge(v, u, d/float(speed))
    return over_graph


def solve():
    N, Q = [int(i) for i in raw_input().split()]
    horses = [[int(i) for i in raw_input().split()] for j in xrange(N)]
    dists = [[int(i) for i in raw_input().split()] for j in xrange(N)]
    queries = [[int(i) for i in raw_input().split()] for j in xrange(Q)]
    over_graph = create_graph(N, dists, horses)
    sol = []
    for i in xrange(Q):
        v, u = queries[i]
        visited, _ = dijsktra(over_graph, v-1)
        sol.append(visited[u-1])
    return ' '.join(str(s) for s in sol)


def main():
    T = int(raw_input())
    for i in xrange(T):
        sol = solve()
        print 'Case #{}: {}'.format(i+1, sol)


if __name__ == '__main__':
    main()
