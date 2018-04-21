from priodict import priorityDictionary
from collections import namedtuple

ConnectionData = namedtuple("ConnectionData", "dist angle")

def get_hint(board, cur_pos, end):
    path_to_end = shortestPathLoc(board, cur_pos, end)
    return get_connection(board, path_to_end[0], path_to_end[1])

def get_connection(board, at, nxt):
    for direction, pos in board.layout[at].items():
        if pos == nxt:
            return direction
    raise ValueError("No direct path from " + at + " to " + nxt)

def shortestPathLoc(b, start, end):
    """Computes the points, in order, of the shortest path between two nodes"""
    D,P = dijkstra(b, start,end)
    if not (end in P):
        raise ValueError("Cannot reach the node %s" % end)
    Path = []
    Path.append(end)
    while end != start:
        end = P[end]
        Path.append(end)
    Path.reverse()
    return Path

def dijkstra(board, start, end=None):
    """Does Dijkstra's algorithm. If end is specified,
    it only looks until it finds the specified node. Returns a tuple:
    (final distances, paths)
    paths: p[elem] will give the predecesor of elem
    """
    adj = board.layout
    D = {} # dictionary of final distances
    P = {} # dictionary of predecessors
    Q = priorityDictionary() # estimated distances of non-final vertices
    Q[start] = 0

    # iterates over the priority queue's keys, remove as you go.
    for v in Q:
        D[v] = Q[v]
        if v == end:
            break;

        for w in adj[v]:
            cur_pos = board.get_new_pos(v, w)
            vwLength = D[v] + 1
            if cur_pos in D:
                if vwLength < D[cur_pos]:
                    raise ValueError("Dijkstra: found better path to already-final vertex")
            elif cur_pos not in Q or vwLength < Q[cur_pos]:
                Q[cur_pos] = vwLength
                P[cur_pos] = v
    return (D,P)

if __name__ == "__main__":
    import sys
    import board
    b = board.Board()
    print(get_hint(b, int(sys.argv[1]), int(sys.argv[2])))
