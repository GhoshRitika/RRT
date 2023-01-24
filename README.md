# Rapidly-Exploring Random Tree
## Simple RRT
Implemented a RRT in 2D domain, D=[0, 100]x[0, 100] with an initial configuration of (50, 50) and incremental distancee, d = 1. The reult is plotted for input number of vertices, K.
* The video below shows the RRT uniformly covering the whole space for a K = 1000.

[Simple RRT](https://user-images.githubusercontent.com/60728026/214358940-66b73a73-9ce9-427d-9737-9bebee50ec09.mp4)

## RRT with Circular Obstacles
This RRT has the same domain but it has a random amount of circular obstacles of varying radii along with an initial and goal position. This RRT runs as long as it does not find an obstacles free straight line path to the goal position.
*The video below shows the RRT with circular obstacles in its path.

[RRT Obstacles](https://user-images.githubusercontent.com/60728026/214363661-18daab9d-c86d-442d-89e3-e6b59bafa9c2.mp4)