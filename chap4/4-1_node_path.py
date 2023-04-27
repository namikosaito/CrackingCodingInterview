# coding: utf-8
from collections import deque

"""
有向グラフが与えられたときに、二つのノード間に経路があるかどうかを判定

# VISUAL OF TEST GRAPH:

# A -- B
# |    |
# C -- D
# |
# E -- F -- G -- H
#      | \
#      O   I -- J -- K
#               |
#               L

# P -- Q
# |  /
# R
"""
# 再帰
def is_route(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    for node in graph[start]:
        if node not in visited:
            visited.add(node)
            if node == end or is_route(graph, node, end, visited):
                return True
        return False

# 幅優先探索
def is_route_bfs(graph, start, end):
    if start == end:
        return True
    visited = set()
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        for adjacent in graph[node]:
            if adjacent == end:
                return True
            else:
                queue.append(adjacent)
        visited.add(node)
        return False
            


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D", "E"],
        "D": ["B", "C"],
        "E": ["C", "F"],
        "F": ["E", "O", "I", "G"],
        "G": ["F", "H"],
        "H": ["G"],
        "I": ["F", "J"],
        "O": ["F"],
        "J": ["K", "L", "I"],
        "K": ["J"],
        "L": ["J"],
        "P": ["Q", "R"],
        "Q": ["P", "R"],
        "R": ["P", "Q"],
    }

    tests = [
        ("A", "L", False),
        ("A", "B", True),
        ("H", "K", False),
        ("L", "D", False),
        ("P", "Q", True),
        ("Q", "P", True),
        ("Q", "G", False),
        ("R", "A", False),
        ("P", "B", False),
    ]

    for [start, end, expected] in tests:
        answer = is_route(graph, start, end)
        # print(answer)
        assert answer == expected

    for [start, end, expected] in tests:
        answer = is_route_bfs(graph, start, end)
        assert answer == expected
