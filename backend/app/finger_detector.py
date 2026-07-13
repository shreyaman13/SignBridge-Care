class FingerDetector:
    """
    Detects whether each finger is OPEN or CLOSED
    using MediaPipe landmarks.
    """

    def __init__(self):

        self.tip_ids = {
            "Thumb": 4,
            "Index": 8,
            "Middle": 12,
            "Ring": 16,
            "Pinky": 20
        }

        self.joint_ids = {
            "Thumb": 3,
            "Index": 6,
            "Middle": 10,
            "Ring": 14,
            "Pinky": 18
        }

    # -----------------------------
    # THUMB
    # -----------------------------
    def detect_thumb(self, landmarks, hand_label):

        tip = landmarks[self.tip_ids["Thumb"]]
        joint = landmarks[self.joint_ids["Thumb"]]

        if hand_label == "Left":
            return "OPEN" if tip.x > joint.x else "CLOSED"

        return "OPEN" if tip.x < joint.x else "CLOSED"

    # -----------------------------
    # OTHER FINGERS
    # -----------------------------
    def detect_finger(self, landmarks, finger_name):

        tip = landmarks[self.tip_ids[finger_name]]
        joint = landmarks[self.joint_ids[finger_name]]

        if tip.y < joint.y:
            return "OPEN"

        return "CLOSED"

    # -----------------------------
    # MAIN FUNCTION
    # -----------------------------
    def detect_fingers(self, landmarks, hand_label):

        finger_states = {}

        finger_states["Thumb"] = self.detect_thumb(
            landmarks,
            hand_label
        )

        for finger in ["Index", "Middle", "Ring", "Pinky"]:

            finger_states[finger] = self.detect_finger(
                landmarks,
                finger
            )

        return finger_states