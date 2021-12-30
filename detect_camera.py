import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while(cap.isOpened()):
      
    while True:
          
        ret, img = cap.read()
        cv2.imshow('img', img)
        if cv2.waitKey(30) & 0xff == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
else:
    print("Alert ! Camera disconnected")

# Python program to send 
# the mail 

import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 66)

conn = smtplib.SMTP('smtp.gmail.com', 587)
  
conn.ehlo()
conn.starttls()
  
# Enter the sender's details
conn.login('mdebone@gmail.com', 
           'wO9iB1xN5iE7yV')
  
conn.sendmail('mdebone@gmail.com', 
              'debonenest19@gmail.com', 
              'Camera has been detected')
  
conn.quit()
