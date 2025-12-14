import cv2
import mediapipe as mp
import pyautogui
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0
prev_x, prev_y = 0, 0
prev_scroll_y = 0
smoothing_factor = 0.5
# Sensitivity adjustments
click_threshold = 20
move_threshold = 50
scroll_threshold = 30

def is_palm_open(landmarks):
    # Check if all fingers are extended (basic palm detection)
    # Thumb extended if tip is to the left of base (for right hand)
    thumb_extended = landmarks[4].x < landmarks[3].x
    index_extended = landmarks[8].y < landmarks[6].y
    middle_extended = landmarks[12].y < landmarks[10].y
    ring_extended = landmarks[16].y < landmarks[14].y
    pinky_extended = landmarks[20].y < landmarks[18].y
    return thumb_extended and index_extended and middle_extended and ring_extended and pinky_extended
while True:
    _, frame = cap.read()
    if not _:
        continue
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        # Multi-hand support: first hand for mouse, second for additional actions
        mouse_hand = hands[0] if len(hands) > 0 else None
        action_hand = hands[1] if len(hands) > 1 else None

        if mouse_hand:
            drawing_utils.draw_landmarks(frame, mouse_hand)
            landmarks = mouse_hand.landmark
            index_x = index_y = thumb_x = thumb_y = middle_y = None
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                if id == 4:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                if id == 12:
                    middle_y = screen_height/frame_height*y

            if index_x is not None and thumb_x is not None:
                dist = abs(index_y - thumb_y)
                palm_open = is_palm_open(landmarks)
                if palm_open and dist > move_threshold:
                    # Better palm detection: only move if palm is open
                    smoothed_x = prev_x + smoothing_factor * (index_x - prev_x)
                    smoothed_y = prev_y + smoothing_factor * (index_y - prev_y)
                    pyautogui.moveTo(smoothed_x, smoothed_y)
                    prev_x, prev_y = smoothed_x, smoothed_y
                elif dist < click_threshold:
                    pyautogui.click()
                    pyautogui.sleep(0.5)
                elif middle_y and abs(thumb_y - middle_y) < click_threshold:
                    # Right-click: thumb and middle finger close
                    pyautogui.rightClick()
                    pyautogui.sleep(0.5)

        if action_hand:
            # Scroll functionality with second hand
            drawing_utils.draw_landmarks(frame, action_hand, landmark_drawing_spec=drawing_utils.DrawingSpec(color=(255,0,0)))
            landmarks = action_hand.landmark
            index_y = middle_y = None
            for id, landmark in enumerate(landmarks):
                y = int(landmark.y*frame_height)
                if id == 8:
                    index_y = screen_height/frame_height*y
                if id == 12:
                    middle_y = screen_height/frame_height*y
            if index_y and middle_y and abs(index_y - middle_y) < scroll_threshold:
                # Two fingers close for scroll mode
                current_scroll_y = (index_y + middle_y) / 2
                if prev_scroll_y != 0:
                    scroll_delta = prev_scroll_y - current_scroll_y
                    if abs(scroll_delta) > 5:  # Threshold to avoid jitter
                        pyautogui.scroll(int(scroll_delta / 10))  # Scroll based on movement
                prev_scroll_y = current_scroll_y
    cv2.imshow('Virtual Mouse', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
