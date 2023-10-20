# NASA EARTHDATA.

## National Snow and Ice Data Center Distributed Active Archive Center (NSIDC DAAC).

## Funcionalidad para descarga de datos (imagenes) mediante el uso de EOS-CMR API.

## 1. ABREVIATURAS.

    * NSIDC: National Snow and Ice Data Center
    * DAAC: Distributed Active Archive Center
    * EOS: Earth Observing System
    * CRM: Common Metadata Repository
    * API: Application programming interface
    * SMAP: Soil Moisture Active Passive Data

## 2. OBJETIVO.

Este proyecto tiene como objetivo disponibilizar una funcionalidad que facilite la consulta y descarga de datos correspondientes **NASA National Snow and Ice Data Center Distributed Active Archive Center (NSIDC DAAC)** y utilizando la funcionalidad disponible de consulta via API.
Si bien originalmente esta funcionalidad fue pensada para consulta de datos correspondientes a la mision **Soil Moisture Active Passive Data (SMAP)** la misma puede ser utilizada para otras misiones que permiten la consulta y descarga de datos utilizando EOS-CMR API.

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


### 4.2 SMAP.

* Soil Moisture Active Passive Data (SMAP) https://nsidc.org/data/smap

* What data subsetting, reformatting, and reprojection services are available for SMAP data? https://nsidc.org/data/user-resources/help-center/what-data-subsetting-reformatting-and-reprojection-services-are-available-smap-data

* SMAP Enhanced L3 Radiometer Global and Polar Grid Daily 9 km EASE-Grid Soil Moisture, Version 5 (SPL3SMP_E) https://nsidc.org/data/spl3smp_e/versions/5

* SMAP Enhanced L3 Radiometer Global and Polar Grid Daily 9 km EASE-Grid Soil Moisture V005 https://cmr.earthdata.nasa.gov/search/concepts/C2136471727-NSIDC_ECS.html

* Interfaz grafica web https://worldview.earthdata.nasa.gov/?v=-207.78934227214495,-113.17005215620739,139.7262447856823,55.3388080265203&l=SMAP_L3_Passive_Enhanced_Day_Soil_Moisture(hidden),BlueMarble_NextGeneration(hidden),MODIS_Terra_CorrectedReflectance_TrueColor&lg=false&t=2015-08-08-T16%3A00%3A00Z


## 5. ESTRUCTURA Y ORGANIZACION DE DIRECTORIOS / ARCHIVOS.

### 5.1 DIRECTORIOS Y ARCHIVOS.

El proyecto contiene los siguientes directorios:

    - src --> Se encuentra el codigo fuente del proyecto.
    - tests --> Se encuentra los test case (unit / integration) y resultados.
    - notebooks --> Se encuentra informacion referida al desarrollo de funcionalidades principales y de consulta general.
    - docs --> Se encuentra documentacion adicional y complementaria sobre el proyecto.

### 5.1.1 DIRECTORIO **src**

Dentro del directorio **src** se encontraran los siguientes directorios:

    - config --> Se encuentra el script para configuracion de parametros por parte del usuario necesarios para la ejecucion del programa.
    - download --> Se encuentra el script download_nasaearthdata.py que contiene la logica principal del programa.
    - utils --> Se encuentra el script modules.py que contiene los modulos necesarios para la ejecucion del programa.

Sumado a los directorios tambien se encuentran los siguientes archivos:

    - main.py --> Script sobre el cual se realiza la llamada para la ejecucion del programa.
    - .env --> Archivo donde se especifican los secretos como variables de entorno necesarias para la conexion con el microservicio (API) de Earthdata.


### 5.1.2 DIRECTORIO **test**

Dentro del directorio **test** se incluye:

    - Directorio unit: Se incluyen los tests unitarios.
    - Directorio integration: Se incluyen los test de integracion. Dentro de este directorio se incluye en directorios especificos los archivos **parameters.py** utilizados para cada configuracion evaluada.

Sumado a lo anterior se incluye un archivo resumen donde se indica las caracterisitcas de cada Test Case y el resultado de la ejecucion del mismo.

### 5.1.3 DIRECTORIO **notebooks**

Dentro del directorio **notebooks** se encontraran los siguientes directorios:

    - develop --> Se encuentran las notebooks (.ipynb) correspondientes al desarrollo inicial de funcionalidades del proyecto.
    - NSIDC_data_products --> Se encuentran las notebooks (.ipynb) correspondientes a la identificacion de posibles valores a seterar por parte del usuario en las variables del archivo **parameters.py**.


## 6. INPUT / OUTPUT

### 6.1 INPUT - PARAMETROS - DATOS DE ENTRADA

El usuario de la funcionalidad tiene permitido configurar la informacion a descargar mediante la especificacion de parametros especificos en el archivo **parameters.py** que se encuentra en **src/config/parameters.py**. A continuacion describe la totalidad de parametros disponibles:

| Variable               | Descripcion                                          | Data Type    | Formato Requerido  | Ejemplo                                            | ¿Es requerido que el usuario complete la variable? | Observaciones |
| -----------------------|:----------------------------------------------------:| :-----------:|:------------------:|:--------------------------------------------------:|:--------------------------------------------------:|:-------------:|
| start_date             | Fecha de Inicio del intervalo temporal               | STRING       | YYYY-MM-DD         | '2023-01-01'                                       | SI                                                 |               |
| start_time             | Hora de Inicio del intervalo temporal                | STRING       | HH-mm-ss           | '00:00:00'                                         | SI                                                 |               |
| end_date               | Fecha de Fin del intervalo temporal                  | STRING       | YYYY-MM-DD         | '2023-01-31'                                       | SI                                                 | (1)           |  
| end_time               | Hora de Fin del intervalo temporal                   | STRING       | HH-mm-ss           | '00:00:00'                                         | SI                                                 | (1)           |
| lower_left_longitude   | Longitud Inferior Izquierda                          | STRING       |                    | '-90'                                              | SI                                                 |               |
| lower_left_latitude    | Latitud Inferior Izquierda                           | STRING       |                    | '-60'                                              | SI                                                 |               |
| upper_right_longitude  | Longitud Superior derecha                            | STRING       |                    | '-30'                                              | SI                                                 |               |
| upper_right_latitude   | Latitud Superior Derecha                             | STRING       |                    | '-60'                                              | SI                                                 |               |
| bbox                   | Bounding Box                                         | STRING       |                    | '2023-01-01,00:00:00,2023-01-03,00:00:00'          | NO                                                 | (2)           |
| base_url               | URL base de NSIDC                                    | STRING       |                    | 'https://n5eil02u.ecs.nsidc.org/egi/request'       | NO                                                 |               |
| short_name             | Abreviatura del Producto NSIDC                       | STRING       |                    | 'SPL3SMP_E'                                        | SI                                                 | (3)           |
| version                | Version del Producto NSIDC                           | STRING       |                    | '005'                                              | SI                                                 | (2)           |
| formato                | Formato de las imagenes a obtener                    | STRING       |                    | 'GeoTIFF'                                          | SI                                                 | (3)           |
| coverages              | Variable / capa o grupo de parámetros                | LIST[STRING] |                    | ['/Soil_Moisture_Retrieval_Data_AM/soil_moisture'] | SI                                                 | (3)           |
| projection             | Proyeccion                                           | STRING       |                    | 'Geographic'                                       | SI                                                 | (3)           |
| page_size              | Cantidad de items a devolver en una respuesta        | STRING       |                    | '2000'                                             | NO                                                 |               |
| request_mode           | Modo del Request ['async','stream']                  | STRING       |                    | 'stream'                                           | NO                                                 |               |
| num_retries            | Cantidad de retries a realizar en el request         | INT          |                    | 3                                                  | NO                                                 |               |
| http_status_list       | Codigos de estado HTTP a manejar en los retries      | LIST[INT]    |                    | [429,500,501,502,503,504]                          | NO                                                 |               |
| folder_name_list       | Listado de directorios a crear durante la ejecucion  | LIST[STRING] |                    | ['TMP','OUTPUT','LOGS']                            | NO                                                 |               |
| script_parameters_name | Nombre del Script con los parametros de la ejecucion | STRING       |                    | 'parameters.py'                                    | NO                                                 |               |
| write_logs_flag        | Flag - Creacion y escritura de logs                  | BOOL         |                    | True                                               | SI                                                 | (4)           |

(1) La configuracion requerida del request **NO PERMITE** dejar estas variables como un string vacio o especificar el mismo valor que start_date / start_time --> Es requerido que se especifique un rango temporal donde start_date y end_date tengan como minimo 1 dia de diferencia y con valores crecientes (end_date > start_date)

(2) Esta variable es contruida utilizando las variables **start_date / start_time / end_date / end_time**, por lo tanto tener cuidado de **NO MODIFICARLA**.

(3) Para el caso de consulta de datos correspondientes a **SMAP** tomar como referencia de posibles valores lo especificado en **notebooks/NSIDC_data_products/NSIDC - SMAP Data Products.ipynb**.

(4) Posibles valores: True --> Se crea el archivo .txt de logs y se registran los eventos de la ejecucion. / False --> No se crea el archivo .txt de logs y no se registran los eventos de la ejecucion.

### 6.1 OUTPUT - DATOS DE SALIDA

Como parte de la ejecucion de la funcionalidad se crean los siguientes directorios dentro de **src**:

     * OUTPUT --> Donde se almacenan las imagenes descargadas. Este directorio si no existe es creado en la primera ejecucion y es permanente (no es eliminado en proximas ejecuciones)
     * LOGS --> Donde se almacenan los archivos *txt correspondientes a logs. Este directorio si no existe es creado en la primera ejecucion y es permanente (no es eliminado en proximas ejecuciones)
     * TMP --> Donde se almacenan en forma temporal las imagenes obtenidas del response. Este directorio si no existe es creado en la primera ejecucion y es eliminado al finalizar la ejecucion.


#### 6.1.1 EJECUCION COMO FUNCIONALIDAD UNICA

Cuando se utiliza la funcionalidad solo para descarga de imagenes y no forma parte integral de otra funcionalidad **SE RECOMIENDA** configurar la variable **write_logs_flag = True** que se encuentra **src/config/parameters.py** de forma tal de disponibilizar los logs (archivo .txt) correspondiente a cada ejecucion. 

Como salida de la ejecucion de la funcionalidad se obtiene:

1) Si se configuro **write_logs_flag = True** --> Se guarda informacion sobre la secuencia de etapas que forman parte de la ejecucion en curso en un archivo *txt en la carpeta **src/LOGS**. La nomenclatura del archivo log es identificador unico de la ejecucion y se relaciona con los valores especificados en las variables de  **src/config/parameters.py** (ej: 'log_ejecucion_2023-10-17T16-45-14_SPL3SMP_E_005_2023-01-01_2023-01-02.txt'). 

    En caso de especificar **write_logs_flag = False** no se crea el archivo de logs y por lo tanto no se registra las secuencia de etapas durante la ejecucion.

2) Por consola se imprime el estado ['OK','NOK'] de cada una de las etapas que forman parte de la ejecucion. Esto es de utilidad para el usuario de forma tal de dar seguimiento a la ejecucion.

3) Las imagenes descargadas que se alojan en **src/OUTPUT**. Las mismas se guardan dentro de una carpeta creada durante la ejecucion cuya nomenclatura es identificador unico de la ejecucion y se relaciona con los valores especificados en las variables de  **src/config/parameters.py**. El nombre de la carpeta se condice con el nombre del archivo log en caso que se especifique su obtencion. 

    Es importante aclarar que la totalidad de imagenes descargadas se guardan en una carpeta unica, por lo tanto si es necesario obtener imagenes de diferentes capas (coverages) es necesario realizar diferentes ejecuciones.


#### 6.1.2 EJECUCION COMO MODULO DE OTRA FUNCIONALIDAD

Cuando se utiliza la funcionalidad como un modulo especifico que forma parte de otra funcionalidad **SE RECOMIENDA** configurar la variable **write_logs_flag = False** que se encuentra **src/config/parameters.py** de forma tal de **NO** disponibilizar los logs (archivo .txt) correspondiente a cada ejecucion. 

Como salida de la ejecucion de la funcionalidad se obtiene:

1) Las imagenes descargadas que se alojan en **src/OUTPUT**. Las mismas se guardan dentro de una carpeta creada durante la ejecucion cuya nomenclatura es identificador unico de la ejecucion y se relaciona con los valores especificados en las variables de  **src/config/parameters.py**. El nombre de la carpeta se condice con el nombre del archivo log en caso que se especifique su obtencion. 

    Es importante aclarar que la totalidad de imagenes descargadas se guardan en una carpeta unica, por lo tanto si es necesario obtener imagenes de diferentes capas (coverages) es necesario realizar diferentes ejecuciones.

2) Como devolucion de la ejecucion (return):
    * status_code_check_execution(str): Codigo de estado ['OK','NOK'].
    * status_message_check_execution(str): Mensaje de estado.
    * destination_folder(str): Directorio donde se alojan las imagenes descargadas.

## 7. EJECUCION

1. Clonar el repositorio mediante HTTPS:

    ```bash
    git clone https://github.com/gotconae/NasaEarthdata.git
    ```

2. Posicionarse en la raiz del directorio **NasaEarthdata** y crear un entorno virtual. Para esto se disponen diferentes alternativas y como referencia se puede consultar la documentacion oficial de Python https://docs.python.org/3/library/venv.html

3. Instalar las dependencias necesarias:

    ```bash
    pip install -r requirements.txt
    ```

3. Configurar las credenciales de acceso a **EARTHDATA** en el archivo *.env* que se encuentra en el directorio **/src**:

    - API_USER = ''
    - API_SECRET = ''
    - API_EMAIL = ''

4. Completar el conjunto de parametros requeridos del script *parameters.py* que se encuentra en el directorio **/src/config**

5. Posicionarse dentro del directorio **/src** y ejecutar el script principal:

    ```bash
    cd src

    python main.py
    ```

6. Finalizada la ejecucion y si la misma fue satisfactoria se encontraran las imagenes descargadas en el directorio **/src/OUPUT/NOMBRE_CARPETA** donde **NOMBRE_CARPETA** se corresponde con el identificador unico de la ejecucion realizada. 

    Si ademas se especifico en **src/config/parameters.py** la variable **write_logs_flag = True** entonces se dispondra del archivo *txt con logs en **/src/LOGS/NOMBRE_LOG** donde **NOMBRE_LOG** se corresponde con el identificador unico de la ejecucion realizada


## 8. ISSUES IDENTIFICADOS

La forma de identificar los errores ocurridos en tiempo de ejecucion son:

1)  Si se configuro **write_logs_flag = True** se tendra disponible el archivo de logs donde se identifica en que etapa se produjo el error junto con el mensaje correspondiente. 

2) Como parte del return de la ejecucion se tiene obtiene el **status_message_check_execution** con el mensaje de error correspondiente.

### 8.1 NO RELACIONADOS CON LA LOGICA DE LA FUNCIONALIDAD.

Estos issues estan relacionados con valores de las variables que debe completar el usuario en el archivo **parameters.py** que son incorrectos y por lo tanto se produce un error al momento de realizar el request a la API. En caso que esto suceda se obtendra un mensaje de error que contiene la consigna **'content-disposition'** dentro de su contenido. 
Para dar solucion a este tipo de issue revisar detalladamente los valores introducidos en las variables considerando lo indicando en **6.1 INPUT - PARAMETROS - DATOS DE ENTRADA** ye jecutar el proceso nuevamente.

### 8.2 INDISPONIBILIDAD DEL SERVICIO EOS-CMR API.

Si bien al momento de realizar los requests a EOS-CMR API se dispone de la funcionalidad para retry pueden ocurrir errores en tiempo de ejecucion por indisponibilidad del servicio. En caso que esto suceda se obtendra un mensaje de error que contiene alguno de los siguiente textos:

    - HTTPSConnectionPool(host='n5eil02u.ecs.nsidc.org', port=443): Max retries exceeded with url
    - Caused by ResponseError('too many 503 error responses')
    - Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1006)'))
    - Caused by ProtocolError('Connection aborted.', ConnectionResetError(10054, 'Se ha forzado la interrupcion de una conexion existente por el host remoto', None, 10054, None))

En caso de identificar un mensaje de error distinto por favor dar aviso a **ccollado@conae.gov.ar** incluyendo el archivo de logs.


### 8.3 RELACIONADOS CON LA LOGICA DE LA FUNCIONALIDAD.

Como resultado de los **integration test cases** ejecutados no se identificaron errores relacionados con la logica de la funcionalidad.

En caso de detectar alguna por favor dar aviso a **ccollado@conae.gov.ar** incluyendo:

    - Archivo **parametros.py**
    - Archivo de logs
    - Informacion adicional que permita replicar las condiciones de ejecucion: SO utilizado / IDE utilizado / archivo requirements.txt en caso de modificar las dependencias / etc.

## 9. TO DO

    * [ ] Incorporar validaciones sobre los parametros temporales que recibe la funcion temporal_range()
    * [ ] Realizar Unit Test de las funciones definidas en /src/utils/modules.py
    * [ ] Refactor a OOP 
    * [ ] Automatizacion de Test Cases (unit / integration)
    * [ ] Uso de la funcionalidad con Docker