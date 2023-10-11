import os
from dotenv import load_dotenv
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import re
import shutil
import pathlib
import fnmatch
from typing import Union,Optional
import shutil
import zipfile
from datetime import date
from parameters import *

def load_secrets() -> tuple[Optional[str],Optional[str],Optional[str]]:
    '''
    Se cargan los secretos necesarios para consultar el microservicio (API) de EARTHDATA.
    
    ----------------------
    Parametros de Entrada:
    ----------------------
        - N/A.

    ---------------------
    Parametros de Salida:
    ---------------------
        - username(str): Login user name asociada a Earthdata.
        - password(str): Login password asociada a Earthdata.
        - email(str): Direccion de mail asociada a Earthdata.
    '''
    try:
        load_dotenv()
        username = os.getenv("API_USER")
        password = os.getenv("API_SECRET")
        email = os.getenv("API_EMAIL")
        return username,password,email
    
    except:
        username = None
        password = None
        email = None
        return username,password,email

    
def temporal_range(start_date:str,start_time:str,end_date:str,end_time:str) -> tuple[str,str,Optional[str]]:
    '''
    Se construye la ventana temporal a utilizar en el request.
    
    ----------------------
    Parametros de Entrada:
    ----------------------
        - start_date(str): Fecha de inicio en formato 'yyyy-MM-dd'.
        - start_time(str): Hora de inicio en formato 'HH:mm:ss'.
        - end_date(str): Fecha de fin en formato 'yyyy-MM-dd'.
        - end_time(str): Hora de fin en formato 'HH:mm:ss'.   

    ---------------------
    Parametros de Salida:
    ---------------------
        - status_code(str): Codigo de estado ['OK','NOK'].
        - status_message(str): Mensaje de estado.
        - temporal(str): Ventana temporal.
    '''
    try:
        if len(start_date) and len(start_time) and len(end_date) and len(end_time):
            temporal = start_date + 'T' + start_time + 'Z' + ',' + end_date + 'T' + end_time + 'Z'
            status_code = 'OK'
            status_message = ''
            return status_code,status_message,temporal
        else:
            status_code = 'NOK'
            status_message = 'temporal_range() --> Error: Una o mas variables se encuentran vacias --> No es posible contruir la ventana temporal'
            temporal = None
            return status_code,status_message,temporal
        
    except Exception as e:
        status_code = 'NOK'
        status_message = f'temporal_range() --> Exception: {e}'
        temporal = None
        return status_code,status_message,temporal
    
def request_urls_list(param_dict:dict,coverages:list) -> tuple[str,str,Optional[str]]:
    '''
    Se obtiene el listado de URL's a utilizar en el request.
    
    ----------------------
    Parametros de Entrada:
    ----------------------
        - param_dict(dict): Diccionario con key:value correspondiente a los parametros a utilizar para la construccion de la URL del Request.
        - coverages(list): Listado de coverages a considerar para la construccion de la URL del Request.

    ---------------------
    Parametros de Salida:
    ---------------------
        - status_code(str): Codigo de estado ['OK','NOK'].
        - status_message(str): Mensaje de estado.
        - request_list(list): Listado de URL's a las cuales es necesario realizar el request.
    '''
    try:
        request_list = []
        for coverage in coverages:
            param_dict['Coverage'] = coverage

            #Se remueven los pares clave:valor que se encuentran en blanco
            param_dict = {k: v for k, v in param_dict.items() if v != ''}

            #Se toma el conjunto de parametros y se arma el string de parametros
            param_string = '&'.join("{!s}={!r}".format(k,v) for (k,v) in param_dict.items())
            param_string = param_string.replace("'","")

            #Se construye el string del request (API Base URL + Parametros Request)
            api_request = f'{base_url}?{param_string}'
            
            #Se incluye la URL en la lista
            request_list.append(api_request)
            
        if len(request_list) == len(coverages):
            status_code = 'OK'
            status_message = ''
            return status_code,status_message,request_list
        else:
            status_code = 'NOK'
            status_message = 'request_urls_list() --> Error: No fue posible construir la totalidad de URLs correspondientes a los coverages indicados'
            return status_code,status_message,request_list
        
    except Exception as e:
        status_code = 'NOK'
        status_message = f'request_urls_list() --> Excepcion: {e}'
        request_list = None
        return status_code,status_message,request_list
    
def create_root_folder(folder_name_list:list) -> tuple[str,str,Optional[str]]:
    '''
    Se crea un conjunto de directorios dentro del directorio raiz.
    
    ----------------------
    Parametros de Entrada:
    ----------------------
        - folder_name_list(list): Listado con nombres de directorios a contruir apartir del directorio raiz.

    ---------------------
    Parametros de Salida:
    ---------------------
        - status_code(str): Codigo de estado ['OK','NOK'].
        - status_message(str): Mensaje de estado.
        - Directorios creados apartir del directorio raiz --> No forma parate del RETURN de la funcion.
    '''
    try:
        for folder in folder_name_list:
            path = str(os.path.join(os.getcwd(),folder))
            if not os.path.exists(path):
                os.mkdir(path)
        status_code = 'OK'
        status_message = ''
        return status_code,status_message,None
    
    except Exception as e:
        status_code = 'NOK'
        status_message = f'create_root_folder() --> Excepcion: {e}'
        return status_code,status_message,None

def create_folder(origin_folder:str,name_folder:str) -> tuple[str,str,Optional[str]]:
    '''
    Se crea un directorio dentro de otro directorio.
    
    ----------------------
    Parametros de Entrada:
    ----------------------
        - origin_folder(str): Directorio origen donde se creara el nuevo directorio
        - name_folder(str): Nombre del directorio a crear

    ---------------------
    Parametros de Salida:
    ---------------------
        - status_code(str): Codigo de estado ['OK','NOK']
        - status_message(str): Mensaje de estado
        - Directorio creado --> No forma parate del RETURN de la funcion
    '''
    try:
        path = str(os.path.join(origin_folder,name_folder))
        if not os.path.exists(path):
            os.mkdir(path)
        status_code = 'OK'
        status_message = ''
        return status_code,status_message,path
    
    except Exception as e:
        status_code = 'NOK'
        status_message = f'create_folder() --> Excepcion: {e}'
        return status_code,status_message,None

def delete_folder(path:str) -> tuple[str,str,Optional[str]]:
    '''
    Se elimina un directorio
    
    ----------------------
    Parametros de Entrada:
    ----------------------
        - path(str): Directorio a eliminar

    ---------------------
    Parametros de Salida:
    ---------------------
        - status_code(str): Codigo de estado ['OK','NOK'].
        - status_message(str): Mensaje de estado.
        - Directorios eliminado --> No forma parate del RETURN de la funcion.
    '''
    try:
        if os.path.exists(path):
            shutil.rmtree(path)
        else:
            pass
        status_code = 'OK'
        status_message = ''
        return status_code,status_message,None
    
    except Exception as e:
        status_code = 'NOK'
        status_message = f'delete_folder() --> Excepcion: {e}'
        return status_code,status_message,None
    
def dict_folders(folder_name_list:list) -> tuple[str,str,Optional[dict]]:
    '''
    Se incorpora en un diccionario los directorios existentes dentro de otro directorio.
    
    ----------------------
    Parametros de Entrada:
    ----------------------
        - folder_name_list(list): Listado con nombres de directorios a listar apartir del directorio raiz.

    ---------------------
    Parametros de Salida:
    ---------------------
        - status_code(str): Codigo de estado ['OK','NOK'].
        - status_message(str): Mensaje de estado.
        - dict_folder_list(dict): Diccionario que contiene los directorios.
    '''
    try:
        dict_folder_list = {}
        for folder in folder_name_list:
            dict_folder_list[f'path_{folder}'] = str(os.path.join(os.getcwd(),folder))
        status_code = 'OK'
        status_message = ''
        return status_code,status_message,dict_folder_list
    
    except Exception as e:
        status_code = 'NOK'
        status_message = f'dict_folder() --> Excepcion: {e}'
        dict_folder_list = None
        return status_code,status_message,dict_folder_list
    
def list_folders(path:str) -> tuple[str,str,Optional[list]]:
    '''
    Se listan los directorios hijos que forman parte de un directorio padre.
    
    ----------------------
    Parametros de Entrada:
    ----------------------
        - path(str): Directorio Padre.

    ---------------------
    Parametros de Salida:
    ---------------------
        - status_code(str): Codigo de estado ['OK','NOK'].
        - status_message(str): Mensaje de estado.
        - subfolder_list(list): Listado de directorios hijos.
    '''
    try:
        subfolder_list = []
        folders_name = next(os.walk(path))[1]
        for folder_name in folders_name:
            subfolder = str(os.path.join(path,folder_name))
            subfolder_list.append(subfolder)
        status_code = 'OK'
        status_message = ''
        return status_code,status_message,subfolder_list
    
    except Exception as e:
        status_code = 'NOK'
        status_message = f'list_folders() --> Excepcion: {e}'
        subfolder_list = None
        return status_code,status_message,subfolder_list
    
def move_files(source:str,destination:str,pattern:str = '*') -> tuple[str,str,Optional[list]]:
    '''
    Se mueve un conjunto de archivos de un directorio origen a un directorio destino.
    
    ----------------------
    Parametros de Entrada:
    ----------------------
        - source(str): Directorio Origen.
        - destination(str): Directorio Destino.
        - pattern(str)[Opcional --> Default '*']: Patron de archivos a mover.

    ---------------------
    Parametros de Salida:
    ---------------------
        - status_code(str): Codigo de estado ['OK','NOK'].
        - status_message(str): Mensaje de estado.
        - Archivos movidos --> No forma parate del RETURN de la funcion.
    '''
    try:
        if not os.path.isdir(destination):
            pathlib.Path(destination).mkdir(parents=True, exist_ok=True)
        for f in fnmatch.filter(os.listdir(source),pattern):
            shutil.move(os.path.join(source,f),os.path.join(destination, f))
        status_code = 'OK'
        status_message = ''
        return status_code,status_message,None
    
    except Exception as e:
        status_code = 'NOK'
        status_message = f'move_files() --> Excepcion: {e}'
        return status_code,status_message,None

def create_logs_file(name_file_logs:str):
    '''
    Se crea el archivo de .txt para almacenar logs de la ejecucion del proceso.
    
    ----------------------
    Parametros de Entrada:
    ----------------------
        - name_file_logs(str).

    ---------------------
    Parametros de Salida:
    ---------------------
        - status_code(str): Codigo de estado ['OK','NOK'].
        - status_message(str): Mensaje de estado.
        - f(TextIOWrapper): Objeto que referencia al .txt para escribir logs.
    '''
    try:
        file_logs = str(os.path.join(os.getcwd(),name_file_logs))
        f = open(file_logs, 'w')
        f.truncate(0)   
        
        if os.path.exists(file_logs):
            status_code = 'OK'
            status_message = ''
            return status_code,status_message,f
        else:
            status_code = 'NOK'
            status_message = 'create_logs_file() --> Error: No fue posible crear el archivo .txt para almacenar los logs'
            f = None
            return status_code,status_message,f
        
    except Exception as e:
        status_code = 'NOK'
        status_message = f'create_logs_file() --> Exception: {e}'
        f = None
        return status_code,status_message,f
    
def write_log_message(f,texto:str):
    '''
    Se escribe un mensaje (log) en el archivo de .txt de logs
    
    ----------------------
    Parametros de Entrada:
    ----------------------
        - f(TextIOWrapper): Objeto que referencia al .txt para escribir logs
        - texto(str): Texto que se desea escribir

    ---------------------
    Parametros de Salida:
    ---------------------
        - N/A

    '''
    try:
        f.write('\n')
        f.write(f'{texto}\n')
        
    except Exception as e:
        f.write(f'write_log_message() --> Exception: {e}')

def write_error_log_message(f):
    '''
    Se escribe un mensaje (log) por error en tiempo de ejecucion en el archivo de .txt de logs
    
    ----------------------
    Parametros de Entrada:
    ----------------------
        - f(TextIOWrapper): Objeto que referencia al .txt para escribir logs
        - texto(str): Texto que se desea escribir

    ---------------------
    Parametros de Salida:
    ---------------------
        - N/A

    '''
    try:
        message = f'#ATENCION!: SE DA POR FINALIZADO EL PROCESO POR ERROR EN TIEMPO DE EJECUCION'
        f.write('\n')
        f.write(f'{message}\n')
        f.close()
        
    except Exception as e:
        f.write(f'write_error_log_message() --> Exception: {e}')
        f.write('\n')
        f.write(f'{message}\n')
        f.close()
        
def unzip(folder_name:str) -> tuple[str,str,Optional[str]]:
    '''
    Se descomprime un conjunto de archivos dentro del mismo directorio.
    
    ----------------------
    Parametros de Entrada:
    ----------------------
        - folder_name(str): Directorio donde se encuentran los archivos comprimidos.

    ---------------------
    Parametros de Salida:
    ---------------------
        - Archivos descomprimidos --> No forma parate del RETURN de la funcion.
    '''
    try:
        for z in os.listdir(folder_name): 
            if z.endswith('.zip'): 
                zip_name = folder_name + "/" + z 
                zip_ref = zipfile.ZipFile(zip_name) 
                zip_ref.extractall(folder_name) 
                zip_ref.close() 
                os.remove(zip_name)
        status_code = 'OK'
        status_message = ''
        return status_code,status_message,None
    
    except Exception as e:
        status_code = 'NOK'
        status_message = f'unzip() --> Excepcion: {e}'
        return status_code,status_message,None
    
def move_images(origin_folder:str,destination_folder:str) -> tuple[str,str,Optional[str]]:
    '''
    Se mueve el conjunto de imagenes descargadas y descomprimidas desde un conjunto de directorios origen a un directorio destino.
    
    ----------------------
    Parametros de Entrada:
    ----------------------
        - origin_folder(str): Directorio Origen.
        - destination_folder(str): Directorio Destino.

    ---------------------
    Parametros de Salida:
    ---------------------
        - status_code(str): Codigo de estado ['OK','NOK'].
        - status_message(str): Mensaje de estado.
        - Imagenes que se movieron --> No forma parate del RETURN de la funcion.
    '''
    try:
        status_code_list_folders,status_message_list_folders,subfolder_list = list_folders(origin_folder)
        if status_code_list_folders == 'OK':
            for subfolder in subfolder_list:
                move_files(subfolder,destination_folder)
            status_code = 'OK'
            status_message = ''
            return status_code,status_message,None
        else:
            status_code = 'NOK'
            status_message = 'move_images() --> list_folders() --> Error: No se obtuvo la lista de directorios necesarios para realizar la copia de imagenes'
            return status_code,status_message,None
            
    except Exception as e:
        status_code = 'NOK'
        status_message = f'move_images() --> Excepcion: {e}'
        return status_code,status_message,None

def execute_request(username:str,password:str,request_url:str,destination_path:str,num_retries:int,http_status_list:list) -> tuple[str,str,Optional[str]]:
    '''
    Se realiza el request y el resultado se guarda en el directorio especificado.
    
    ----------------------
    Parametros de Entrada:
    ----------------------
        - username(str): Nombre de Usuario.
        - password(str): Contraseña.
        - request_url(str): URL.
        - destination_path(str): Directorio Destino.
        - num_retries(int): Cantidad de Retries.
        - http_status_list(list): Listado de codigos de estado HTTP a manejar.

    ---------------------
    Parametros de Salida:
    ---------------------
        - status_code(str): Codigo de estado ['OK','NOK'].
        - status_message(str): Mensaje de estado.
        - Imagenes devueltas por el response --> No forma parate del RETURN de la funcion.
    '''
    try:
        #Se define la estrategia de retry.
        retry_strategy = Retry(total=num_retries,status_forcelist=http_status_list)

        #Se crea un adaptador HTTP que contiene la estrategia de retry.
        adapter = HTTPAdapter(max_retries=retry_strategy)
        
        #Se crea una sesion para almecenar las cookies y pasar las credenciales al microservicio
        session = requests.session()

        #Se monta el adaptador HTTP en la sesion
        session.mount('http://', adapter)
        session.mount('https://', adapter)

        #Se realiza el request
        s = session.get(request_url)
        request = session.get(s.url,auth=(username,password))
        request_status_code = request.status_code
        request.raise_for_status()
        d = request.headers['content-disposition']
        fname = re.findall('filename=(.+)', d)
        dirname = os.path.join(destination_path,fname[0].strip('\"'))
        open(dirname, 'wb').write(request.content)
        
        if request_status_code == 200:
            status_code = 'OK'
            status_message = f'HTTP response status code : {str(request_status_code)}'
            return status_code,status_message,None
        else:
            status_code = 'NOK'
            status_message = f'HTTP response status code : {str(request_status_code)}'
            return status_code,status_message,None

    except Exception as e:
        status_code = 'NOK'
        status_message = f'execute_request() --> Excepcion: {e}'
        return status_code,status_message,None

def check_execution_result(destination_folder:str,start_date:str,end_date:str,coverages:list) -> tuple[str,str,Optional[str]]:
    '''
    Se realiza el check de la cantidad de imagenes obtenidas con respecto a la cantidad teorica.
    
    ----------------------
    Parametros de Entrada:
    ----------------------
        - detination_folder(str): Diccionario donde se guardaron las imagenes
        - start_date(str): Parametro --> Fecha de inicio
        - end_date(str): Parametro --> Fecha de fin
        - coverages(list): Parametro --> Lista de productos

    ---------------------
    Parametros de Salida:
    ---------------------
        - status_code(str): Codigo de estado ['OK','NOK'].
        - status_message(str): Mensaje de estado.
        - request_list(list): Listado de URL's a las cuales es necesario realizar el request.
    '''
    try:
        start_date_inicio = date(int(start_date[0:4]),int(start_date[5:7]),int(start_date[8:]))
        start_date_fin = date(int(end_date[0:4]),int(end_date[5:7]),int(end_date[8:]))
        dias = ((start_date_fin - start_date_inicio).days) + 1 

        cantidad_imagenes_teorica = dias * len(coverages)
        cantidad_imagenes_real = len([name for name in os.listdir(destination_folder) if os.path.isfile(os.path.join(destination_folder, name))])

        if cantidad_imagenes_teorica == cantidad_imagenes_real:
            status_code = 'OK'
            status_message = ''
            return status_code,status_message,None
        
        elif cantidad_imagenes_teorica > cantidad_imagenes_real:
            status_code = 'NOK'
            status_message = 'check_execution_result() --> Error: La cantidad de imagenes que se obtuvieron ES MENOR que la cantidad teorica esperada'
            return status_code,status_message,None
        
        else:
            status_code = 'NOK'
            status_message = 'check_execution_result() --> Error: La cantidad de imagenes que se obtuvieron ES MAYOR que la cantidad teorica esperada'
            return status_code,status_message,None
        
    except Exception as e:
        status_code = 'NOK'
        status_message = f'check_execution_result() --> Exception: {e}'
        return status_code,status_message,None