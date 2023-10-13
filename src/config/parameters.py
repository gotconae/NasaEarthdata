##############################################################################
### A.VARIABLES DEL REQUEST - COMPLETAR POR PARTE DEL USUARIO DEL PRODUCTO ###
##############################################################################

# A1. FECHAS --> [str]
start_date = '2023-01-01' #Fecha de inicio en formato 'yyyy-MM-dd' (str)
start_time = '00:00:00' #Hora de inicio en formato 'HH:mm:ss' (str)
end_date = '2023-01-02' #Fecha de fin en formato 'yyyy-MM-dd' (str)
end_time = '00:00:00' #Hora de fin en formato 'HH:mm:ss' (str)

#A2. ZONA GEOGRAFICA --> [str]
lower_left_longitude = '-90'
lower_left_latitude = '-60'
upper_right_longitude = '-30'
upper_right_latitude = '20'
bbox = lower_left_longitude + ',' + lower_left_latitude + ',' + upper_right_longitude + ',' + upper_right_latitude

#A3. URL Base - National Snow & Ice Data Center (NSIDC) --> [str]
base_url = 'https://n5eil02u.ecs.nsidc.org/egi/request'

#A4. Nombre del servicio --> [str]
short_name = 'SPL3SMP_E'

#A5. Version del servicio --> [str]
version = '005'

#A6. Formato de salida de las imagenes --> [str]
formato = 'GeoTIFF'

#A7. Productos a considerar --> [list] + [str]
coverages = ['/Soil_Moisture_Retrieval_Data_AM/soil_moisture',
             '/Soil_Moisture_Retrieval_Data_PM/soil_moisture_pm']

#A8. Proyeccion --> [str]
projection = 'Geographic' 

#A9. Tamaño de la pagina --> [str]
page_size = '100'

############################################################################################################
### B.CONFIGURACION DEL REQUEST - VALORES PREDEFINIDOS (NO MODIFICAR POR PARTE DEL USUARIO DEL PRODUCTO) ###
############################################################################################################

#B1. Modo del Request --> [str]
request_mode = 'stream'

#B2. Cantidad de Retries --> [int]
num_retries = 3

#B3. Listado de codigos de estado HTTP a manejar --> [list] + [int]
http_status_list = [429,500,501,502,503,504]


################################################
### C.CONFIGURACION DE DIRECTORIOS (FOLDERS) ###
################################################

#C1. Nombre de FOLDERS a contruir para la ejecucion --> [list] + [str]:
    #Directorios OBLIGATORIOS: ['TMP','SMAP']
folder_name_list = ['TMP','OUTPUT','LOGS']


###############
### D.OTROS ###
###############

#D1. Nombre del script donde se cargan los parametros a utilizar durante la ejecucion
script_parameters_name = 'parameters.py'