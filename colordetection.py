import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# HSV color ranges
colors = {
    "Red": [
        (np.array([0,120,70]), np.array([10,255,255])),
        (np.array([170,120,70]), np.array([180,255,255]))
    ],
    "Green": [
        (np.array([40,70,70]), np.array([80,255,255]))
    ],
    "Blue": [
        (np.array([100,150,0]), np.array([140,255,255]))
    ],
    "Yellow": [
        (np.array([20,100,100]), np.array([35,255,255]))
    ],
    "Orange": [
        (np.array([10,100,100]), np.array([20,255,255]))
    ],
    "Purple": [
        (np.array([130,50,50]), np.array([160,255,255]))
    ],
    "Brown": [
        (np.array([10,100,20]), np.array([20,255,200]))
    ],
    "Pink": [
        (np.array([145,50,100]), np.array([170,255,255]))
    ],
    "Black": [
        (np.array([0,0,0]), np.array([180,255,50]))
    ],
}

# Drawing colors (BGR)
draw_colors = {
    "Red": (0,0,255),
    "Green": (0,255,0),
    "Blue": (255,0,0),
    "Yellow": (0,255,255),
    "Orange": (0,165,255),
    "Purple": (255,0,255),
    "Brown": (19,69,139),
    "Pink": (203,192,255),
    "Black": (0,0,0)
}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    combined_mask = np.zeros(hsv.shape[:2], dtype=np.uint8)

    for color_name, ranges in colors.items():
        mask = np.zeros(hsv.shape[:2], dtype=np.uint8)

        for lower, upper in ranges:
            mask += cv2.inRange(hsv, lower, upper)

        # Reduce noise
        mask = cv2.GaussianBlur(mask, (5,5), 0)

        combined_mask = cv2.bitwise_or(combined_mask, mask)

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)

            if area > 800:  # increased threshold to avoid noise
                (x, y), radius = cv2.minEnclosingCircle(cnt)
                center = (int(x), int(y))
                radius = int(radius)

                # Draw circle
                cv2.circle(frame, center, radius, draw_colors[color_name], 2)

                # Label
                cv2.putText(frame, color_name,
                            (center[0], center[1]-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                            draw_colors[color_name], 2)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", combined_mask)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
