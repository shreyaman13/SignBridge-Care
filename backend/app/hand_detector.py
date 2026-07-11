import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Drawing utility
mp_draw = mp.solutions.drawing_utils

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()

    if not success:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    cv2.imshow("SignBridge Hand Detection", frame)

    # Exit if Q is pressed OR if the window is closed
    if (
        cv2.waitKey(1) & 0xFF == ord("q")
        or cv2.getWindowProperty("SignBridge Hand Detection", cv2.WND_PROP_VISIBLE) < 1
    ):
        break

cap.release()
cv2.destroyAllWindows()
