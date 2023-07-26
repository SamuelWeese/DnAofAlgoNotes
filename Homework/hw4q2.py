# We can enumerate each vertex of the graph as below
# Where edges is a list of pointers
class vertice:
    def __init__(self, val):
        self.val = val
        self.edges = []
# If we pass graph, a pointer to a list of connected vertices, we can use the following algorithm
# graph is an array of vertices
def findSourcesSinks(graph):
# Initializing lists
    notSources = []
    sinks = []
# looping through each value, using vertex instead of vertice due to name clarity
    for vertex in graph:
# upon finding no output, it must be a sink
    if len(vertex.edges) == 0:
    sinks += vertex
    else:
# if it has output, it must be a source
    for edge in vertex.edges:
    if edge not in notSources: # checking for uniqueness
    notSources.append(edge)
# Since we know that a graph MUST be connected, we now just remove all sources which have input
# which we keep a list of in not sources
    sources = [i for i in graph if i not in notSources]
    return sources, sinks
