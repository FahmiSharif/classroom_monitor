import time

while True:
    try:
        exec(open("/home/Desktop/classroom_monitor.py").read()) # change the file location to your own location
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(5)  # Wait 5 seconds, can change to your own setting
