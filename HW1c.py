"""
@author: Zhou Fang
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import sys

actorArr = []
movieArr = []


def exc_graph(filename):
    g = nx.Graph()
    with open(filename) as fp:
        for line in fp:
            actor_in_movie = line.strip().split("|")
            actor = actor_in_movie[0]
            movie = actor_in_movie[1]

            actorArr.append(actor)
            movieArr.append(movie)
            g = nx.Graph()

        for i in range(len(actorArr)):
            g.add_edge(actorArr[i], movieArr[i])

        return g
        # movieArr.index(1)
        # print movieArr.index(1)


def draw_graph(g):
    nx.draw_networkx(g)
    # Draw graph in separate window.
    plt.show()


def run_bfs_using_nx(g, s):
    bfs_tree = nx.bfs_tree(g, s)
    draw_graph(bfs_tree)


def run_dfs_using_nx(g, s):
    dfs_tree = nx.dfs_tree(g, s)
    draw_graph(dfs_tree)


def main(fn, s):
    g = exc_graph(fn)
    #draw_graph(g)#for small input check bipartie graph
    # run_bfs_using_nx(g,actorArr[s])
    # run_dfs_using_nx(g,actorArr[s])# for large input
    b=[]
    for x in actorArr:
        if x not in b:
            b.append(x)
    #print actorArr
    #print b
    unreach=0
    length=[]
    for i in range(len(b)):
         if not b[i]==actorArr[s]:
             if nx.has_path(g, source=actorArr[s], target=b[i]):
                length.append(nx.shortest_path_length(g,actorArr[s],b[i]))
             if not nx.has_path(g, source=actorArr[s], target=b[i]):
                    unreach = unreach + 1
         else:
                    length.append(0)

    print length
    temp = sorted(length)
    # print temp
    maxValue = temp[len(temp) - 1]
    # print maxValue#max value
    # print range(maxValue)
    print  str("BaconNumber") + " " + str("Frequency")
    for i in range(maxValue + 1):
        if not temp.count(i) == 0:
            print str(i/2) + "\t\t\t\t" + str(temp.count(i))

    print "Unreachable:" + "\t" + str(unreach)





if __name__ == "__main__":
    # print sys.argvif
    # len(sys.argv) == 3:
    fn = "input3.txt"  # sys.argv[1]  # Filename
    s = "428"  # sys.argv[2] # Source node
    main(fn, int(s))
    print actorArr[428]
    #print len(actorArr)
    #print len(movieArr)