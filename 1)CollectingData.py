"""
The license we use in this project is the "GNU General Public License v3.0"

Juan Luis Ruiz Vanegas -> juanluisruiz971@gmail.com
"""

import json
import requests
from datetime import datetime
import matplotlib 
import matplotlib.pyplot as plt
import numpy as np


response = requests.get("https://api.datos.gob.mx/v1/calidadAire") #Servidor

data = response.json()
N = len(data)
keys = data.keys() # ['pagination', 'results']


station = []
value = []
data.pop('pagination') #Limpiar datos
#print (data['results'])  #Datos listos para trabajar

registros = data.get('results')
#print (type(registros)) #### LIST ####
totalRegistros = len(registros) 
print (len(registros) )
######## Hasta este momento ya esta preprada ########
######## la lista con todos los registros ###########

#print (type(registros[0]) ) #dictionary
#print (registros[0].keys()) #dict_keys(['_id', 'stations'])
#print (registros[0]) 

vectorIdRregistros = []             ### Guarda en un 
for i in range(totalRegistros):          ### vector los 
    #print( registros[i],i )               ### id de los registros
    id = registros[i].get('_id')
    vectorIdRregistros.append(id)
#print (vectorIdRregistros)

vectorDatosEstaciones= []
for i in range(totalRegistros):    
    stationsDataRegistros = registros[i].get('stations')
    vectorDatosEstaciones.append (stationsDataRegistros)
#print(vectorDatosEstaciones[-1])
#print(len(vectorDatosEstaciones))

vectorIndexes = [] #[{'calculationTime': '2016-03-11T21:15:01.000Z', 'responsiblePollutant': '', 'value': '1', 'scale': 'IMECA'}]
vectorMeasurements = []  #[{'averagedOverInHours': '24', 'time': '2016-03-11T21:15:01.000Z', 'value': '0.0017125', 'unit': 'ppm', 'pollutant': 'SO2'}]
vectorLocations = [] #{'alt': '', 'lon': '-103.3557263', 'lat': '20.7201458'}
vectorSource_id = [] #GDL
vectorName = [] #Atemajac
vectorId = [] #ATM

for i in range(totalRegistros):
    indexes = (vectorDatosEstaciones[i][0]).get('indexes')
    vectorIndexes.append(indexes)
    
    measurements = (vectorDatosEstaciones[i][0]).get('measurements')
    vectorMeasurements.append(measurements)
    
    location = (vectorDatosEstaciones[i][0]).get('location')
    vectorLocations.append(location)
    
    source_id = (vectorDatosEstaciones[i][0]).get('source_id')
    vectorSource_id.append(source_id)
    
    name = (vectorDatosEstaciones[i][0]).get('name')
    vectorName.append(name)
    
    id = (vectorDatosEstaciones[i][0]).get('id')
    vectorId.append(id)




########vectorMeasurements########
#[{'averagedOverInHours': '24', 'time': '2016-03-11T21:15:01.000Z', 'value': '0.0017125', 'unit': 'ppm', 'pollutant': 'SO2'}]
##De aqui queremos el valor, la unidad y el contaminante
vectorMeasurementsValue = []
vectorMeasurementsUnit = []
vectorMeasurementsPollutant = []
for i in range(totalRegistros):
    if (vectorMeasurements[i] == []):
        vectorMeasurementsValue.append("0")
        vectorMeasurementsUnit.append("ppm")
        vectorMeasurementsPollutant.append("SO2")
    
    else:
        value = (vectorMeasurements[i][0].get('value')) 
        vectorMeasurementsValue.append(value)
        
        unit = (vectorMeasurements[i][0].get('unit')) 
        vectorMeasurementsUnit.append(unit)
        
        pollutant = (vectorMeasurements[i][0].get('pollutant')) 
        vectorMeasurementsPollutant.append(pollutant)


        
######## vectorIndexes ###########
#[{'calculationTime': '2016-03-11T21:15:01.000Z', 'responsiblePollutant': '', 'value': '1', 'scale': 'IMECA'}]
vectorIndexesTiempo = []
vectorIndexesResponsiblePollulant = []
vectorIndexesValue = []
for i in range (totalRegistros):
    time = (vectorIndexes [i][0].get('calculationTime'))
    vectorIndexesTiempo.append(time)
    
    rp = (vectorIndexes [i][0].get('responsiblePollutant'))
    vectorIndexesResponsiblePollulant.append(rp)
    
    value = (vectorIndexes [i][0].get('value'))
    vectorIndexesValue.append(value)


#print(( vectorDatosEstaciones[99][0]).keys() ) #dict_keys(['indexes', 'measurements', 'location', 'source_id', 'name', 'id'])



print(vectorName)
print(vectorMeasurementsValue)
print(vectorMeasurementsUnit)
print(vectorMeasurementsPollutant)
print(vectorSource_id)

save_file = {
    'Name': vectorName,
    'MeasurementsValue': vectorMeasurementsValue,
    'MeasurementsUnit': vectorMeasurementsUnit,
    'MeasurementsPollutant':vectorMeasurementsPollutant,
    'Source_id': vectorSource_id
}

today = datetime.today().strftime('%Y-%m-%d')
file_name = "Pollutants_measurements"+today+".json"
with open(file_name,'w') as json_file:
    json.dump(save_file,json_file)

