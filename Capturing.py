import cv2

def capture_image_from_camera(source, save_path):
    # initialize the camera
    vid_cap = cv2.VideoCapture(source)
    if not vid_cap.isOpened():
        print(f'Failed to open camera {source}')
        return

    print("Press 's' to save the image, 'q' to quit.")

    while True:
        # read one frame from live stream
        ret, frame = vid_cap.read()
        if not ret:
            print("Failed to capture image.")
            break
        
        # display the live stream
        cv2.imshow('Camera Feed', frame)

        # wait 
        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):  # press 's' to save the image
            cv2.imwrite(save_path, frame)
            print(f"Image saved to {save_path}")
        elif key == ord('q'):  # press 'q' to quit the live stream mode
            print("Quitting...")
            break

    # release camera
    vid_cap.release()
    cv2.destroyAllWindows()

def main():
    # configure camera index and set the path
    source = 0  # camera index ( default is 0 )
    save_path = '圆1.jpg'  # save path

    # capture image and save
    capture_image_from_camera(source, save_path)

if __name__ == '__main__':
    main()
