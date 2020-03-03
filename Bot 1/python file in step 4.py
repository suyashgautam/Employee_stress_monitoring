import cv2
def detect(hello12):

    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    ret, frame = cam.read()

    cv2.imwrite("C:\\Users\\<user name>\\Desktop\\project\\pics\\"+hello12+"\\"+"Desktop12_"+hello12+".jpg", frame) #Enter the user name in place of <user name> to store the files on desktop
    cam.release()