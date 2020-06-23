"""
The license we use in this project is the "GNU General Public License v3.0"

Juan Luis Ruiz Vanegas -> juanluisruiz971@gmail.com
Paola Gonzalez Hernandez -> paaoogh@gmail.com
Maria Lucrecia Beltz Gonzalez -> lucreciabeltz@gmail.com
"""
#Further libraries might be needed
import mysql
import mysql.connector
from mysql.connector import errorcode
import json
import glob
import subprocess

#Insertion query function with connector and cursor.
def insertar (data_query):
    try:
        cnx=mysql.connector.connect(**config,auth_plugin='mysql_native_password')
        cursor=cnx.cursor()
        query=("INSERT INTO Measurements (Name,MeasurementsValue,MeasurementsUnit,MeasurementsPollutant,Source_id) VALUES(%s,%s,%s,%s,%s) ")

        cursor.execute(query,data_query)
        cnx.commit()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
        else:
                print(err)
                
    else:
        cnx.close()



if __name__ == "__main__":
    PATHDBCONNECTION= '/home/luis/Documentos/UNAM/CuartoSemestre/ComputoDistribuido/dbconnection/'
    PATHJSONFILE='/home/luis/Documentos/UNAM/CuartoSemestre/ComputoDistribuido/Measurement-of-pollutants-and-air-quality/'

    with open(PATHDBCONNECTION+'db.json') as json_file:
            config=json.load(json_file)
                
    for filename in glob.glob(PATHJSONFILE+"*.json"):
        print("a",filename)

        real_file =filename[103:]
        with open(real_file,'r') as f:
            data=json.load(f)
        
        Name = data.get('Name')
        MeasurementsValue = data.get('MeasurementsValue')
        MeasurementsUnit = data.get('MeasurementsUnit')
        MeasurementsPollutant = data.get("MeasurementsPollutant")
        Source_id = data.get("Source_id")
        for i in range (len(Name)):
            data_query = (Name[i],MeasurementsValue[i],MeasurementsUnit[i],MeasurementsPollutant[i],Source_id[i])
            insertar(data_query)
                
    #output = subprocess.run(["mv",filename,PATH+"Backup/"])
    
        
        
