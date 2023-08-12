# Canny Edge Detection Implementation

This repository provides a Python implementation of the Canny Edge Detection algorithm from scratch. The Canny Edge Detection technique is widely used for detecting edges in images, making it a fundamental tool in computer vision and image processing applications.

## Introduction

Canny Edge Detection, developed by John F. Canny in 1986, is a multi-step process that identifies the edges in an image while suppressing noise. It has proven to be an essential technique in various fields, including object detection, image segmentation, and feature extraction.

## Usage

1. Install the necessary dependencies using the following command:
 
   ```bash
   pip install opencv-python numpy
   ```
   
2. Replace the `flower.png` with the path to your image.
  
3. Run `canny_edge_detection.py` using the following command:
   
   ```bash
   python canny_edge_detection.py
   ```

## Algorithm Overview

The Canny Edge Detection algorithm consists of several key steps:

1. **Noise Reduction with Gaussian Smoothing**: Apply Gaussian blur to reduce noise in the image.

2. **Gradient Calculation**: Compute gradient magnitude and orientation using Sobel operators.

3. **Non-Maximum Suppression**: Suppress non-maximum values to obtain thin edges.

4. **Double Thresholding**: Classify edge pixels as strong, weak, or non-edges using two thresholds.

5. **Edge Tracking by Hysteresis**: Connect weak edges to strong edges to complete edge contours.

## Article

For an in-depth understanding of the Canny Edge Detection algorithm and the steps involveds, you can refer to the article: [What is Canny Edge Detection?](https://www.educative.io/answers/what-is-canny-edge-detection)

Feel free to explore the provided code implementation and adapt it to your specific use cases. 
