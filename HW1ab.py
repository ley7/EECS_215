
"""
@author: Zhou Fang
"""

import networkx as nx
import matplotlib.pyplot as plt
import Queue
import numpy as np
import sys

actorArr=[]
movieArr=[]


def exab_graph(filename):
    g = nx.Graph()
    dict = {}
    with open(filename) as fp:
        for line in fp:
            actor_in_movie=line.strip().split("|")
            actor = actor_in_movie[0]
            movie = actor_in_movie[1]
            actorArr.append(actor)
            movieArr.append(movie)
            if movie in dict:
                old_actor = dict.get(movie)
                old_actor.append(actor)
                dict[movie] = old_actor
            else:
                dict[movie] = [actor]
            g = nx.Graph()

        for movie in dict:
            actors = dict.get(movie)
            for i in range(len(actors)):
                for j in range(i+1, len(actors)):
                    g.add_edge(actors[i], actors[j])
        # for i in range(len(movieArr)):
        #         for j in range(len(movieArr)):
        #             if movieArr[i]==movieArr[j]:
        #                 if i!=j:
        #                     g.add_edge(actorArr[i],actorArr[j])

        return g
        #movieArr.index(1)
        #print movieArr.index(1)

def draw_graph(g):
    
    nx.draw_networkx(g)
    # Draw graph in separate window.
    plt.show() 

def run_bfs_using_nx(g, s):
    
    bfs_tree = nx.bfs_tree(g,s)
    draw_graph(bfs_tree)
    
def run_dfs_using_nx(g, s):
    
    dfs_tree = nx.dfs_tree(g,s)
    draw_graph(dfs_tree)
    
def bfs(g, s, distance):
  queue = Queue.Queue()
  distance[s] = 0;
  d = 0
  queue.put(s)
  while not queue.empty():
    node = queue.get()
    g_neighbors = g.neighbors(node)
    # d = d + 1
    for neighbor in g_neighbors:
        if distance[neighbor] < 0:
            queue.put(neighbor)
            distance[neighbor] = distance[node] + 1

def main(fn, s):
    g = exab_graph(fn)
    #draw_graph(g)#for small input
    #run_bfs_using_nx(g,actorArr[s])
    #run_dfs_using_nx(g,actorArr[s])# for large input
    nodeArr = g.nodes()

    # length = nx.single_source_shortest_path_length(g, actorArr[s])#compute shorest path of the

    #print node test
    #for node in length:
       #print('{}: {}'.format(node, length[node]))
    # print length

    distance = {}
    for actor in actorArr:
        distance[actor] = -1
    bfs(g, actorArr[s], distance)
    distanceList = []
    for actor in distance:
        distanceList.append(distance[actor])
    maxValue = max(distanceList)
    for i in range(maxValue+1):
         print str(i)+"\t\t\t\t"+str(distanceList.count(i))
    print "Unreachable:"+"\t"+str(distanceList.count(-1))
    print "----------"

    # unreach = 0
    # for item in nodeArr:
    #     if not nx.has_path(g, source=actorArr[s], target=item):
    #         unreach = unreach + 1
    #
    # temp=[]
    # for node in length:
    #     temp.append(length[node])
    # temp = sorted(temp)
    # #print temp
    # maxValue = temp[len(temp)-1]
    # #print maxValue#max value
    # #print range(maxValue)
    # print str("BaconNumber")+" "+str("Frequency")
    # for i in range(maxValue+1):
    #     if not temp.count(i) == 0:
    #         print str(i)+"\t\t\t\t"+str(temp.count(i))
    #
    # print "Unreachable:"+"\t"+str(unreach)

if __name__ == "__main__":
    #print sys.argvif
    #len(sys.argv) == 3:
        fn = "input3.txt"#sys.argv[1]  # Filename
        s  = "428"#sys.argv[2] # Source node
        main(fn,int(s))
