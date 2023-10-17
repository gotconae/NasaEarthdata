# National Snow and Ice Data Center (NSIDC) - Consulta de datos 

## 1. Objetivo

Este proyecto tiene como objetivo disponibilizar una funcionalidad que facilite la descarga de datos correspondientes al National Snow and Ice Data Center (NSIDC).

## 2. Estructura y organizacion de directorios y archivos

### 2.1 Directorios y archivos.

El proyecto contiene los siguientes directorios:

    - src --> Se encuentra el codigo fuente del proyecto.
    - test --> Se encuentra los test case y resultados de testing sobre el proyecto.
    - notebooks --> Se encuentra informacion referida al desarrollo de funcionalidades principales y de consulta general.

### 2.2.1 Directorio **src**

Dentro del directorio **src** se encontraran los siguientes directorios:

    - config --> Se encuentra el script para configuracion de parametros por parte del usuario necesarios para la ejecucion del programa.
    - download --> Se encuentra el script download_nasaearthdata.py que contiene la logica principal del programa.
    - utils --> Se encuentra el script modules.py que contiene los modulos necesarios para la ejecucion del programa

Sumado a los directorios tambien se encuentran los siguientes archivos:

    - main.py --> Script sobre el cual se realiza la llamada para la ejecucion del programa.
    - .env --> Archivo donde se especifican los secretos como variables de entorno necesarias para la conexion con el microservicio (API) de Earthdata


### 2.2.2 Directorio **test**


### 2.2.3 Directorio **notebooks**

## 3. Input / Output

### 3.1 Input - Parametros datos de entrada

El usuario del programa dispone de la posibilidad de configurar la informacion a descargar mediante la especificacion de parametros en el archivo **parameters.py** que se encuentra en src/config. A continuacion describe la totalidad de parametros disponibles:

| Variable              | Descripcion                       | Data Type  | Formato Requerido  | Ejemplo                                      | ¿Requerido que complete la variable el Usuario? | Observaciones      |
| ---------------       |:---------------------------------:| :---------:|:------------------:|:--------------------------------------------:|:-----------------------------------------------:|:------------------:|
| start_date            | Fecha de Inicio                   | STRING     | YYYY-MM-DD         | '2023-01-01'                                 | SI                                              |                    |
| start_time            | Hora de Inicio                    | STRING     | HH-mm-ss           | '00:00:00'                                   | SI                                              |                    |
| end_date              | Fecha de Fin                      | STRING     | YYYY-MM-DD         | '2023-01-31'                                 | SI                                              |                    |  
| end_time              | Hora de Fin                       | STRING     | HH-mm-ss           | '00:00:00'                                   | SI                                              |                    |
| end_time              | Hora de Fin                       | STRING     | HH-mm-ss           | '00:00:00'                                   | SI                                              |                    |
| lower_left_longitude  | Longitud Inferior Izquierda       | STRING     |                    | '-90'                                        | SI                                              |                    |
| lower_left_latitude   | Latitud Inferior Izquierda        | STRING     |                    | '-60'                                        | SI                                              |                    |
| upper_right_longitude | Longitud Superior derecha         | STRING     |                    | '-30'                                        | SI                                              |                    |
| upper_right_latitude  | Latitud Superior Derecha          | STRING     |                    | '-60'                                        | SI                                              |                    |
| base_url              | URL base de NSIDC                 | STRING     |                    | 'https://n5eil02u.ecs.nsidc.org/egi/request' | NO                                              |                    |
| short_name            | Abreviatura del Producto NSIDC    | STRING     |                    | 'SPL3SMP_E'                                  | SI                                              | Ver Notebook       |
| version               | Version del Producto NSIDC        | STRING     |                    | '005'                                        | SI                                              | Ver Notebook       |
| formato               | Formato de las imagenes a obtener | STRING     |                    | 'GeoTIFF'                                    | SI                                              | Ver Notebook       |

