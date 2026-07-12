class FingerDetector:
    def __init__(self):
        # Landmark IDs for fingertips
        self.tip_ids = [8, 12, 16, 20]

        # Landmark IDs for the joints just below the fingertips
        self.joint_ids = [6, 10, 14, 18]

        # Finger names
        self.finger_names = [
            "Index",
            "Middle",
            "Ring",
            "Pinky"
        ]

    def detect_fingers(self, landmarks):
        """
        Detect whether each finger is OPEN or CLOSED.

        Parameters:
            landmarks: List of MediaPipe hand landmarks.

        Returns:
            Dictionary containing finger states.
        """

        finger_states = {}

        for i in range(4):

            tip = landmarks[self.tip_ids[i]]
            joint = landmarks[self.joint_ids[i]]

            # Finger is OPEN if fingertip is above the joint
            if tip.y < joint.y:
                finger_states[self.finger_names[i]] = "OPEN"
            else:
                finger_states[self.finger_names[i]] = "CLOSED"

        return finger_states