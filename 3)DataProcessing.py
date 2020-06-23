"""
The license we use in this project is the "GNU General Public License v3.0"

Juan Luis Ruiz Vanegas -> juanluisruiz971@gmail.com
Paola Gonzalez Hernandez -> paaoogh@gmail.com
Maria Lucrecia Beltz Gonzalez -> lucreciabeltz@gmail.com
"""

import mysql.connector
from mysql.connector import errorcode
import json
import glob
import datetime
import subprocess
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from datetime import datetime

PATHDBCONNECTION= '/home/luis/Documentos/UNAM/CuartoSemestre/ComputoDistribuido/dbconnection/'
today = datetime.today().strftime('%Y-%m-%d')

with open(PATHDBCONNECTION+'db.json') as json_file:
    config = json.load(json_file)

    vName = []; vMeasurementsValue = []; vMeasurementsUnit = []
    

try:
    cnx = mysql.connector.connect(**config,auth_plugin='mysql_native_password')
    cursor = cnx.cursor()
    ##Change Query if you want to change the Measurements Pollutant 
    #+-----------------------+
    #| MeasurementsPollutant |
    #+-----------------------+
    #| SO2                   |
    #| CO                    |
    #| O3                    |
    #| NO2                   |
    #| PM10                  |
    #+-----------------------+
    #
    query = ("SELECT  DISTINCT (Name) FROM Measurements  ORDER BY Name;")
    #Select the stations
    cursor.execute(query)
    for ( Name) in cursor:
        vName.append(Name)
    vNameQuery = []
    for i in range (len(vName)):
        vName.append(Name)
        vNameQuery.append(vName[i][0])

    for name in vNameQuery:
        query = ("SELECT MAX(MeasurementsValue) as MeasurementsValue FROM Measurements WHERE MeasurementsPollutant = 'PM10'AND Name = '%s'" % (name))
        cursor.execute(query)
        for (MeasurementsValue) in cursor:
            vMeasurementsValue.append(MeasurementsValue)
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()
    cnx.close()

    
# Path where data is going to be saved
PATH='/home/luis/Documentos/UNAM/CuartoSemestre/ComputoDistribuido/Measurement-of-pollutants-and-air-quality/'

fig, ax = plt.subplots()
ax.plot(vNameQuery, vMeasurementsValue)

ax.set(xlabel='Stations', ylabel='PM10 Levels',
       title='PM10 Measurement Pollutant (ppm) ')
ax.grid()
plt.xticks(rotation='vertical')
plt.grid(True)
plt.margins(0.2)
# Tweak spacing to prevent clipping of tick-labels
plt.subplots_adjust(bottom=0.3)

plt.savefig(PATH+'/Plots/'+today+'-PM10.png')
#plt.show()
