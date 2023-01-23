import numpy as np
from matplotlib import pyplot as plt
import RRTtask1 as t1
from math import isclose

def main():
    domain = (100, 100)
    sd = 1
    f, ax = plt.subplots()
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.title("A with RRT with obstacles and a goal")
    centers, rad = printCircle(domain, ax)
    plt.ion()
    plt.pause(10)
    start = getpoint(centers, rad, domain)
    plt.plot(start[0],start[1], color='g', marker='o', markersize=10)
    plt.pause(0.1)
    print(start)
    end = getpoint(centers,rad, domain)
    plt.plot(end[0], end[1], color='r', marker='X', markersize=10)
    plt.pause(0.1)
    print(end)
    graph, tree= gettree(sd, start, end, centers, rad, domain)
    # lc = LineCollection(tree)
    # ax.add_collection(lc)
    # plt.pause(1)
    # plt.scatter(*zip(*graph), s=8)
    # plt.pause(1)
    # plt.show()
    # plt.pause(1)
    print(len(graph))
    returnpath(graph, tree, start)
    
def printCircle(d, ax):
    i = np.random.randint(50, 60)
    center = []
    radii = []
    for j in range(i):
        np.random.seed()
        r = np.random.randint(2, 10)
        (x, y) = t1.qrandom(d)
        center.append((x,y))
        radii.append(r)
        c = plt.Circle((x,y),r)
        c.set_facecolor('yellow')
        ax.add_patch(c)
    #return f, ax
    #plt.show()
    return center, radii

def checkobstacle(p1,p2,c,r):
    a =p1[1] - p2[1]
    b = p2[0] - p1[0]
    m = p1[0]*p2[1] - p2[0]*p1[1]
    
    Flag = True #no collision
    for i in range(len(r)):
        p = c[i]
        #checking for circles with centers within their radius range from the points
        if min(p1[0], p2[0]) - r[i] < p[0]< max(p1[0], p2[0]) + r[i] and min(p1[1], p2[1]) - r[i] < p[1]< max(p1[1], p2[1]) + r[i]:
            try:
                dist = abs((a * p[0] + b * p[1] + m) /((a * a + b * b)**0.5)) 
            except ZeroDivisionError:
                dist =0
            # here it was checking entire line, so even if intersected at another section
            if (dist <= r[i]):
                Flag = False # False if it intersects or touches
                break
    #print (Flag)
    return Flag
            

def checkpoints(p, c, r):
    len = t1.get_distance(p, c)
    return len > r 

def getpoint(c, r, d):
    while(True):
        pt = t1.qrandom(d)
        #print(pt)
        flag = True
        for i in range(len(r)):
            if checkpoints(pt, c[i], r[i]) != True:
                flag = False
                break
        if flag == True:
            return pt

def gettree(d, init, goal, cc, cr, D):
    G = [init]
    tree = []
    #temp = G.copy()
    l = 0
    k = 5000
    for i in range(k):
        if checkobstacle(G[-1], goal, cc, cr) == True:
            plt.plot([G[-1][0], goal[0]], [G[-1][1], goal[1]], 'b.-')
            plt.show()
            plt.pause(0.0001)
            tree.append([G[-1],goal])
            G.append(goal)
            # plt.plot(goal[0], goal[1], '.b', markersize=5)
            break
        flag = True
        count = 0
        while(flag and count<100):
            count+=1
            qr =  getpoint(cc, cr, D)
            qnear = t1.nearest(G, qr)
            qnew = t1.new_config(qnear, qr, d)
            outside_circles = True
            for i in range(len(cr)):
                if checkpoints(qnew, cc[i], cr[i]) != True:
                    outside_circles = False
                    break
            if (outside_circles == True):
                tree.append([qnear,qnew])
                G.append(qnew)
                plt.plot(qnew[0], qnew[1], '.b', markersize=5)
                plt.plot([qnear[0], qnew[0]], [qnear[1],qnew[1]], 'b-')
                plt.pause(0.0001)
                flag = False
    return G, tree

def returnpath(G, T, init):
    plt.plot([G[-1][0], G[-2][0]], [G[-1][1],G[-2][1]], 'r.-', markersize=5)
    plt.pause(0.0001)
    if len(G)>2:
        past = G[-2]
        current=G[-3]
        i = -3
        while(current[0]!=init[0] or current[1]!=init[1]):
            if i<-1*(len(G)):
                break
            current = G[i]
            if (isclose(t1.get_distance(past, current), 1.0, abs_tol=1e-8)):
                plt.plot([past[0], current[0]], [past[1],current[1]], 'r.-', markersize=5)
                plt.pause(0.0001)
                past = current
            i-=1
        plt.pause(1)




if __name__ == '__main__':
    main()
