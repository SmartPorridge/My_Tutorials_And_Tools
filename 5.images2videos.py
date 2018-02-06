import cv2
from common import readTupleList

if __name__ == '__main__':
    trituple = readTupleList('../data/surveillance_examples/trituple.list')
    for name1, name2, _ in trituple:
        img1 = cv2.imread(name1)
        img2 = cv2.imread(name2)
        cv2.imshow('ori', img1)
        # videoWriter = cv2.VideoWriter('test.mp4', cv2.VideoWriter_fourcc(*'MJPG'), 25, img1.shape[1::-1])
        videoWriter = cv2.VideoWriter('test.avi', cv2.cv.CV_FOURCC('M','J','P','G'), 25, img1.shape[1::-1])# #img1.shape[1::-1]
        videoWriter.write(img1) #'M','I','M','1'
        videoWriter.write(img2)

        videoCapture = cv2.VideoCapture('test.avi')
        flag, img1_1 = videoCapture.read()
        flag, img2_1 = videoCapture.read()
        cv2.imshow('img1', img1_1)

        videoWriter = cv2.VideoWriter('test1.avi', cv2.cv.CV_FOURCC('M','J','P','G'), 25, img1.shape[1::-1])# #img1.shape[1::-1]
        videoWriter.write(img1_1) #'M','I','M','1'
        videoWriter.write(img2_1)

        videoCapture = cv2.VideoCapture('test1.avi')
        flag, img1_2 = videoCapture.read()
        flag, img2_2 = videoCapture.read()

        cv2.imshow('img2', img1_2)
        # cv2.imshow('img2', img2_1)
        # cv2.waitKey()
        pass

