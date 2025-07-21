import cv2
import numpy as np
import requests
import subprocess
import os
import base64

# === Configuration ===
THINGSPEAK_API_KEY = "your_thingspeak_api_key"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

IMGBB_API_KEY = "your_imgbb_api_key
IMGBB_URL = "https://api.imgbb.com/1/upload"

CASCADE_PATH = "/home/snowboy/yolo/venv/lib/python3.11/site-packages/cv2/data/haarcascade_frontalface_default.xml"

# === Step 1: Capture image using libcamera ===
img_filename = "capture.jpg"
subprocess.run(["libcamera-jpeg", "-o", img_filename, "--width", "640", "--height", "480"])

# === Step 2: Read the image ===
if not os.path.exists(img_filename):
    print("No image found after capture.")
    exit()

img = cv2.imread(img_filename)
light_on = 0
human_detected = 0
wastage = 0
brightness = 0

# === Step 3: Analyze brightness ===
if img is not None:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    brightness = gray.mean()
    print(f"Average brightness: {brightness:.2f}")
    light_on = 1 if brightness > 60 else 0

    # === Step 4: Detect human (face) if light is ON ===
    if light_on:
        face_cascade = cv2.CascadeClassifier(CASCADE_PATH)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        if len(faces) > 0:
            human_detected = 1
            wastage = 0
        else:
            human_detected = 0
            wastage = 1
            
        print(f"Human detected: {bool(human_detected)}")
    else:
        print("Light is OFF. Skipping face detection.")
else:
    print("Failed to load image.")
    exit()

# === Step 5: Upload image to imgbb ===
with open(img_filename, "rb") as f:
    img_base64 = base64.b64encode(f.read())

img_payload = {
    "key": IMGBB_API_KEY,
    "image": img_base64
}

img_response = requests.post(IMGBB_URL, data=img_payload)
if img_response.status_code == 200:
    image_link = img_response.json()["data"]["url"]
    print(f"Image uploaded: {image_link}")
else:
    image_link = "Upload failed"
    print(" Failed to upload image.")

# === Step 7: Send data to ThingSpeak ===
status_msg = image_link

payload = {
    "api_key": THINGSPEAK_API_KEY,
    "field1": light_on,
    "field2": human_detected,
    "field3": wastage,
    "status": status_msg
}

response = requests.get(THINGSPEAK_URL, params=payload)
if response.status_code == 200:
    print("Data sent to ThingSpeak.")
else:
    print(f"ThingSpeak update failed: {response.status_code}")

