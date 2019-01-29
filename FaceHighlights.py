import numpy as np
import cv2
import time
import face_recognition

cap = cv2.VideoCapture(0)
count = 0
memory = 0
duration = 60
face_locations = []
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter('output2.mov',fourcc, 20.0, (1280,720))
start_time = time.time()
while(int(time.time() - start_time) < duration):
    ret, frame = cap.read()
    if ret==True:
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)#Just for faster processing
        rgb_small_frame = small_frame[:, :, ::-1]#Converting frame from BGR to RGB [OpenCV:Uses BGR & face_recognition:Uses RGB]

        face_locations = face_recognition.face_locations(rgb_small_frame)#Finding faces
        #print(face_locations)


        for (top, right, bottom, left) in face_locations:
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            a = frame[top:bottom , left:right]
            cv2.imwrite("Faces/%d.jpg"%count , a)




        

        
        out.write(frame)
        if memory%10 == 0:
            cv2.imwrite("Highlights/%d.jpg" % count, frame)
            count += 1
        memory += 1
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
