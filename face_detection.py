import cv2
import os


MODEL_PATH = "face_detection_yunet_2023mar.onnx"
WINDOW_NAME = "Face Detection"


def create_face_detector():
    detector = cv2.FaceDetectorYN.create(
        MODEL_PATH,
        "",
        (320, 320),
        0.9,
        0.3,
        5000
    )

    return detector


def detect_faces(frame, detector):
    height, width, _ = frame.shape

    detector.setInputSize((width, height))

    _, faces = detector.detect(frame)

    if faces is not None:
        for face in faces:
            x, y, w, h = face[:4]

            cv2.rectangle(
                frame,
                (int(x), int(y)),
                (int(x + w), int(y + h)),
                (255, 0, 0),
                2
            )

    return frame


def run_webcam(detector):
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Could not open webcam.")
        return

    while True:
        ret, frame = camera.read()

        if not ret:
            print("Could not read from webcam.")
            break

        frame = detect_faces(frame, detector)

        cv2.imshow(WINDOW_NAME, frame)

        if cv2.waitKey(1) == ord("q"):
            break

    camera.release()


def run_video(video_path, detector):
    if not os.path.exists(video_path):
        print("Video file not found.")
        return

    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        print("Could not open video.")
        return

    while True:
        ret, frame = video.read()

        if not ret:
            break

        frame = detect_faces(frame, detector)

        cv2.imshow(WINDOW_NAME, frame)

        if cv2.waitKey(1) == ord("n"):
            break

    video.release()


def main():
    detector = create_face_detector()

    print("Choose input:")
    print("1 - Webcam")
    print("2 - Video file")

    choice = input("Enter your choice: ")

    if choice == "1":
        run_webcam(detector)

    elif choice == "2":
        video_path = input("Enter video path: ")
        run_video(video_path, detector)

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()

cv2.destroyAllWindows()