#Almacenar
import cv2
import os
import imutils
from time import sleep

personName = '0001'
#dataPath = 'C:/Users/emeza/OneDrive/Documentos/Universidad/Proyects P/Data'
dataPath = 'C:/xampp/htdocs/PythonProyectoBaseData/Data'
personPath = dataPath + '/' + personName
if not os.path.exists(personPath):   #crea la carpeta 
    print('Carpeta creada: ',personPath)
    os.makedirs(personPath) #creacion de directorio
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) ##inicia la captura por video
#cap = cv2.VideoCapture('Video.mp4')
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml') #comienza la cladificacion en escala
count = 0 #variable contadora igual a 0
while True:  #inicia el ciclo de captura
    
    ret, frame = cap.read()
    if ret == False: break
    frame =  imutils.resize(frame, width=640) #redimencion de la camara
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)##escala de color de grises rgb
    auxFrame = frame.copy()
    faces = faceClassif.detectMultiScale(gray,1.3,5) #deteccion de multiple escala
    for (x,y,w,h) in faces: ##inicia el ciclo para rectangulo
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2) #dimensiones del rectangulo
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)#reajuste de la imagen
        cv2.imwrite(personPath + '/rotro_{}.jpg'.format(count),rostro)#almacena la imagen como archivo.jpg
        count = count + 1
        cv2.rectangle(frame,(10,5),(450,25),(0,0,0),-1) ##rectangulo negro
    cv2.putText(frame,'Almacenando Captuas',(10,20), 2, 0.5,(0,0,255),1,cv2.LINE_AA)#mensaje en pantalla de camara
    cv2.imshow('frame',frame)
    k =  cv2.waitKey(1)
    if k == 27 or count >= 200: ##capturas de rostro igual a 500, el ciclo no se rompe hasta cumplirse
        break

cap.release()#funcion de captura realizada
cv2.destroyAllWindows()#cerrar programa