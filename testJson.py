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
#print (vectorIndexes[-1])

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
#print (vectorIndexesValue)

#print(( vectorDatosEstaciones[99][0]).keys() ) #dict_keys(['indexes', 'measurements', 'location', 'source_id', 'name', 'id'])


"""Convertir el tiempo"""
#2016-03-11T21:15:01.000Z
timeVector = []
for item in vectorIndexesTiempo:
    print (item)
    timeVector.append( datetime.strptime(item, '%Y-%m-%dT%H:%M:%S.%fZ') )
    
print(timeVector)

"""
for item in data:
	#2020-03-05T19:02:00Z
	if item['energy'] == "0.1-0.8nm":
		myTime = datetime.datetime.strptime(item['time_tag'], '%Y-%m-%dT%H:%M:%SZ' ) #Parsing time

		flux= float(item["flux"])
		
		timeVector.append(myTime)
		fluxVector.append(flux)
		
		print (myTime,flux)


fig,ax = plt.subplots()
ax.plot (timeVector,fluxVector)

ax.set(xlabel = 'Time', ylabel = 'Flix (W m^2)', title = "X ray flux 1 day")
ax.grid()
plt.ylim(1e-9,1e-2)
plt.yscale("log")


fig.savefig("xRayFlux.png")
#plt.show()
	

"""
#information = data[0]

#print (information["time_tag"])



#xray_flux = json.load(response.txt)
#print (xray_flux["time_tag"])
