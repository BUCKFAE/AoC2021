

from collections import namedtuple
from dataclasses import dataclass, field
import sys
import heapq
from typing import List, Optional, Tuple, Type, ClassVar


board = []

with open("day-15/input.txt") as f:
    file_content = [line.strip() for line in f.readlines() if line.strip()]
    board = [[int(i) for i in line] for line in file_content]

def print_board(board):
    print('\n'.join([''.join([str(i) for i in line]) for line in board]))

print_board(board)

edge = namedtuple('Edge', 'node, cost')

@dataclass
class Node:
    board_pos_x: int
    board_pos_y: int
    adj: List[edge] = field(default_factory=list)
    visited: bool = False
    distance: float = float('inf')

    def __lt__(self, other):
        return self.distance < other.distance

def get_tile_at(x: int, y: int) -> Optional[int]:
    if x < 0 or y < 0:
        return None
    if x >= len(board[0]) or y >= len(board):
        return None
    return board[y][x]

def get_node_at(x: int, y: int) -> Node:
    return nodes[y * len(board[0]) + x]

nodes: List[Node] = []

nodes = [Node(x, y) for x in range(len(board[0])) for y in range(len(board))]

for y, row in enumerate(board): 
    for x, col in enumerate(row):

        print(f'Coordinates: {x} {y}')
        curr = get_node_at(x, y)
        curr_cost = get_tile_at(x, y)
        for mod_x, mod_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:

            if neighbor := get_tile_at(x + mod_x, y + mod_y):
                neighbor_node = get_node_at(x + mod_x, y + mod_y)

                curr.adj.append(edge(neighbor_node, neighbor))
                neighbor_node.adj.append(edge(curr, curr_cost))

def dijkstra(nodes, start):

    start.distance = 0

    heap = []
    heapq.heapify(heap)

    heapq.heappush(heap, (start.distance, start))

    while heap:
        _, u = heapq.heappop(heap)
        if u.visited:
            continue

        u.visited = True
        for v, c in u.adj:
            alt = u.distance + c
            if alt < v.distance:
                v.distance = alt
                heapq.heappush(heap, (v.distance, v))

dijkstra(nodes, get_node_at(0, 0))
print(get_node_at(len(board) - 1, len(board[0]) - 1).distance)