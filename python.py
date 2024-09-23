import cv2

def addLog():
    img_log=cv2.imread('./image/loga.jpg')
    img_log_gray=cv2.cvtColor(img_log,cv2.COLOR_BGR2GRAY)
    #二值化
    ret,img_log_mask=cv2.threshold(img_log_gray,170,255,cv2.THRESH_BINARY)


    cv2.imshow('log',img_log)
    cv2.imshow('log_gray', img_log_gray)
    cv2.imshow('log_gray_mask',img_log_mask)
    cv2.waitKey()
    cv2.destroyAllWindows()

