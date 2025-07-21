# Smart Classroom Light Monitoring System

This project is an **IoT-based smart monitoring system** that uses a Raspberry Pi with a camera module to automatically detect classroom light status and human presence. The system helps reduce energy wastage by identifying empty classrooms where lights are left on.

##  Features

-  Captures real-time classroom images using `libcamera`
-  Detects brightness level to determine if lights are ON/OFF
-  Uses Haar Cascade classifier to detect human presence (face detection)
-  Uploads images to **ImgBB** and logs data to **ThingSpeak** cloud
-  Monitors:
  - Light status
  - Human presence
  - Energy wastage
  - Image link

## Tech Stack

- **Raspberry Pi OS**
- **Python 3**
- **OpenCV** for image processing and face detection
- **libcamera-jpeg** for capturing images
- **ThingSpeak API** for real-time data logging
- **ImgBB API** for cloud image storage

## Project Structure

├── smart_monitor.py # Main Python script
├── smart_monitor_loop.py # Make the system continuous
├── capture.jpg # Captured image
└── README.md # This file

## Requirements

- Raspberry Pi with camera module
- Python 3.x
- OpenCV (`pip install opencv-python`)
- Requests (`pip install requests`)
- Internet connection for API calls

## How It Works

1. **Image Capture** – Uses `libcamera-jpeg` to capture an image.
2. **Brightness Analysis** – Converts image to grayscale and computes mean brightness.
3. **Face Detection** – If lights are ON, detects human face using Haar cascade classifier.
4. **Image Upload** – Encodes image and uploads it to ImgBB.
5. **Data Logging** – Sends light status, human presence, and wastage flag to ThingSpeak.

## API Keys

Replace the following variables in the script with your actual API keys:

```python
THINGSPEAK_API_KEY = "your_thingspeak_api_key"
IMGBB_API_KEY = "your_imgbb_api_key"
