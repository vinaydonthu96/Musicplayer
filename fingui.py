import time  
import cv2
import label_image
import os,random
import subprocess
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'



def musics():
    size = 4
# We load the xml file
    classifier = cv2.CascadeClassifier('E://trial 1//original//haarcascade_frontalface_alt.xml')
                                      
    global text
    webcam = cv2.VideoCapture(0)  # Using default WebCam connected to the PC.
    now = time.time()###For calculate seconds of video
    future = now + 20  ####here is second of time which taken by emotion recognition system ,you can change it was 60 before
    while True:
        (rval, im) = webcam.read()
        im = cv2.flip(im, 1, 0)  # Flip to act as a mirror
    # Resize the image to speed up detection
        mini = cv2.resize(im, (int(im.shape[1] / size), int(im.shape[0] / size)))
    # detect MultiScale / faces
        faces = classifier.detectMultiScale(mini)
    # Draw rectangles around each face
        for f in faces:
            (x, y, w, h) = [v * size for v in f]  # Scale the shapesize backup
            sub_face = im[y:y + h, x:x + w]
            FaceFileName = "test.jpg"  # Saving the current image from the webcam for testing.
            cv2.imwrite(FaceFileName, sub_face)
            text = label_image.main(FaceFileName)  # Getting the Result from the label_image file, i.e., Classification Result.
            text = text.title()  # Title Case looks Stunning.
            font = cv2.FONT_HERSHEY_TRIPLEX

            if text == 'Happy':
                cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                cv2.putText(im, text, (x + h, y), font, 1, (0, 25,255), 2)

            if text == 'Smile':
                cv2.rectangle(im, (x, y), (x + w, y + h), (0,260,0), 7)
                cv2.putText(im, text, (x + h, y), font, 1, (0,260,0), 2)

            if text == 'Surprise':
                cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 255), 7)
                cv2.putText(im, text, (x + h, y), font, 1, (0, 255, 255), 2)

            if text == 'Neutral':
                cv2.rectangle(im, (x, y), (x + w, y + h), (0,191,255), 7)
                cv2.putText(im, text, (x + h, y), font, 1, (0,191,255), 2)

    # Show the image/
        cv2.imshow('Music player with Emotion recognition', im)
        key = cv2.waitKey(30)& 0xff
        if time.time() > future:##after 20second music will play
            try:
                cv2.destroyAllWindows()
                mp = 'C:/Program Files (x86)/Windows Media Player/wmplayer.exe'
                if text == 'Happy':
                    randomfile = random.choice(os.listdir("E:/prasad project/songs/angry/"))
                    print('You are angry !!!! please calm down:) ,I am will play song for you :' + randomfile)
                    file = ('E:/prasad project/songs/angry/' + randomfile)
                    subprocess.call([mp, file])

                if text == 'Surprise':
                    randomfile = random.choice(os.listdir("E:/prasad project/songs/happy/"))
                    print('You are smiling :) ,I am playing special song for you: ' + randomfile)
                    file = ('E:/prasad project/songs/happy/' + randomfile)
                    subprocess.call([mp, file])

                if text == 'Neutral':
                    randomfile = random.choice(os.listdir("E:/prasad project/songs/calm/"))
                    print('You have fear of something ,I am playing song for you: ' + randomfile)
                    file = ('E:/prasad project/songs/calm/' + randomfile)
                    subprocess.call([mp, file])

                if text == 'Sad':
                    randomfile = random.choice(os.listdir("E:/prasad project/songs/sad/"))
                    print('You are sad,dont worry:) ,I am playing song for you: ' + randomfile)
                    file = ('E:/prasad project/songs/sad/' + randomfile)
                    subprocess.call([mp, file])
                break

            except :
                print('Please stay focus in Camera frame atleast 15 seconds & run again this program:)')
                break

        if key == 27:  # The Esc key
            break


def look():
    import cv2
    import numpy as np
    import pyautogui as pag
    import psutil

    eye_cascade = cv2.CascadeClassifier('E://trial 1//original//haarcascade_eye.xml')
    face_cascade = cv2.CascadeClassifier('E://trial 1//original//haarcascade_frontalface_alt.xml')
    previousEyes = currentEyes = "0"
    runningState = False

    while True:
        try:
            processes = [psutil.Process(i).name for i in psutil.pids()]
            if "vlc.exe" in str(processes):
                runningState = True
            if runningState:
                cap = cv2.VideoCapture(0)
        except:
            pass
        while runningState:
            previousEyes = currentEyes
            _, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            if len(faces) < 1:
                currentEyes = "0"
            for (x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex,ey,ew,eh) in eyes:
                    if ey > 40 and ey < 100:
                        currentEyes = "1"
                        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            if previousEyes + currentEyes == "01":
                pag.hotkey('Shift', 'r') #resume
            if previousEyes + currentEyes == "10":
                pag.hotkey('Shift', 'p') #pause
            try:
                processes = [psutil.Process(i).name() for i in psutil.pids()]
                cv2.namedWindow('FACE CAMERA',cv2.WINDOW_NORMAL)
                cv2.imshow('FACE CAMERA',frame)
                k = cv2.waitKey(10)
                if "vlc.exe" not in str(processes):
                    pag.alert(text='VIDEO PLAYER IS CLOSED', title='VIDEO PLAYER', button='OK')
                    runningState = False
                    cap.release()
                    cv2.destroyAllWindows()
                    break
            except:
                pass


from tkinter import *
from tkinter import messagebox

MGui = Tk()
MGui.title("SMART MEDIA PLAYER")
MGui.geometry('450x450')

messagebox.showinfo("ABOUT", "CREATED BY SAVVY TECH PRVT LTD")

widget = Button(text='SELECT YOUR OPTION', padx=10, pady=10)
widget.pack(padx=20, pady=20)
widget.config(bg='dark green', fg='white')
widget.config(font=('trajan', 20, 'italic'))



mbutton = Button(text = "AUDIO PLAYER", padx=50,pady=10,fg="red",font=('berlin', 20, 'italic'),command = musics).pack()
mbutton = Button(text = "VIDEO PLAYER", padx=50,pady=10, fg="blue", font=('helvetica', 20, 'italic'),command = look).pack()


MGui.mainloop()
