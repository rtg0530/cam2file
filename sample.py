from src import cam2file as c2f
import cv2

res = c2f.capturePaper()
cv2.imshow("result", res)
cv2.waitKey()
cv2.destroyAllWindows()

path = './result.png'
c2f.handle_image(path)
