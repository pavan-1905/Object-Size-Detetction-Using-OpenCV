Image Dimension Detection with OpenCV
This project demonstrates how to use OpenCV for image processing, including object dimension detection and display. The primary functionality includes detecting contours in an image, calculating the bounding box for each object, and determining its dimensions (in inches) based on a pixel-per-metric conversion. Additionally, the program resizes the image, detects edges, and displays the object dimensions along with the image's size.

Features
1. **Image Resize: Resizes the input image to a reduced size for faster processing.**
2. **Contour Detection: Identifies the contours of objects within the image.**
3. **Bounding Box: Computes and draws the rotated bounding box for each object.**
Midpoints and Connecting Lines: Marks the midpoints of the bounding box edges and draws connecting lines.
Euclidean Distance: Calculates the Euclidean distance between points in the bounding box to determine the dimensions.
Pixel to Metric Conversion: Converts the dimensions of the detected objects from pixels to real-world units (inches) using a given reference.
Text Annotations: Annotates the image with the calculated dimensions and image size.
Requirements
To run the project, you need the following Python libraries:

Python 3.x
OpenCV
NumPy
SciPy
imutils
You can install the required libraries using the following command:

bash
Copy code
pip install opencv-python numpy scipy imutils
Usage
Prepare the Image: Place the image you want to analyze in the /content/ directory or modify the image path accordingly.
Run the Code: Execute the Python script to detect objects, compute their dimensions, and display the output.
Check the Output: The processed image will be displayed with annotated dimensions (in inches) and midpoints.
