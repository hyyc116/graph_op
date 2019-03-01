#coding:utf-8

from basic_config import *

def find_longest_path_to_leaves(G,root):
    ## 首先找到出度为0的叶子结点
    leaves = []
    for node,od in  G.out_degree():

        if od==0:
            leaves.append(node)

    ## 计算最长距离
    long_paths = []
    for leaf in leaves:
        ### 目前来看只能用这个方法，但是在复杂的图上会失效，这个方法列举出所有的路径，从中选择一个最长的
        paths = nx.all_simple_paths(G,root,leaf)

        longest_path = sorted(paths,key=lambda x:len(x),reverse=True)[0]

        # print root,leaf,longestpath
        long_paths.append(longest_path)

    return long_paths


def visualize_graph(edges,name):
    plot_a_subcascade(edges,name)


if __name__ == '__main__':
    edges = [('P','P1'),('P','P3'),('P','P4'),('P','P2'),('P','P5'),('P1','P3'),('P2','P4'),('P1','P4'),('P3','P5'),('P1','P5'),('P2','P5')]
    visualize_graph(edges,'input')

    G = nx.DiGraph()
    G.add_edges_from(edges)

    long_paths = find_longest_path_to_leaves(G,'P')

    nG = nx.DiGraph()
    for path in long_paths:
        nG.add_path(path)

    visualize_graph(nG.edges(),'output')

