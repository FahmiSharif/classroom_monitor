import time

while True:
    try:
        exec(open("/home/snowboy/Desktop/shafi&fahmi/classroom_monitor.py").read())
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(5)  # Wait 5 seconds