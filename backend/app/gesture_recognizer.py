from gesture_database import GESTURES


class GestureRecognizer:

    def __init__(self):
        self.gestures = GESTURES

    def recognize(self, finger_states):

        pattern = (

            finger_states["Thumb"],
            finger_states["Index"],
            finger_states["Middle"],
            finger_states["Ring"],
            finger_states["Pinky"]

        )

        return self.gestures.get(pattern, "UNKNOWN")