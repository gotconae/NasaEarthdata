# National Snow and Ice Data Center (NSIDC) - Consulta de datos 

## 1. Objetivo

Este proyecto tiene como objetivo disponibilizar una funcionalidad que facilite la descarga de datos correspondientes al National Snow and Ice Data Center (NSIDC).

## 2. Estructura y organizacion de directorios y archivos

### 2.1 Directorios

El proyecto contiene los siguientes directorios:

    - src --> Se encuentra el codigo fuente del proyecto.
    - test --> Se encuentra los test case y resultados de testing sobre el proyecto.
    - notebooks --> Se encuentra informacion referida al desarrollo de funcionalidades principales y de consulta general.

### 2.2.1 Directorio **src**

Dentro del directorio **src** se encontraran los siguientes directorios:

    - config --> Se encuentra el script para configuracion de parametros por parte del usuario necesarios para la ejecucion del programa.
    - download --> Se encuentra el script download_nasaearthdata.py que contiene la logica principal del programa.
    - utils --> Se encuentra el script modules.py que contiene los modulos necesarios para la ejecucion del programa

Sumado a los directorios tambien se encuentra:
    - main.py --> Script sobre el cual se realiza la llamada para la ejecucion del programa.
    - .env --> Archivo donde se especifican los secretos como variables de entorno necesarias para la conexion con el microservicio (API) de Earthdata


### 2.2.2 Directorio **test**


### 2.2.3 Directorio **notebooks**
