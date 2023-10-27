##############################################################################
### A.VARIABLES DEL REQUEST - COMPLETAR POR PARTE DEL USUARIO DEL PRODUCTO ###
##############################################################################

# A1. Fechas --> [str]
start_date = '2023-01-01' #Fecha de inicio en formato 'YYYY-MM-DD' (str)
start_time = '00:00:00' #Hora de inicio en formato 'HH:mm:ss' (str)
end_date = '2023-01-02' #Fecha de fin en formato 'YYYY-MM-DD' (str)
end_time = '00:00:00' #Hora de fin en formato 'HH:mm:ss' (str)

# A2. Zona Geografica --> [str]
left = '-90'
bottom = '-60'
right = '-30'
top = '20'
bbox = left + ',' + bottom + ',' + right + ',' + top

# A3. URL Base - National Snow & Ice Data Center (NSIDC) --> [str]
base_url = 'https://n5eil02u.ecs.nsidc.org/egi/request'

# A4. Nombre del Producto --> [str]
short_name = 'SPL3SMP_E'

# A5. Version del Producto --> [str]
version = '005'

# A6. Formato de salida de las imagenes --> [str]
formato = 'GeoTIFF'

# A7. Variable / Capa --> [list] + [str]
coverages = ['/Soil_Moisture_Retrieval_Data_AM/soil_moisture',
             '/Soil_Moisture_Retrieval_Data_PM/soil_moisture_pm']

# A8. Proyeccion --> [str]
projection = 'Geographic' 

# A9. Cantidad de items a devolver en una respuesta --> [str]
page_size = '2000'

############################################################################################################
### B.CONFIGURACION DEL REQUEST - VALORES PREDEFINIDOS (NO MODIFICAR POR PARTE DEL USUARIO DEL PRODUCTO) ###
############################################################################################################

# B1. Modo del Request --> [str]
request_mode = 'stream'

# B2. Cantidad de Retries --> [int]
num_retries = 3

# B3. Listado de codigos de estado HTTP a manejar --> [list] + [int]
http_status_list = [429,500,501,502,503,504]


################################################
### C.CONFIGURACION DE DIRECTORIOS (FOLDERS) ###
################################################

# C1. Nombre de FOLDERS a contruir para la ejecucion --> [list] + [str]:
    #Directorios OBLIGATORIOS: ['TMP','SMAP']
folder_name_list = ['TMP','OUTPUT','LOGS']


###############
### D.OTROS ###
###############

# D1. Nombre del script donde se cargan los parametros a utilizar durante la ejecucion
script_parameters_name = 'parameters.py'

# D2. Flag para habilitar / deshabilitar la creacion y escritura de logs --> [bool]
write_logs_flag = True