# Hand Tracking Paint Application

This is a simple paint application using hand tracking with the help of the MediaPipe library in Python. The application allows you to draw on the screen using different colors by moving your hand in front of the webcam.

## Prerequisites

Make sure you have the following libraries installed:

- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)
- MediaPipe (`pip install mediapipe`)

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
