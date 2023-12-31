import cv2


harcascade = "plate_no/haarcascade_russian_plate_number.xml"

cap = cv2.VideoCapture(0)


cap.set(3,640)
cap.set(4,480)

min_area = 500



while True:
    success,img = cap.read()
    img_roi = 1
    plates_cascade = cv2.CascadeClassifier(harcascade)
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY )

    plates = plates_cascade.detectMultiScale(img_gray,1.1,4)
    k = 0
    for(x,y,w,h) in plates:
        area = w * h

        if area > min_area:
            image = cv2.resize(img, (0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            cv2.putText(img,"number plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,255),2)
            k = 1
            img_roi= img[y: y+h,x:x+w]
            cv2.imshow("ROI",img_roi)


    cv2.imshow("Result", img)

    if cv2.waitKey(400) & k == 1:
        cv2.imwrite("op/plates/scaned_img_"+ '2' + ".jpg",img_roi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"plate saved",(150,265),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,0,255),2)
        cv2.imshow("Results",img)
        cv2.waitKey(500)
        
        
    