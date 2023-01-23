import matplotlib.pyplot as pt
from matplotlib.collections import LineCollection
import numpy as np 
import random
import os
import time
import math

def main():
    sd = 1
    domain = (100,100)
    qinit = (50,50)
    getRRT(domain, sd, qinit)


def qrandom(D):
    qrand= (random.randint(0,D[0]), random.randint(0,D[1]))
    return qrand

def nearest(G, qrand):
    dist = []
    for i in G:
        dist.append(get_distance(qrand, i)) 
    m = dist.index(min(dist))
    return G[m]

def get_distance(a,b):
    x = a[0]- b[0]
    y = a[1] - b[1]
    dist = ((x**2 + y**2)**0.5)
    return dist


def new_config(qnear,qrandom, d):
    if qnear == qrandom:
        return qnear
    v1 = np.array(qrandom)
    v2 = np.array(qnear)
    v3 = v1 - v2 
    u3 = (v3/get_distance(v1, v2)) *d 
    qnew = tuple(v2 + u3)
    return qnew

    
def getRRT(D, SD, qi):
    G = [qi]
    T= []
    k = int(input('Enter value of K:'))
    f, ax = pt.subplots(figsize=[10,10])
    pt.xlim(0, 100)
    pt.ylim(0, 100)
    pt.title("A simple RRT with " +str(k) + " iterations")
    pt.ion()
    pt.plot(qi[0], qi[1], '.b', markersize=5)
    pt.pause(5)            #pt.pause(0.0001)
    for i in range(k):
        ran = qrandom(D)
        near = nearest(G,ran)
        qnewconfig = new_config(near, ran, SD)
        T.append([near,qnewconfig])
        G.append(qnewconfig)
        pt.xlim(0, 100)
        pt.ylim(0, 100)
        # pt.ion()
        # pt.plot(qnewconfig[0], qnewconfig[1], '.b', markersize=5)
        # lc = LineCollection(T)
        # ax.add_collection(lc)
        pt.plot([near[0], qnewconfig[0]], [near[1],qnewconfig[1]], 'b.-', markersize=5)
        pt.pause(0.0001)
    pt.pause(1)


if __name__ == '__main__': 
    main()