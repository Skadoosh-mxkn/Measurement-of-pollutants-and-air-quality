![0056a0b4ea2ac7a (1)](https://user-images.githubusercontent.com/38228291/76676594-6bd05700-65c5-11ea-8fc0-7490022b1886.jpg)

# Computation distributed in pollutant measurements of the National Air Quality Information System
#### Authors
- Juan Luis Ruiz Vanegas
- Paola González Hernández
- María Lucrecia Beltz González

### How to run the program
- Before running the program make sure you have the necessary requirements, clone the repository and run the program in your terminal.

   >- git clone https://github.com/Skadoosh-mxkn/Measurement-of-pollutants-and-air-quality.git
   
   >- Access the save folder and run the program "1)CollectingData.py"
   >- Create the Database. The comands needed are in the folder "MySQL comands"
   >- Run the program "2)StoreDB.py". It will need credentials. In our case are in PATHDBCONNECTION, you will need USER, PASSWORD, HOST and DATABASE. You have to configure that requeriments on your SQLServer.
   >- Run the program "3)DataProcessing.py". You will need your credentials. You can change the Query to plot what you want.
   
- You can install the web server like this:
   >- Download the web server from http://www.lighttpd.net/
   >- Install it:
   >- ./configure build_fullstatic = yes --without-bzip2 --prefix = <install_directory>
   >- make
   >- make install 
   
### Introduction

This is a distributed computing project where the general objective is process and analyze data from a specific data source and then displaying the resulting on a web server. The main goal is to generate plottings that are comprehensible enough about the diverse pollutants that cover the atmosphere: sulfur dioxide, carbon monoxide, ozone and nitrogen dioxide. 

### Definition of the project 

In this project, we use distributed computing techinqes to work with open data on pollutant measurements and information on air quality. The API contains a list of geographic information retrieved hourly by strategical stations where pollutant statistics are found. The API is created and openly shared by INECC (*Instituto Nacional de Ecología y Cambio Climático*). We also use a web server to show the results of the analysis of this data using more techniques.

### Overall objective

The objective of this project is to collect data in real time from the Instituto Nacional de Ecología y Cambio Climático to model air quality and the amount of pollutants from different stations in the country, we want these data to be exposed to interested people through a web server, that is, use distributed computing in our data collection model.

### General system architecture
The architecture of our system is structured in two main elements:

 - The program **"1)CollectingData.py"**:
>> This program written on Python 3.7.5 is where we work with our data source obtained from INECC (Instituto Nacional de Ecología y Cambio Climático). In general, what we do in this code is to take the data records of pollutant measurements obtained from the geographic information stations and make an analysis of these data to save them in directories that we will show on the server. This program creates a json file with the data processed.
 - The program **"2)StoreDB.py"**:
>> In this program, we open the json file, connect with the SQL Server and executing queries to store the data on a SQL table.
- The program **"3)DataProcessing.py"**:
>> Here we make queries to the SQL Server over our table in order to get the information necessary to create plottings. You can change the path where datum is going to be saved.
- Plots folder
>>Here is an example of the plots you can create.

- Plotting folder
>> Here are some plots explaining more information about the project.

- Diagrams folder
>>In case any questions about the structure of the system, there are five images that show the data flux process, a latency diagram, logical connections and classes information used. 
- Mezzanine folder
>>The original idea was to work with Mezzanine Django framework. Installation and basic information about is can be found within this folder.

- The server **Lighttpd**:
>> The Lighttpd server is a secure web server, fast and adhering to certain standards, it is optimized for environments where speed is very important and, therefore, consumes less CPU and RAM than other services. The process followed with this server was to download it to the personal computer and configure it, then compile and execute it. The next thing was to start the server on port 3000 and activate the option to view files and upload the data directories retrieved from the analysis of our data source to the server.

(Connection test)
![Test Server](https://user-images.githubusercontent.com/38228291/76675975-6f60df80-65bf-11ea-846b-b1f3e46452c8.png)

### Outcome and Conclusions

The result we obtained by filtering the relevant data for our project and processing it to work with it were: locations of the stations, name of the cities, amount of pollutants, measurement dates and the pollutants values relative to a reference frame. This information is represented on the IMECA scale and the following image is an impression of the analysis results.


### Bibliography
- [Api of the DB](https://datos.gob.mx/busca/dataset/mediciones-de-contaminantes-del-sistema-nacional-de-informacion-de-la-calidad-del-aire)
- [Webserver](http://www.lighttpd.net/)
- [Logo](https://www.redbubble.com/es/shop/yin+yang+del+drag%C3%B3n+stickers)
- [Pip package](https://pypi.org/project/pip/)

### License

 **"GNU General Public License v3.0"** was used in this project. More information about sharing and usage of this project within the file.

### Contact information

For further contacting and more questions, the following contacts are provided:

- Juan Luis Ruiz Vanegas ----> juanluisruiz971@gmail.com
- Paola González Hernández ----> paaoogh@gmail.com
- María Lucrecia Beltz González ----> lucreciabeltz@gmail.com
