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
    

try:
    cur01= conexion.cursor()
    insertar="insert into usuario values(0001,'NL.2', 1)"
    cur01.execute(insertar)
    conexion.commit()
except Exception as err:
    print('Error Insertando Datos en la tabla', err)
else:
    print('datos Insertados corectamente'
          )



conexion.close()