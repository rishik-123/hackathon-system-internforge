# import cv2
# import threading

camera_running = False

def start_camera():
    global camera_running
    camera_running = True

    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("Camera not found")
        return

    while camera_running:
        ret, frame = cam.read()
        if not ret:
            break

        cv2.imshow("Proctoring Camera", frame)

        # No blocking key
        if cv2.waitKey(1) & 0xFF == 27:  # ESC to force stop
            break

    cam.release()
    cv2.destroyAllWindows()


def start_camera_thread():
    thread = threading.Thread(target=start_camera)
    thread.daemon = True
    thread.start()


def stop_camera():
    global camera_running
    camera_running = False