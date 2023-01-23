import numpy as np
from matplotlib import pyplot as plt
import RRTtask1 as t1
from math import isclose
import cv2

#https://www.tutorialspoint.com/opencv-python-how-to-convert-a-colored-image-to-a-binary-image
#https://stackoverflow.com/questions/48121916/numpy-resize-rescale-image
def main():
    f, ax = plt.subplots()
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.ion()
    im = cv2.imread('/home/ritz/hackathon/RRT-challenge/RRTrepo/NWlogo.jpg')
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    original_image = np.asarray(im_gray)
    width , height = 100,100
    resize_image = np.zeros(shape=(width,height))

    for W in range(width):
        for H in range(height):
            new_width = int( W * original_image.shape[0] / width )
            new_height = int( H * original_image.shape[1] / height )
            resize_image[W][H] = original_image[new_width][new_height]

    obj = np.flipud(resize_image)
    imgplot = plt.imshow(obj, origin = 'lower', cmap='gray')
    plt.pause(5)

if __name__ == '__main__':
    main()