# -*- coding: utf-8 -*- 
"""
Created on Mon Dec  1 09:07:39 2014

@author: snehasishbarman

Creates a directed friendship graph (with bidirectional edges) and uses page rank to 
compute the importance of every user in the graph.

"""

import json
import copy
import tabulate as tb
import sys

class DirectedGraphADT(object):
    
    def __init__(self):
        self.graph = {}
        self.noOfEdges = 0.0
        
    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        if v not in self.graph[u] and u not in self.graph[v]:
            self.graph[u].append(v)
            self.graph[v].append(u)
            self.noOfEdges += 1.0
    
    def showgraph_(self):
        for v in self.graph:
            print "%s: %s" % (v, self.graph[v])
            
    def vertices(self):
        return self.graph.keys()
        
    def getGraph(self):
        if self.graph == None or len(self.graph) == 0:
            raise Exception("Graph is empty")
        return self.graph
     
    def setGraph(self, graph):
        self.graph = graph
        
    def getNoOfEdges(self):
        return self.noOfEdges
        
        
def createGraph(users_file):
    graph = DirectedGraphADT()
    users = open("./"+users_file, "r", 1)
    try:
        for user in users:
            py_ = json.loads(user)
            user_id, friends = py_["user_id"], py_["friends"]
            for friend in friends:
                graph.addEdge(user_id, friend)
        return graph
    finally:
        users.close()
        
# Fr. = (1-d)/N + summ(d*Prank(v)/outgoing edges)
def computePageRank(graph, damping_factor = 0.80, eps = 0.00001):
    vertices = len(graph.vertices())    
    old_prank, new_prank = {}, {}
    for vertex in graph.vertices():
        old_prank[vertex] = 1.0/vertices
    for iter_ in range(1, 101):
        print "Iteration: %d" % iter_        
        diff = []
        for u in graph.vertices():
            rank = (1-damping_factor)/vertices
            for v in graph.vertices():
                if u in graph.getGraph()[v]:
                    rank += damping_factor*old_prank[v]/len(graph.getGraph()[v])
            diff.append(abs(old_prank[u] - rank))
            new_prank[u] = rank
        old_prank = copy.deepcopy(new_prank)
        new_prank.clear()
        if sum(diff) < eps:
            print "Total iterations: %d" % iter_
            break
    return old_prank

def topthirtyusers(scores):
    """
    Display the top 30 users in the graph ranked by
    their page rank scores
    """
    table = sorted(scores.items(), key = lambda x: x[1], reverse = True)
    headers = ["User", "PageRank Score"]
    print tb.tabulate(table[:30], headers, tablefmt = "rst")
    



# Test Case: http://www.dcs.bbk.ac.uk/~dell/teaching/ir/examples/pr_example.pdf
graph = DirectedGraphADT()
graph.setGraph({"A":["B"], "B":["A", "C"], "C":["B"]})
ranks = computePageRank(graph, 0.7)
print ranks

# Actual
graph = createGraph(USERS_FILE)
print len(graph.vertices())
print graph.getNoOfEdges()
graph.showgraph_()           
len(graph.getGraph()["Cw3UMmYeqqx1u4HIWaWw3w"])
ranks = computePageRank(graph, 0.8)
print ranks
topthirtyusers(ranks)






    
