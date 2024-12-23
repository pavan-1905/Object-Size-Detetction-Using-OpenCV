# **Object Size Detection with OpenCV**

**This project demonstrates how to use OpenCV for image processing, including object dimension detection and display. The primary functionality includes detecting contours in an image, calculating the bounding box for each object, and determining its dimensions (in inches) based on a pixel-per-metric conversion. Additionally, the program resizes the image, detects edges, and displays the object dimensions along with the image's size.**

# **Features**
1. **Image Resize: Resizes the input image to a reduced size for faster processing.**
2. **Contour Detection: Identifies the contours of objects within the image.**
3. **Bounding Box: Computes and draws the rotated bounding box for each object.**
4. **Midpoints and Connecting Lines: Marks the midpoints of the bounding box edges and draws connecting lines.**
5. **Euclidean Distance: Calculates the Euclidean distance between points in the bounding box to determine the dimensions.**
6. **Pixel to Metric Conversion: Converts the dimensions of the detected objects from pixels to real-world units (inches) using a given reference.**
7. **Text Annotations: Annotates the image with the calculated dimensions and image size.
Requirements.**
8. **To run the project, you need the following Python libraries:**

    **Python 3.x**
    **OpenCV**
    **NumPy**
    **SciPy**
    **imutils**
You can install the required libraries using the following command:

  1. **bash**
  2. **Copy code**
  **pip install opencv-python numpy scipy imutils**

Steps:  
1. **Prepare the Image: Place the image you want to analyze in the /content/ directory or modify the image path accordingly.**
2. **Run the Code: Execute the Python script to detect objects, compute their dimensions, and display the output.**
3. **Check the Output: The processed image will be displayed with annotated dimensions (in inches) and midpoints.**

A similar alternative is an "Open in Colab" badge, which allows people with a google account to open launch one of the public jupyter notebooks here directly on Google's servers. What I'd like is a badge that like Open In Colab next to the current Binder badge.

# **The Sample Code is in this following Colab Notebook:**
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1BZ5rl3nH9QXNktSoivqfz6AIhDKTXWgP#scrollTo=MOLoWIGg5EgF)

# **Sample Input Image**
![image](https://github.com/pavan-1905/Object-Size-Detetction-Using-OpenCV/blob/main/Image1.jpg)


# **Output**
**The output image will display:**

1. **The detected objects with rotated bounding boxes drawn around them.**
2. **Midpoints marked for each side of the bounding box.**
3. **Connecting lines between the midpoints.**
4. **Dimensions (in inches) annotated on the image.**
5. **Image size (width and height in pixels) displayed in the bottom-left corner.**
   
# **Sample Output Image**
![image](https://github.com/pavan-1905/Object-Size-Detetction-Using-OpenCV/blob/main/Output.png)

# **Contributing**
**Feel free to fork this repository, make changes, and submit pull requests. Any contributions to improve the accuracy or functionality of the project are welcome.**


 
