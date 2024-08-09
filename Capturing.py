import cv2

def capture_image_from_camera(source, save_path):
    # 初始化摄像头
    vid_cap = cv2.VideoCapture(source)
    if not vid_cap.isOpened():
        print(f'Failed to open camera {source}')
        return

    print("Press 's' to save the image, 'q' to quit.")

    while True:
        # 读取一帧图像
        ret, frame = vid_cap.read()
        if not ret:
            print("Failed to capture image.")
            break
        
        # 显示实时视频流
        cv2.imshow('Camera Feed', frame)

        # 等待用户按键
        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):  # 按下 's' 键保存图像
            cv2.imwrite(save_path, frame)
            print(f"Image saved to {save_path}")
        elif key == ord('q'):  # 按下 'q' 键退出
            print("Quitting...")
            break

    # 释放摄像头
    vid_cap.release()
    cv2.destroyAllWindows()

def main():
    # 配置摄像头索引和保存路径
    source = 0  # 摄像头索引，0 通常是默认摄像头
    save_path = '圆1.jpg'  # 保存图像的路径

    # 捕捉图像并保存
    capture_image_from_camera(source, save_path)

if __name__ == '__main__':
    main()
