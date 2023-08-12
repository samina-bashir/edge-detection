import cv2
import numpy as np

def canny_edge_detection(image, sigma=1.0, low_threshold=50, high_threshold=100):
    # Step 1: Noise Reduction with Gaussian Smoothing
    blurred_image = cv2.GaussianBlur(image, (5, 5), sigma)
    cv2.imwrite('noise_reduction.png', blurred_image)
    # Step 2: Gradient Calculation
    gradient_x = cv2.Sobel(blurred_image, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y = cv2.Sobel(blurred_image, cv2.CV_64F, 0, 1, ksize=3)

    gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
    gradient_orientation = np.arctan2(gradient_y, gradient_x)
    cv2.imwrite('sobel_gradient.png', gradient_magnitude)

    # Step 3: Non-Maximum Suppression
    suppressed_gradient = np.zeros_like(gradient_magnitude)
    for i in range(1, gradient_magnitude.shape[0] - 1):
        for j in range(1, gradient_magnitude.shape[1] - 1):
            angle = gradient_orientation[i, j] * (180.0 / np.pi)
            if (0 <= angle < 22.5) or (157.5 <= angle <= 180):
                neighbor_magnitudes = [gradient_magnitude[i, j - 1], gradient_magnitude[i, j + 1]]
            elif (22.5 <= angle < 67.5):
                neighbor_magnitudes = [gradient_magnitude[i - 1, j + 1], gradient_magnitude[i + 1, j - 1]]
            elif (67.5 <= angle < 112.5):
                neighbor_magnitudes = [gradient_magnitude[i - 1, j], gradient_magnitude[i + 1, j]]
            else:
                neighbor_magnitudes = [gradient_magnitude[i - 1, j - 1], gradient_magnitude[i + 1, j + 1]]

            if gradient_magnitude[i, j] >= max(neighbor_magnitudes):
                suppressed_gradient[i, j] = gradient_magnitude[i, j]
    cv2.imwrite('suppression.png', suppressed_gradient)


    # Step 4: Double Thresholding
    edges = np.zeros_like(suppressed_gradient)
    edges[(suppressed_gradient >= high_threshold)] = 255
    weak_edges = np.zeros_like(suppressed_gradient)
    weak_edges[(suppressed_gradient >= low_threshold) & (suppressed_gradient < high_threshold)] = 255
    cv2.imwrite('double_thresholding.png', edges)


    # Step 5: Edge Tracking by Hysteresis
    rows, cols = edges.shape
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if edges[i, j] == 255:
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if weak_edges[i + x, j + y] == 255:
                            edges[i + x, j + y] = 255

    return edges

# Load an image
image = cv2.imread('flower.png', cv2.IMREAD_GRAYSCALE)

# Apply Canny edge detection
canny_edges = canny_edge_detection(image, sigma=1, low_threshold=60, high_threshold=160)

# Save the Canny edges as an image file
cv2.imwrite('canny_edges.jpg', canny_edges)
