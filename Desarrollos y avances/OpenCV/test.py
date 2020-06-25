import cv2
path = 'lena.jpg'
img = cv2.imread(path, 1)
if(not img.any()):
    print('Can\'t find file path:', path)
else:
    cv2.imshow('W. Name', img)
    cv2.waitKey(4000)

