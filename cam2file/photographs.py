import core
import cv2

img = core.capturePaper()
cv2.imwrite('C:/grayImage.png',img)

def handle_image():
    img = core.capturePaper()
    cv2.imwrite('C:/grayImage.png',img)