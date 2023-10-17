# NASA EARTHDATA.

## National Snow and Ice Data Center Distributed Active Archive Center (NSIDC DAAC).

## Funcionalidad para descarga de datos mediante el uso de EOS-CMR API.

## 1. ABREVIATURAS.



## 2. OBJETIVO.

Este proyecto tiene como objetivo disponibilizar una funcionalidad que facilite la consulta y descarga de datos correspondientes **NASA National Snow and Ice Data Center Distributed Active Archive Center (NSIDC DAAC)** mediante linea de comando y utilizando la funcionalidad disponible de consulta via API.
Si bien originalmente esta funcionalidad fue pensada para consulta de datos correspondientes a la mision **Soil Moisture Active Passive Data (SMAP)** la misma puede ser utilizada para otras misiones que permiten la consulta y descarga de datos via API.

## 3. ALCANCE Y LIMITACIONES.

Tal cual se indica en https://nsidc.org/data/user-resources/help-center/programmatic-data-access-guide#anchor-0 es importante destacar que todos los datos de NSIDC DAAC pueden ser accedidos en forma directa desde el sistema de archivos HTTPS utilizando wget o curl.

Sumado a lo anterior se tiene la posibilidad de consultar una gran seleccion de datos mediante API, lo cual ofrece la posibilidad de ordenar datos utilizando filtros temporales y espaciales específicos, así como subconjuntos, reformatear y reproyectar conjuntos de datos seleccionados.
 Es importante aclarar que si bien se puede acceder a una gran selección de datos NSIDC mediante la API (por ejemplo, AMSR-E/AMSR2, ICESat-2/ICESat, MODIS, SMAP, VIIRS), no se puede acceder a todos los datos DAAC de NSIDC de esta manera. Esto ultimo representa una **limitacion** en el uso de esta funcionalidad para consulta y descarga de datos, lo cual debe ser tenido en consideracion en caso de querer consultar datos no disponibles via API.

## 4. DOCUMENTACION DE REFERENCIA.

### 4.1 NSIDC.

* NSIDC Home https://nsidc.org/home

* NSIDC Data https://nsidc.org/data

* Explore web services, interactive tutorials, and other tools to access and work with NSIDC data https://nsidc.org/data/user-resources/data-tools

* Programmatic Data Access Guide https://nsidc.org/data/user-resources/help-center/programmatic-data-access-guide

* NSIDC DAAC's data access and service API https://nsidc.org/data/user-resources/help-center/programmatic-data-access-guide#anchor-3

* NSIDC-Data-Access-Notebook https://github.com/nsidc/NSIDC-Data-Access-Notebook

* Table of Key-Value-Pair (KVP) Operands for Subsetting, Reformatting, and Reprojection Services https://nsidc.org/data/user-resources/help-center/table-key-value-pair-kvp-operands-subsetting-reformatting-and-reprojection-services

* Earthdata CRM Search - API Documentation https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html#_ga=2.224475802.1037008902.1697547140-1448504569.1697547140


### 4.2 SMAP (Soil Moisture Active Passive)

* Soil Moisture Active Passive Data (SMAP) https://nsidc.org/data/smap

* What data subsetting, reformatting, and reprojection services are available for SMAP data? https://nsidc.org/data/user-resources/help-center/what-data-subsetting-reformatting-and-reprojection-services-are-available-smap-data

* SMAP Enhanced L3 Radiometer Global and Polar Grid Daily 9 km EASE-Grid Soil Moisture, Version 5 (SPL3SMP_E) https://nsidc.org/data/spl3smp_e/versions/5

* SMAP Enhanced L3 Radiometer Global and Polar Grid Daily 9 km EASE-Grid Soil Moisture V005 https://cmr.earthdata.nasa.gov/search/concepts/C2136471727-NSIDC_ECS.html

* Interfaz grafica web https://worldview.earthdata.nasa.gov/?v=-207.78934227214495,-113.17005215620739,139.7262447856823,55.3388080265203&l=SMAP_L3_Passive_Enhanced_Day_Soil_Moisture(hidden),BlueMarble_NextGeneration(hidden),MODIS_Terra_CorrectedReflectance_TrueColor&lg=false&t=2015-08-08-T16%3A00%3A00Z


## 5. ESTRUCTURA Y ORGANIZACION DE DIRECTORIOS / ARCHIVOS.

### 5.1 DIRECTORIOS Y ARCHIVOS.

El proyecto contiene los siguientes directorios:

    - src --> Se encuentra el codigo fuente del proyecto.
    - test --> Se encuentra los test case y resultados de testing sobre el proyecto.
    - notebooks --> Se encuentra informacion referida al desarrollo de funcionalidades principales y de consulta general.

### 5.1.1 DIRECTORIO **src**

Dentro del directorio **src** se encontraran los siguientes directorios:

    - config --> Se encuentra el script para configuracion de parametros por parte del usuario necesarios para la ejecucion del programa.
    - download --> Se encuentra el script download_nasaearthdata.py que contiene la logica principal del programa.
    - utils --> Se encuentra el script modules.py que contiene los modulos necesarios para la ejecucion del programa

Sumado a los directorios tambien se encuentran los siguientes archivos:

    - main.py --> Script sobre el cual se realiza la llamada para la ejecucion del programa.
    - .env --> Archivo donde se especifican los secretos como variables de entorno necesarias para la conexion con el microservicio (API) de Earthdata


### 5.1.2 DIRECTORIO **test**


### 5.1.3 DIRECTORIO **notebooks**

## 6. INPUT / OUTPUT

### 6.1 INPUT - PARAMETROS DATO DE ENTRADA

El usuario de la funcionalidad tiene permitido configurar la informacion a descargar mediante la especificacion de parametros especificos en el archivo **parameters.py** que se encuentra en **src/config/parameters.py**. A continuacion describe la totalidad de parametros disponibles:

| Variable               | Descripcion                                          | Data Type    | Formato Requerido  | Ejemplo                                            | ¿Es requerido que el usuario complete la variable? | Observaciones |
| -----------------------|:----------------------------------------------------:| :-----------:|:------------------:|:--------------------------------------------------:|:--------------------------------------------------:|:-------------:|
| start_date             | Fecha de Inicio del intervalo temporal               | STRING       | YYYY-MM-DD         | '2023-01-01'                                       | SI                                                 |               |
| start_time             | Hora de Inicio del intervalo temporal                | STRING       | HH-mm-ss           | '00:00:00'                                         | SI                                                 |               |
| end_date               | Fecha de Fin del intervalo temporal                  | STRING       | YYYY-MM-DD         | '2023-01-31'                                       | SI                                                 |               |  
| end_time               | Hora de Fin del intervalo temporal                   | STRING       | HH-mm-ss           | '00:00:00'                                         | SI                                                 |               |
| lower_left_longitude   | Longitud Inferior Izquierda                          | STRING       |                    | '-90'                                              | SI                                                 |               |
| lower_left_latitude    | Latitud Inferior Izquierda                           | STRING       |                    | '-60'                                              | SI                                                 |               |
| upper_right_longitude  | Longitud Superior derecha                            | STRING       |                    | '-30'                                              | SI                                                 |               |
| upper_right_latitude   | Latitud Superior Derecha                             | STRING       |                    | '-60'                                              | SI                                                 |               |
| base_url               | URL base de NSIDC                                    | STRING       |                    | 'https://n5eil02u.ecs.nsidc.org/egi/request'       | NO                                                 |               |
| short_name             | Abreviatura del Producto NSIDC                       | STRING       |                    | 'SPL3SMP_E'                                        | SI                                                 | (*)           |
| version                | Version del Producto NSIDC                           | STRING       |                    | '005'                                              | SI                                                 | (*)           |
| formato                | Formato de las imagenes a obtener                    | STRING       |                    | 'GeoTIFF'                                          | SI                                                 | (*)           |
| coverages              | Variable / capa o grupo de parámetros                | LIST[STRING] |                    | ['/Soil_Moisture_Retrieval_Data_AM/soil_moisture'] | SI                                                 | (*)           |
| projection             | Proyeccion                                           | STRING       |                    | 'Geographic'                                       | SI                                                 | (*)           |
| page_size              | Cantidad de items a devolver en una respuesta        | STRING       |                    | '2000'                                             | NO                                                 |               |
| request_mode           | Modo del Request ['async','stream']                  | STRING       |                    | 'stream'                                           | NO                                                 |               |
| num_retries            | Cantidad de retries a realizar en el request         | INT          |                    | 3                                                  | NO                                                 |               |
| http_status_list       | Codigos de estado HTTP a manejar en los retries      | LIST[INT]    |                    | [429,500,501,502,503,504]                          | NO                                                 |               |
| folder_name_list       | Listado de directorios a crear durante la ejecucion  | LIST[STRING] |                    | ['TMP','OUTPUT','LOGS']                            | NO                                                 |               |
| script_parameters_name | Nombre del Script con los parametros de la ejecucion | STRING       |                    | 'parameters.py'                                    | NO                                                 |               |


(*) Ver **notebooks/NSIDC_data_products/NSIDC - SMAP Data Products.ipynb**