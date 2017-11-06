import sys
import resource
from collections import defaultdict
import logging
logger = logging.getLogger()

# Increase recursion depth and stack size
sys.setrecursionlimit(100000)
resource.setrlimit(resource.RLIMIT_STACK,
                   (resource.RLIM_INFINITY, resource.RLIM_INFINITY))


def setup_debug_logger():
    handler = logging.StreamHandler()
    global logger
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)


def read_lines(file_name):
    g, gr = defaultdict(list), defaultdict(list)
    with open(file_name) as f:
        for line in f:
            nodes = map(int, line.strip().split(' '))
            g[nodes[0]].append(nodes[1])
            gr[nodes[1]].append(nodes[0])
    logger.debug("graph nodes number is {0}".format(len(g)))
    return g, gr


def dfs(g, start_node, visited_nodes):
    # iterative DFS does not work to measure finish time
    # thinking how to measure finish time...
    trace = []

    # add start node
    stack = [start_node]
    print start_node, "it visited"
    visited_nodes.add(start_node)
    trace.append(start_node)

    while stack:
        next_node = stack.pop()  # different with BFS
        for v in g[next_node]:
            if v not in visited_nodes:
                print v, "it visited"
                visited_nodes.add(v)
                trace.append(v)
                stack.append(v)

    return trace


def dfs_loop(g):
    # loop through the whole graph to deal with isolated nodes
    # use set is more efficient than list to remember nodes visited
    visited_nodes, final_trace = set(), []

    for k in g.keys():
        if k not in visited_nodes:
            trace = dfs(g, k, visited_nodes)
            trace.reverse()
            final_trace.extend(trace)

    return final_trace


def dfs_rec(g):
    # iterative DFS does not work here
    visited_nodes, trace = set(), []

    def inner_dfs(v):
        print v, "rec visited"
        visited_nodes.add(v)
        for u in g[v]:
            if u not in visited_nodes:
                inner_dfs(u)
        trace.append(v)

    for u in graph.keys():
        if u not in visited_nodes:
            inner_dfs(u)
    return trace


def scc(g, gr):
    visited_nodes, scc_graph = set(), defaultdict(list)

    # trace0 = dfs_loop(g)
    trace = dfs_rec(g)
    # logger.debug("trace is {0}".format(trace))
    # test two method
    # print trace0 == trace1
    # print 'trace0', trace0
    # print 'trace1', trace1

    for node in reversed(trace):
        if node not in visited_nodes:
            # DFS of the reversed graph
            visited_nodes.add(node)
            stack = [node]
            while stack:
                next_node = stack.pop()
                for v in gr[next_node]:
                    if v not in visited_nodes:
                        visited_nodes.add(v)
                        stack.append(v)
                scc_graph[node].append(next_node)

    return scc_graph


if __name__ == "__main__":
    setup_debug_logger()
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        graph, graph_reversed = read_lines(file_name)
        scc_graph = scc(graph, graph_reversed)
        top_scc = sorted(map(len, scc_graph.values()))[::-1][:10]
        print("Top SCC list is {0}".format(top_scc))
    else:
        print("Please provide file name!")
