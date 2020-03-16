![0056a0b4ea2ac7a (1)](https://user-images.githubusercontent.com/38228291/76676594-6bd05700-65c5-11ea-8fc0-7490022b1886.jpg)

# Computation distributed in pollutant measurements of the National Air Quality Information System

### How to run the program
- Before running the program make sure you have the necessary requirements, clone the repository and run the program in your terminal.

   >- git clone https://github.com/Skadoosh-mxkn/Measurement-of-pollutants-and-air-quality.git
   
   >- access the save folder and run the program "testJson.py"
   

### Definition of the project

In this project, we use distributed computing to work with open data on pollutant measurements and information on air quality. The API contains a list of geographic information stations where pollutant statistics are found. These data are updated every hour. The API is created and openly shared by INECC, which is the national institute for ecology and climate change. We also use a web server to show the result of the analysis of this data using distributed computing.

### Overall objective

The objective of this project is to collect data in real time from the National Institute of Ecology and Climate Change to model air quality and the amount of pollutants from different stations in the country, we want these data to be exposed to interested people through a web server, that is, use distributed computing in our data collection model.

### General system architecture
The architecture of our system is structured in two main elements:

 - The program **"testJson.py"**:
>> This program written in the python language is where we work with our data source obtained from INECC (National Institute of Ecology and Climate Change). In general, what we do in this code is to take the data records of pollutant measurements obtained from the geographic information stations and make an analysis of these data to save them in directories that we will show on the server.
- The server **Lighttpd**:
>> The Lighttpd server is a secure web server, fast and adhering to certain standards, It is optimized for environments where speed is very important and therefore consumes less CPU and RAM than other servers. The way we work with this server was to download it to our computer and configure it, then we compile and execute it. The next thing was to start the server on port 3000 and activate the option to view files to upload the data directiorios obtained from the analysis of our data source to the server.

(Connection test)
![Test Server](https://user-images.githubusercontent.com/38228291/76675975-6f60df80-65bf-11ea-846b-b1f3e46452c8.png)

### Outcome of data analysis

The result we obtained by filtering the relevant data for our project and processing it to work with it were; The locations of the stations, the name of the city, the amount of pollutants, date of measurement and the value of pollutants on the scale. This information is represented on the IMECA scale and the following image is an impression of the analysis results.
![Test Data Acquisition](https://user-images.githubusercontent.com/38228291/76675986-88699080-65bf-11ea-883e-5aaca9077fc5.png)


### Bibliography
- [Api of the DB](https://datos.gob.mx/busca/dataset/mediciones-de-contaminantes-del-sistema-nacional-de-informacion-de-la-calidad-del-aire)
- [Webserver](http://www.lighttpd.net/)
- [Logo](https://www.redbubble.com/es/shop/yin+yang+del+drag%C3%B3n+stickers)
- [Pip package](https://pypi.org/project/pip/)
