import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0)

MIN_DIST = 30    # fingers close
MAX_DIST = 220   # fingers far

prev_volume = 50
SMOOTHING = 0.2   # lower = smoother

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    h, w, _ = img.shape

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    volume = prev_volume
    info_text = "Show thumb & index finger"

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:

            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.append((int(lm.x * w), int(lm.y * h)))

            thumb_tip = landmarks[4]
            index_tip = landmarks[8]

            cv2.circle(img, thumb_tip, 10, (0, 255, 0), cv2.FILLED)
            cv2.circle(img, index_tip, 10, (0, 255, 0), cv2.FILLED)
            cv2.line(img, thumb_tip, index_tip, (255, 255, 255), 2)

            # Distance
            dist = np.linalg.norm(np.array(thumb_tip) - np.array(index_tip))

            # Clamp distance
            dist = np.clip(dist, MIN_DIST, MAX_DIST)

            # Map to 0–100
            target_volume = (dist - MIN_DIST) / (MAX_DIST - MIN_DIST) * 100

            #  Smooth the value
            volume = int(prev_volume * (1 - SMOOTHING) + target_volume * SMOOTHING)
            prev_volume = volume

            info_text = f"Distance: {int(dist)} px"

            mp_draw.draw_landmarks(
                img,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    cv2.rectangle(img, (20, 20), (340, 160), (0, 0, 0), -1)

    cv2.putText(img, "PINCH VOLUME CONTROL", (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    cv2.putText(img, info_text, (30, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)

    cv2.putText(img, f"Volume: {volume}%", (30, 110),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    bar_x1, bar_y1 = 30, 125
    bar_x2, bar_y2 = 300, 145
    cv2.rectangle(img, (bar_x1, bar_y1), (bar_x2, bar_y2), (255, 255, 255), 1)

    fill_w = int((volume / 100) * (bar_x2 - bar_x1))
    cv2.rectangle(img, (bar_x1, bar_y1), (bar_x1 + fill_w, bar_y2), (0, 255, 0), -1)

    cv2.imshow("AI Pinch Volume Controller", img)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
