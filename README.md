# Air Canvas
Computer vision project implemented with OpenCV with Machine learning using the Mediapipe

Ever wanted to draw your imagination by just waiving your finger in air. In this post we will learn to build an Air Canvas which can draw anything on it by just motion of our hands and noticing the landmark on the hand knuckels. A very beautiful project for resume of machine learning people. We will be using the computer vision techniques of OpenCV to build this project. The preffered language is python due to its exhaustive libraries and easy to use syntax but understanding the basics it can be implemented in any OpenCV supported language.

Here Hand landmarks detection and tracking is used in order to achieve the objective.

This is a simple paint application using hand tracking with the help of the MediaPipe library in Python. The application allows you to draw on the screen using different colors by moving your hand in front of the webcam.

## Prerequisites

Make sure you have the following libraries installed:

- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)
- MediaPipe (`pip install mediapipe`)

# Algorithm

1-> Start reading the frames and convert the captured frames to HSV colour space.(Easy for colour detection)
2-> Prepare the canvas frame and put the respective ink buttons on it.
3-> Adjust the values of teh mediapipe intilization to detect one hand only.
4-> Detect teh landmarks by passing the RGB frame to the mediapipe hand detector
5-> Detect the landmarks, find the forefinger coordinates and keep storing them in the array for successive frames .(Arrays for drawing points on canvas)
6-> Finally draw the points stored in array on the frames and canvas .

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/d01mittal/hand-tracking-paint.git
Change to the project directory:

bash
Copy code
cd hand-tracking-paint
Run the script:

bash
Copy code
python paint_app.py
The application will open a webcam window, and you can start drawing on the canvas by moving your hand in front of the camera.

Features
Draw with different colors (Blue, Green, Red, Yellow).
Clear the canvas.
Real-time hand tracking using the MediaPipe library.
Usage
Move your hand in front of the webcam.
Use the index finger to draw on the canvas.
Buttons for different colors and clearing are displayed on the screen.
To select a color, move your hand to the corresponding color button.
Controls
Blue: Move hand to the blue button (185, 33).
Green: Move hand to the green button (298, 33).
Red: Move hand to the red button (420, 33).
Yellow: Move hand to the yellow button (520, 33).
Clear: Move hand to the clear button (49, 33).
Author
Divyanshu Mittal

Acknowledgments
Mediapipe library for hand tracking.
OpenCV for computer vision.
NumPy for numerical operations.
