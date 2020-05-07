"""
License Attribution-NonCommercial 4.0 International

"""
import mysql
import mysql.connector
from mysql.connector import errorcode
import json
import glob
import subprocess
    


if __name__ == "__main__":
    PATH='/home/luis/Documentos/UNAM/CuartoSemestre/ComputoDistribuido/dbconnection'

with open(PATH+'db.json') as json_file:
        config=json.load(json_file)
    
try:
    cnx=mysql.connector.connect(**config,auth_plugin='mysql_native_password')
    cursor=cnx.cursor()
    query=("INSERT INTO Measurements (Name,MeasurementsValue,MeasurementsUnit,MeasurementsPollutant,SourceID) VALUES(%s,%s,%s,%s,%s) ")
        
    for filename in glob.glob(PATH+"*.json"):
        print(filename)
        real_file =filename[18:]
        with open(real_file,'r') as f:
            datos=json.load(f)
        
        Name = data['Name']
        MeasurementsValue = data['MeasurementsValue']
        MeasurementsUnit = data['MeasurementsUnit']
        MeasurementsPollutant = data ["MeasurementsPollutant"]
        SourceID = data ["SourceID"]
        
        data_query = (Name,MeasurementsValue,MeasurementsUnit,MeasurementsPollutant,SourceID)
        
        cursor.execute(query,data_query)
        cnx.commit()
        output = subprocess.run(["mv",filename,PATH+"backup/"])
        
        
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
    else:
            print(err)
else:
        cnx.close()
