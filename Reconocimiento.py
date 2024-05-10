#sistema de reconocimiento Facial
'''
/* Proyecto Modular Codigo   Sistema de Registro de Asistencia facial
 *  Equipo  7°A T/M
 *  Jorge Enrique Meza Gutierrez
 *  Josue Luna Salinas
 *  Alfonso Ramirez Alvarez

'''
#libreias
import cv2
import os
#import mediapipe as mp
#import serial
import time
from time import sleep

import mysql.connector

try:
    conexion=mysql.connector.connect(host='localhost',
                                     user='root',
                                     passwd='',
                                     database='base_prueba')
except Exception as err:
    print('Error Conectando a la base)')
else:
    print('Conectado a MYSQL')




#ser = serial.Serial('COM3', 9600, timeout=1) ##comucicacion serial Arduino
time.sleep(2)
limt= "100" ## variable utilizada para contar

dataPath = 'C:/xampp/htdocs/PythonProyectoBaseData/Data' #Cambia a la ruta donde hayas almacenado Data
imagePaths = os.listdir(dataPath) ##funcion para pasar datos de la data
print('imagePaths=',imagePaths)
#face_recognizer = cv2.face.EigenFaceRecognizer_create()
#face_recognizer = cv2.face.FisherFaceRecognizer_create()
face_recognizer = cv2.face.LBPHFaceRecognizer_create() # funcion para leer datos
# Leyendo el modelo
#face_recognizer.read('modeloEigenFace.xml')
#face_recognizer.read('modeloFisherFace.xml')
face_recognizer.read('modeloLBPHFace.xml')  ##modelo de captura facial
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
#cap = cv2.VideoCapture('Video.mp4')
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')#lee y abre el modelo creado anteriormente en la carpeta
while True: #ciclo while
    ret,frame = cap.read()  ###captura con camara
    if ret == False: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #ajuste de colores escala de grises
    auxFrame = gray.copy()
    faces = faceClassif.detectMultiScale(gray,1.3,5)  #nuevo ajuste de colores vividos
    for (x,y,w,h) in faces: #ciclo for para comenzar a escanear
        rostro = auxFrame[y:y+h,x:x+w]  #almacenar datos en variables
        rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC) #detector cv2
        result = face_recognizer.predict(rostro) ##almacenamineto de la varibale rostro
        cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,0,0),1,cv2.LINE_AA)  ###imprimir resultado en pantalla
        '''
        # EigenFaces
        if result[1] < 5700:
            cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        else:
            cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
        
        # FisherFace
        if result[1] < 500:
            cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        else:
            cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
          '''
         #LBPHFace
        if result[1] < 70: ###evaluando valores
            cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,0,255),1,cv2.LINE_AA) #resutado en pantalla
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
            cadena=imagePaths[result[0]] #almacenar resultado en una variable
            #print(result)
            s = ''.join(str(x) for x in cadena) #convertir datos a tipo string
            #print(imagePaths[result[0]])
            chars=s[3] #almacenar un solo dato
            print(s)
            if chars != limt: ## evaluar condicion
            # ser.write(chars.encode('ascii')) ##trasnferir datos al arduino
             limt=chars ##almacenar datos0
             #print(chars)
             print(limt)
             aumento = 1
             cur01= conexion.cursor()
             #insertar="insert into usuario values(3, 'Nl.2' , 1)"
             consulta = "UPDATE usuario SET Asistencia = Asistencia + %s WHERE cod_estudiante = %s "
             #cur01.execute(consulta)
             cur01.execute(consulta,(aumento, s ))
             conexion.commit()
             #print('datos Insertados corectamente')
        else: ###evaluar condicion secundaria
            
            cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,0),1,cv2.LINE_AA) ##imprimir resultado en pantalla desconocido si no hay coincidencias
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2) #rectangulo alrededor del rostro en rojo
      
    cv2.imshow('frame',frame) ##imagen en pantalla
    k = cv2.waitKey(1) ##almacenar datos
    if k == 27: ##evaluando condicion para salir con esc
        break
cap.release() #cirra la camara
cv2.destroyAllWindows()##cirra el programa
#set.close() ##cirra el serial arduino
conexion.close()