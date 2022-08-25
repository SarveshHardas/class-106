# import the opencv library
import cv2

# Define a video capture object
vid = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while(True):
   
    # Capture the video frame by frame
    ret, frame = vid.read()
    grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(grey,1.1,3)

    for (x,y,w,h) in faces:
       cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
       #to crop img
       #roi_color = img[y:y+h,x:x+w]
       #cv2.imwrite("cropped.jpeg",roi_color)



    # Display the resulting frame
    cv2.imshow("Web cam", frame)
      
    # Quit Window by Spacebar Key
    if cv2.waitKey(25) == 32:
        break
  
# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()
