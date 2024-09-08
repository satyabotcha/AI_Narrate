import cv2 as cv



def record_video():
    # Initialize the webcam
    webcam = cv.VideoCapture(0)

    if not webcam.isOpened():
        print("Error: Could not open webcam.")
        exit()

    # Get the actual frame width and height from the camera
    frame_width = int(webcam.get(cv.CAP_PROP_FRAME_WIDTH))
    frame_height = int(webcam.get(cv.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create VideoWriter object
    video_path = "recorded_video.mp4"
    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    out = cv.VideoWriter(video_path, fourcc, 20.0, (frame_width, frame_height))

    while True:
        # Read a frame from the webcam
        success, frame = webcam.read()

        if not success:
            print("Error: Failed to capture frame.")
            break

        # Write the frame to the video file
        out.write(frame)

        # Display the frame in a window
        cv.imshow("Webcam", frame)
        
        # Wait for 1 millisecond and check for 'q' key press
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    # Release everything
    webcam.release()
    out.release()
    cv.destroyAllWindows()

    print(f"Video saved with dimensions: {frame_width}x{frame_height}")
    return video_path

