#-*- coding: utf-8 -*-
import cv2
import pyzbar.pyzbar as pyzbar

cv2.namedWindow("Camera",cv2.WINDOW_NORMAL)

camera = cv2.VideoCapture(0)
#開始設定camera的變數
while True:
    ret , frame = camera.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#讓影像變灰階
    barcodes = pyzbar.decode(gray)#尋找條碼
    for i in barcodes:#一個一個輸出出來
        barcode_data = i.data.decode("utf-8")#用utf-8輸出出來
        barcode_type = i.type
        print("掃描類型:"+barcode_type+"掃描的資料"+barcode_data)
        
    cv2.imshow("Camera",frame)#顯示視窗
    if(cv2.waitKey(5) == 27):
        break
camera.release()
cv2.destroyAllWindows()#當按下ESC鍵,視窗跳開