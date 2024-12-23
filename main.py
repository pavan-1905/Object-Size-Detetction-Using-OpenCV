from google.colab.patches import cv2_imshow
import cv2
import numpy as np
from scipy.spatial import distance as dist
from imutils import perspective
import imutils

# Function to compute the midpoint between two points
def midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

# Example input parameters
pixels_per_metric = None  # Replace this with actual calibration data

# Load the image, convert it to grayscale, and blur it slightly
image = cv2.imread('/content/testimg2.jpg')  # Replace with your actual image path

# Resize the image to reduce its dimensions
scale_percent = 50  # Adjust this percentage as needed
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Grayscale and blur
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 0)

# Perform edge detection, then perform a dilation + erosion to
# close gaps in the edges
edged = cv2.Canny(gray, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)

# Find contours in the edge map
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# Loop over the contours
for c in cnts:
    # If the contour is too small, ignore it
    if cv2.contourArea(c) < 100:
        continue

    # Compute the rotated bounding box of the contour
    box = cv2.minAreaRect(c)
    box = cv2.boxPoints(box) if imutils.is_cv3() else cv2.boxPoints(box)
    box = np.array(box, dtype="int")

    # Order the points in the contour and draw them
    box = perspective.order_points(box)
    cv2.drawContours(image, [box.astype("int")], -1, (0, 255, 0), 2)

    # Loop over the points and draw them
    for (x, y) in box:
        cv2.circle(image, (int(x), int(y)), 5, (0, 0, 255), -1)

    # Compute midpoints
    (tl, tr, br, bl) = box
    (tltrX, tltrY) = midpoint(tl, tr)
    (blbrX, blbrY) = midpoint(bl, br)
    (tlblX, tlblY) = midpoint(tl, bl)
    (trbrX, trbrY) = midpoint(tr, br)

    # Draw the midpoints and connecting lines
    cv2.circle(image, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
    cv2.circle(image, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
    cv2.circle(image, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
    cv2.circle(image, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)
    cv2.line(image, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)), (255, 0, 255), 2)
    cv2.line(image, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)), (255, 0, 255), 2)

    # Compute the Euclidean distances
    dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
    dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))

    # If pixels per metric is None, initialize it
    if pixels_per_metric is None:
        pixels_per_metric = dB / 0.955  # Replace 0.955 with the actual reference width in inches

    # Compute the size of the object
    dimA = dA / pixels_per_metric
    dimB = dB / pixels_per_metric

    # Print the dimensions of the detected object
    print(f"Object Dimensions: Width = {dimA:.1f} inches, Height = {dimB:.1f} inches")

    # Draw the dimensions on the image
    cv2.putText(image, "{:.1f}in".format(dimA), (int(tltrX - 15), int(tltrY - 10)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)
    cv2.putText(image, "{:.1f}in".format(dimB), (int(trbrX + 10), int(trbrY)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)

# Show the output image
cv2_imshow(image)
cv2.waitKey(0)
