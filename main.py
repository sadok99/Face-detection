import cv2 #import open_cv

faceCascade = cv2.CascadeClassifier('sensor.xml') #import sensor.xml(un fichier xml par open cv pour traitement des visages et les détecter)

video_capture = cv2.VideoCapture(0) #ouvrir la caméra, 0 car usb
while True:
    ret, frame = video_capture.read() #faire des captures de video pour l'examiner
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #l'image sera gris
    faces = faceCascade.detectMultiScale(gray, 1.3, 5) #detection_visages  
    for (x, y, w, h) in faces: #boucle for dans chaque image 
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) #dessiner un rectangle vert autour de visage détecté
    cv2.putText(frame,str(len(faces)), (400,450),cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, 100)  #ecrir le nombre des visages détecté  au dessous
    cv2.imshow('Video', frame) #affichage les visages détecté avec le rectangle  et le nombre des visages détecté
    if cv2.waitKey(1) & 0xFF == ord('q'): #si on tapez 'q' , l'interface sera fermez
        break
video_capture.release() 
cv2.destroyAllWindows()