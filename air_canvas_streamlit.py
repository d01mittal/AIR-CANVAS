import cv2
import numpy as np
import mediapipe as mp
from collections import deque
import streamlit as st

# Set up Streamlit
st.set_page_config(page_title="Air Canvas with Mediapipe", page_icon=":art:", layout="wide")
st.title("Air Canvas with Mediapipe :art:")
st.write("Draw on the canvas using your hand movements. Use the sidebar to select colors and clear the canvas.")

# Developer section as buttons
st.sidebar.title("About the Developers")
if st.sidebar.button("Susanta Baidya"):
    st.sidebar.write("[LinkedIn](https://www.linkedin.com/in/susanta-baidya-03436628a/)")
if st.sidebar.button("Divyanshu Mittal"):
    st.sidebar.write("[LinkedIn](https://www.linkedin.com/in/divyanshu-mittal-4b652228a/)")
if st.sidebar.button("Manaswini Gupta"):
    st.sidebar.write("[LinkedIn](https://www.linkedin.com/in/manaswini-gupta-1a698827b/)")
if st.sidebar.button("Subhi Arjaria"):
    st.sidebar.write("[LinkedIn](https://www.linkedin.com/in/subhi-arjaria-279336237/)")

# Project section as a button
st.sidebar.title("About the Project")
if st.sidebar.button("Air Canvas Project"):
    st.sidebar.write("Air Canvas is a project that allows users to draw on a digital canvas using hand gestures captured by a webcam. It utilizes the Mediapipe library for hand detection and tracking. Users can select different colors and clear the canvas using the sidebar controls.")

# Initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Initialize the points deque for different colors
bpoints = [deque(maxlen=1024)]
gpoints = [deque(maxlen=1024)]
rpoints = [deque(maxlen=1024)]
ypoints = [deque(maxlen=1024)]

# Indexes for points
blue_index = 0
green_index = 0
red_index = 0
yellow_index = 0

# Colors in BGR format
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
color_names = ["Blue", "Green", "Red", "Yellow"]
colorIndex = 0

# Sidebar for color selection and clear button
st.sidebar.title("Controls")
colorIndex = st.sidebar.radio("Choose Color", [0, 1, 2, 3], format_func=lambda x: color_names[x])
clear_button = st.sidebar.button("Clear Canvas")
stop_button = st.sidebar.button("Stop")

# Canvas setup
paintWindow = np.zeros((471, 636, 3), dtype=np.uint8) + 255
paintWindow = cv2.rectangle(paintWindow, (40, 1), (140, 65), (0, 0, 0), 2)
paintWindow = cv2.rectangle(paintWindow, (160, 1), (255, 65), (255, 0, 0), 2)
paintWindow = cv2.rectangle(paintWindow, (275, 1), (370, 65), (0, 255, 0), 2)
paintWindow = cv2.rectangle(paintWindow, (390, 1), (485, 65), (0, 0, 255), 2)
paintWindow = cv2.rectangle(paintWindow, (505, 1), (600, 65), (0, 255, 255), 2)
cv2.putText(paintWindow, "CLEAR", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "BLUE", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "GREEN", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "RED", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "YELLOW", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)

# Start the webcam
cap = cv2.VideoCapture(0)

# Streamlit video frame placeholder
frame_placeholder = st.empty()
paint_placeholder = st.empty()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Add button rectangles to the frame
    frame = cv2.rectangle(frame, (40, 1), (140, 65), (0, 0, 0), 2)
    frame = cv2.rectangle(frame, (160, 1), (255, 65), (255, 0, 0), 2)
    frame = cv2.rectangle(frame, (275, 1), (370, 65), (0, 255, 0), 2)
    frame = cv2.rectangle(frame, (390, 1), (485, 65), (0, 0, 255), 2)
    frame = cv2.rectangle(frame, (505, 1), (600, 65), (0, 255, 255), 2)
    cv2.putText(frame, "CLEAR", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "BLUE", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "GREEN", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "RED", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "YELLOW", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)

    result = hands.process(framergb)
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                lmx = int(lm.x * 640)
                lmy = int(lm.y * 480)
                landmarks.append([lmx, lmy])

            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

        fore_finger = (landmarks[8][0], landmarks[8][1])
        center = fore_finger
        thumb = (landmarks[4][0], landmarks[4][1])
        cv2.circle(frame, center, 3, (0, 255, 0), -1)

        if thumb[1] - center[1] < 30:
            bpoints.append(deque(maxlen=512))
            blue_index += 1
            gpoints.append(deque(maxlen=512))
            green_index += 1
            rpoints.append(deque(maxlen=512))
            red_index += 1
            ypoints.append(deque(maxlen=512))
            yellow_index += 1

        elif center[1] <= 65:
            if 40 <= center[0] <= 140:  # Clear Button
                bpoints = [deque(maxlen=512)]
                gpoints = [deque(maxlen=512)]
                rpoints = [deque(maxlen=512)]
                ypoints = [deque(maxlen=512)]
                blue_index = 0
                green_index = 0
                red_index = 0
                yellow_index = 0
                paintWindow[67:, :, :] = 255
        else:
            if colorIndex == 0:
                bpoints[blue_index].appendleft(center)
            elif colorIndex == 1:
                gpoints[green_index].appendleft(center)
            elif colorIndex == 2:
                rpoints[red_index].appendleft(center)
            elif colorIndex == 3:
                ypoints[yellow_index].appendleft(center)
    else:
        bpoints.append(deque(maxlen=512))
        blue_index += 1
        gpoints.append(deque(maxlen=512))
        green_index += 1
        rpoints.append(deque(maxlen=512))
        red_index += 1
        ypoints.append(deque(maxlen=512))
        yellow_index += 1

    points = [bpoints, gpoints, rpoints, ypoints]
    for i in range(len(points)):
        for j in range(len(points[i])):
            for k in range(1, len(points[i][j])):
                if points[i][j][k - 1] is None or points[i][j][k] is None:
                    continue
                cv2.line(frame, points[i][j][k - 1], points[i][j][k], colors[i], 2)
                cv2.line(paintWindow, points[i][j][k - 1], points[i][j][k], colors[i], 2)

    frame_placeholder.image(frame, channels="BGR")
    paint_placeholder.image(paintWindow, channels="BGR")

    if clear_button:
        bpoints = [deque(maxlen=512)]
        gpoints = [deque(maxlen=512)]
        rpoints = [deque(maxlen=512)]
        ypoints = [deque(maxlen=512)]
        blue_index = 0
        green_index = 0
        red_index = 0
        yellow_index = 0
        paintWindow[67:, :, :] = 255

    if stop_button:
        break

cap.release()
cv2.destroyAllWindows()
