import cv2
import time
import test_code

window_name = 'Image'
cv2.namedWindow(window_name)  # , cv2.WND_PROP_FULLSCREEN)

#path
image_path = r'C:\Users\Admin\Desktop\projects\face_segmentation\images\2201.jpg'


def read_image(path):
    # Reading an image in default mode
    image = cv2.imread(path)
    # Window name in which image is displayed
    return image


def draw_line(image, sp=(0, 0), ep=(150, 50), color=(0, 255, 0), thickness=9):
    # Start coordinate, here (0, 0)
    # represents the top left corner of image
    start_point = sp

    # End coordinate, here (250, 250)
    # represents the bottom right corner of image
    end_point = ep

    # Green color in BGR
    color = color

    # Line thickness of 9 px
    thickness = thickness

    # Using cv2.line() method
    # Draw a diagonal green line with thickness of 9 px
    image = cv2.line(image, start_point, end_point, color, thickness)

    return image


def show_image(image):
    # Displaying the image
    while True:
        cv2.imshow(window_name, image)
        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            break


def main():
    img = read_image(image_path)
    img = draw_line(img, thickness=20, ep=(100, 150), color=(0,50,0))
    show_image(img)


if __name__ == '__main__':
    main()
