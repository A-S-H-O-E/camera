import cv2
VCO = cv2.VideoCapture(0)
ret,frame = VCO.read()
cv2.imwrite('picture.png', frame)
VCO.release()
cv2.destroyAllWindows()