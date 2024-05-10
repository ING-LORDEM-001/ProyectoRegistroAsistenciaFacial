import cv2
import os
import numpy as np
dataPath = 'C:/xampp/htdocs/PythonProyectoBaseData/Data'#Cambia a la ruta donde hayas almacenado Data
peopleList = os.listdir(dataPath) ##lista creada dependiendo los archivos almacenados
print('Lista de personas: ', peopleList) #impresion de lista
labels = [] #etiqueta vacia
facesData = [] #etiqueta string vacia
label = 0 #etiqueta int vacia
for nameDir in peopleList:  #ciclo iniciando
    personPath = dataPath + '/' + nameDir ## almacenar en variable nombre de la capeta e imagenes una a una
    print('Leyendo las imágenes')
    for fileName in os.listdir(personPath): #ciclo secundario para almacenar imagenes por cada carpeta
        print('Rostros: ', nameDir + '/' + fileName) #mesaje sobre rostro y nombre
        labels.append(label) ##adjunta etiqueta creada
        facesData.append(cv2.imread(personPath+'/'+fileName,0)) #adjunda el los nombres de las variables person path
        #image = cv2.imread(personPath+'/'+fileName,0)
        #cv2.imshow('image',image)
        #cv2.waitKey(10)
    label = label + 1 #aumenta con el ciclo la etiqueta
#print('labels= ',labels)
#print('Número de etiquetas 0: ',np.count_nonzero(np.array(labels)==0))
#print('Número de etiquetas 1: ',np.count_nonzero(np.array(labels)==1))


# Métodos para entrenar el reconocedor
face_recognizer = cv2.face.EigenFaceRecognizer_create()
face_recognizer = cv2.face.FisherFaceRecognizer_create()
face_recognizer = cv2.face.LBPHFaceRecognizer_create() #funcion utilizada para el modelo de almacenamiento de open cv

# Entrenando el reconocedor de rostros
print("Entrenando...")
face_recognizer.train(facesData, np.array(labels)) #crea el modelo adjuntando los array de las etiuetas como rostro 1,2,3 etc


# Almacenando el modelo obtenido
#face_recognizer.write('modeloEigenFace.xml')
#face_recognizer.write('modeloFisherFace.xml')
face_recognizer.write('modeloLBPHFace.xml') #crea el nombre del modelo en la carpeta como archivo . xml
print("Modelo almacenado...")


