import cv2
from gesture_recognizer import GestureRecognizer

from hand_detector import HandDetector
from finger_detector import FingerDetector


# -----------------------------------
# Initialize Components
# -----------------------------------

hand_detector = HandDetector()
finger_detector = FingerDetector()
gesture_recognizer = GestureRecognizer()

cap = cv2.VideoCapture(0)

print("SignBridge Started...")
print("Press Q to Quit")


while True:

    success, frame = cap.read()
    frame = cv2.flip(frame, 1)

    if not success:
        break

    results = hand_detector.detect(frame)

    if results.multi_hand_landmarks:

        for hand_landmarks, handedness in zip(
            results.multi_hand_landmarks,
            results.multi_handedness
        ):

            # Draw landmarks
            hand_detector.draw(frame, hand_landmarks)

            # Right / Left hand
            hand_label = handedness.classification[0].label
            cv2.putText(
                frame,
                f"Detected: {hand_label}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            # Detect finger states
            finger_states = finger_detector.detect_fingers(
                hand_landmarks.landmark,
                hand_label
            )
            print(finger_states)

            gesture = gesture_recognizer.recognize(finger_states)

            print(f"Detected Gesture : {gesture}")

            cv2.putText(

                frame,

                f"Gesture : {gesture}",

                (20,80),

                cv2.FONT_HERSHEY_SIMPLEX,

                1,

                (255,0,0),

                2

            )

    cv2.imshow("SignBridge", frame)

    if (
        cv2.waitKey(1) & 0xFF == ord("q")
        or cv2.getWindowProperty("SignBridge", cv2.WND_PROP_VISIBLE) < 1
    ):
        break

cap.release()
cv2.destroyAllWindows()