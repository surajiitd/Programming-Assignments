"""
Starter code for EECS 442 W21 HW1
"""
import os
import cv2
import numpy as np
import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt
from util import generate_gif, renderCube


def rotX(theta):
    """
    Generate 3D rotation matrix about X-axis
    Input:  theta: rotation angle about X-axis
    Output: Rotation matrix (3 x 3 array)
    """
    pass


def rotY(theta):
    """
    Generate 3D rotation matrix about Y-axis
    Input:  theta: rotation angle along y-axis
    Output: Rotation matrix (3 x 3 array)
    """
    pass


def part1():
    # TODO: Solution for Q1
    # Task 1: Use rotY() to generate cube.gif

    # Task 2:  Use rotX() and rotY() sequentially to check
    # the commutative property of Rotation Matrices
    
    # Task 3: Combine rotX() and rotY() to render a cube 
    # projection such that end points of diagonal overlap
    # Hint: Try rendering the cube with multiple configrations
    # to narrow down the search region
    pass


def split_triptych(trip):
    """
    Split a triptych into thirds
    Input:  trip: a triptych (H x W matrix)
    Output: R, G, B martices
    """
    R, G, B = None, None, None
    # TODO: Split a triptych into thirds and 
    # return three channels as numpy arrays
    return R, G, B


def normalized_cross_correlation(ch1, ch2):
    """
    Calculates similarity between 2 color channels
    Input:  ch1: channel 1 matrix
            ch2: channel 2 matrix
    Output: normalized cross correlation (scalar)
    """
    pass


def best_offset(ch1, ch2, metric, Xrange=np.arange(-10, 10), 
                Yrange=np.arange(-10, 10)):
    """
    Input:  ch1: channel 1 matrix
            ch2: channel 2 matrix
            metric: similarity measure between two channels
            Xrange: range to search for optimal offset in vertical direction
            Yrange: range to search for optimal offset in horizontal direction
    Output: optimal offset for X axis and optimal offset for Y axis

    Note: Searching in Xrange would mean moving in the vertical 
    axis of the image/matrix, Yrange is the horizontal axis 
    """
    # TODO: Use metric to align ch2 to ch1 and return optimal offsets
    pass


def align_and_combine(R, G, B, metric):
    """
    Input:  R: red channel
            G: green channel
            B: blue channel
            metric: similarity measure between two channels
    Output: aligned RGB image 
    """
    # TODO: Use metric to align the three channels 
    # Hint: Use one channel as the anchor to align other two
    pass


def pyramid_align():
    # TODO: Reuse the functions from task 2 to perform the 
    # image pyramid alignment iteratively or recursively
    pass


def part2():
    # TODO: Solution for Q2
    # Task 1: Generate a colour image by splitting 
    # the triptych image and save it 

    # Task 2: Remove misalignment in the colour channels 
    # by calculating best offset
    
    # Task 3: Pyramid alignment
    pass


def part3():
    # TODO: Solution for Q3
    pass
    

def main():
    part1()
    part2()
    part3()


if __name__ == "__main__":
    main()
