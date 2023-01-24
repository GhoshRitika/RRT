import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np 
import random

def main():
    sd = 2
    domain = (100,100, 100)
    qinit = qrandom(domain)
    getRRT(domain, sd, qinit)


def qrandom(D):
    qrand= (random.randint(0,D[0]), random.randint(0,D[1]), random.randint(0,D[2]))
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
    z = a[2] - b[2]
    dist = ((x**2 + y**2 + z**2)**0.5)
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
    # plt.rcParams["figure.figsize"] = [7.5, 3.50]
    # plt.rcParams["figure.autolayout"] = True
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d') 
    ax.axes.set_xlim3d(left=0, right=100) 
    ax.axes.set_ylim3d(bottom=100, top=0) 
    ax.axes.set_zlim3d(bottom=0, top=100) 
    plt.title("A simple RRT with " +str(k) + " iterations")
    plt.ion()
    plt.pause(5)
    ax.scatter(qi[0], qi[1], qi[2], s =3, c = 'green')
    plt.pause(0.0001)
    for i in range(k):
        ran = qrandom(D)
        near = nearest(G,ran)
        qnewconfig = new_config(near, ran, SD)
        T.append([near,qnewconfig])
        G.append(qnewconfig)
        ax.scatter(qnewconfig[0], qnewconfig[1], qnewconfig[2], s =4, c = 'green')
        ax.plot([near[0], qnewconfig[0]], [near[1], qnewconfig[1]], [near[2], qnewconfig[2]], 'green')
        plt.pause(0.0001)
    plt.pause(1)


if __name__ == '__main__': 
    main()