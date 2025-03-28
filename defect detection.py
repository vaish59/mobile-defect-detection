import cv2
import numpy as np
import os

def detect_defects(image_path, output_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not read image {image_path}")
        return

    # Convert to different color spaces
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ### **1. Detect Scratches (Crashes) using Edge Detection**
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if 500 < area < 5000:  # Ignore small/noise contours
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)  # Green for scratches
            cv2.putText(image, "Scratch", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    ### **2. Detect Stains (Red-like regions)**
    lower_stain = np.array([0, 50, 50])     # Lower bound for red
    upper_stain = np.array([10, 255, 255])  # Upper bound for red
    mask_stain = cv2.inRange(hsv, lower_stain, upper_stain)

    contours_stain, _ = cv2.findContours(mask_stain, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours_stain:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)  # Red for stains
        cv2.putText(image, "Stain", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    ### **3. Detect Oil (Blue-like regions)**
    lower_oil = np.array([90, 50, 50])     # Lower bound for blue
    upper_oil = np.array([130, 255, 255])  # Upper bound for blue
    mask_oil = cv2.inRange(hsv, lower_oil, upper_oil)

    contours_oil, _ = cv2.findContours(mask_oil, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours_oil:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Blue for oil
        cv2.putText(image, "Oil", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Save and show the processed image
    cv2.imwrite(output_path, image)
    print(f"Processed: {image_path} → Saved: {output_path}")

    # Open the image using default viewer (Works on Windows)
    os.startfile(output_path)

# Set paths for input and output images
image_path = r"C:\Users\Vaishnavi\Desktop\Istreet CV project\dataset\oil\Oil_0015.jpg"
output_path = r"C:\Users\Vaishnavi\Desktop\Istreet CV project\output\Processed_Oil_0015.jpg"

# Run detection
detect_defects(image_path, output_path)






