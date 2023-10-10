#Import packages

import time
from datetime import datetime
import inspect

from utils import load_secrets
from utils import temporal_range
from utils import request_urls_list
from utils import create_root_folder
from utils import create_folder
from utils import delete_folder
from utils import dict_folders
from utils import create_logs_file
from utils import write_log_message
from utils import write_error_log_message
from utils import unzip
from utils import move_images
from utils import execute_request
from utils import check_execution_result

import parameters
from parameters import *

def download_nasaearthdata():
    
    ##############################
    ### CONDIDCIONES INICIALES ###
    ##############################

    #Marca temporal correspondiente al inicio de la ejecucion.
    execution_time_start = time.time()

    #Request - Diccionario con parametros.
    param_dict = {'short_name': short_name, 
                  'version': version,
                  'format': formato,
                  'time': '',
                  'Coverage': '',
                  'projection': projection,
                  'bbox': bbox,
                  'email': '',
                  'page_size': page_size,
                  'request_mode': request_mode
                 }
    
    #################################################################################################################
    ### ETAPA N°0: Se crea el archivo donde se guardaran los logs de la ejecucion en curso --> create_logs_file() ###
    #################################################################################################################

    datetime_execution = datetime.today().isoformat('T','seconds')
    time_now = datetime_execution.replace(':','-')
    name_file_log = f'log_ejecucion_{time_now}_{short_name}_{version}_{start_date}_{end_date}.txt'
    status_code_log_file,status_message_log_file,log = create_logs_file(name_file_log)
    if status_code_log_file == 'OK':
        #log - Se contruye el mensaje inicial y se realiza la escritura.
        message = f'ATENCION! --> SE INICIA LA EJECUCION DEL PROCESO [{short_name}] CON FECHA: [{datetime_execution}]'
        write_log_message(log,'#'*len(message))
        write_log_message(log,message)
        write_log_message(log,'#'*len(message))
    
        #log - Se construye el mensaje con el conjunto de parametros a utilizar para la ejecucion en curso y se realiza la escritura.
        list_parameters = [v for v in dir(parameters) if v[:2] != "__"]
        parameters_values = dict(inspect.getmembers(parameters))
        message = f'LOS PARAMETROS QUE SE CARGARON EN EL SCRIPT [{script_parameters_name}] Y SERAN UTILIZADOS PARA LA EJECUCION EN CURSO SON:'
        write_log_message(log,'#'*150)
        write_log_message(log,message)
        for parameter in list_parameters:
            valor = parameters_values[parameter]
            message = f'\t{parameter} = {valor}'
            write_log_message(log,message)
        write_log_message(log,'#'*150)

        ##########################################################################################################################
        ### ETAPA N°1: Se cargan los secretos para realizar la conexion al microservicio (API) de EARTHDATA --> load_secrets() ###
        ##########################################################################################################################

        username,password,email = load_secrets()
        if (username is not None) and (password is not None) and (email is not None):
            #Se incorpora el valor de la variable 'email' al diccionario de parametros.
            param_dict['email'] = email

            #log - Se contruye el mensaje y se realiza la escritura.
            status_code_load_secrets = 'OK'
            status_message_load_secrets = ''
            message = f'#ETAPA 1: Se cargan los secretos para realizar la conexion al microservicio (API) de EARTHDATA --> load_secrets() --> Estado:[{status_code_load_secrets}] --> Mensaje:[{status_message_load_secrets}] --> {round(time.time() - execution_time_start,4)} seg'
            write_log_message(log,message)

            #################################################################################################
            ### ETAPA N°2: Se construye la ventana temporal a utilizar en el request --> temporal_range() ###
            #################################################################################################

            status_code_time,status_message_time,time_range = temporal_range(start_date,start_time,end_date,end_time)

            #log - Se contruye el mensaje y se realiza la escritura.
            message = f'#ETAPA 2: Se construye la ventana temporal [{time_range}] a utilizar en el request --> temporal_range() --> Estado:[{status_code_time}] --> Mensaje:[{status_message_time}] --> {round(time.time() - execution_time_start,4)} seg'
            write_log_message(log,message)

            if status_code_time == 'OK':
                #Se incorpora el valor de la variable 'time' al diccionario de parametros.
                param_dict['time'] = time_range

                ##################################################################################################
                ### ETAPA N°3: Se obtiene el listado de URL's a utilizar en el request --> request_urls_list() ###
                ##################################################################################################

                status_code_request_list,status_message_request_list,request_list = request_urls_list(param_dict,coverages)

                #log - Se contruye el mensaje y se realiza la escritura.
                message = f'#ETAPA 3: Se obtiene el listado de URLs (cantidad = {len(request_list)}) a utilizar en el request --> request_urls_list() --> Estado:[{status_code_request_list}] --> Mensaje:[{status_message_request_list}] --> {round(time.time() - execution_time_start,4)} seg'
                write_log_message(log,message)
                
                if status_code_request_list == 'OK':

                    #################################################################################################
                    ### ETAPA N°4: Se crean los directorios necesarios para la ejecucion --> create_root_folder() ###
                    #################################################################################################

                    status_code_root_folder,status_message_root_folder,_ = create_root_folder(folder_name_list)

                    #log - Se contruye el mensaje y se realiza la escritura.
                    message = f'#ETAPA 4: Se crean los directorios {folder_name_list} necesarios para la ejecucion --> create_root_folder() --> Estado:[{status_code_root_folder}] --> Mensaje:[{status_message_root_folder}] --> {round(time.time() - execution_time_start,4)} seg'
                    write_log_message(log,message)
                    
                    if status_code_root_folder == 'OK':

                        #########################################################################################################
                        ### ETAPA N°5: Se incorpora en un diccionario los directorios creados en ETAPA N°4 --> dict_folders() ###
                        #########################################################################################################

                        status_code_dict_folders,status_message_dict_folders,dict_folder_list = dict_folders(folder_name_list)

                        #log - Se contruye el mensaje y se realiza la escritura.
                        message = f'#ETAPA 5: Se crea un diccionario con los directorios creados en ETAPA 4 --> dict_folders() --> Estado:[{status_code_dict_folders}] --> Mensaje:[{status_message_dict_folders}] --> {round(time.time() - execution_time_start,4)} seg'
                        write_log_message(log,message)
                        
                        if status_code_dict_folders == 'OK':

                            ########################################################################################################
                            ### ETAPA N°6: Se crea el directorio donde se almacenan las imagenes descargadas --> create_folder() ###
                            ########################################################################################################

                            name_folder = f'{time_now}_{short_name}_{version}_{start_date}_{end_date}'
                            origin_folder = dict_folder_list['path_OUTPUT']
                            status_code_create_folder,status_message_create_folder,destination_folder = create_folder(origin_folder,name_folder)

                            #log - Se contruye el mensaje y se realiza la escritura.
                            message = f'#ETAPA 6: Se crea el directorio [{name_folder}] dentro del directorio [{origin_folder}] donde se almacena la salida del proceso --> create_folder() --> Estado:[{status_code_create_folder}] --> Mensaje:[{status_message_create_folder}] --> {round(time.time() - execution_time_start,4)} seg'
                            write_log_message(log,message)

                            if status_code_create_folder == 'OK':

                                ###################################################################################################
                                ### ETAPA N°7 - Se realiza el Request al microservicio (API) de EARTHDATA --> execute_request() ###
                                ###################################################################################################

                                destination_path = dict_folder_list['path_TMP']
                                status_code_execute_request_list = []
                                
                                #Se realiza el Request a todas las URL's listadas
                                for indice_url,url in enumerate(request_list):
                                    status_code_execute_request,status_message_execute_request,_ = execute_request(username,password,url,destination_path,num_retries,http_status_list)
                                    #Se incorpora el status del response para check posterior sobre la totalidad de los Request realizados
                                    status_code_execute_request_list.append(status_code_execute_request)
                                    #log - Se contruye el mensaje y se realiza la escritura.
                                    message = f'#ETAPA 7-{indice_url+1}: Se realiza el request a [{url}] y el resultado se guarda en [{destination_path}] --> execute_request() --> Estado:[{status_code_execute_request}] --> Mensaje:[{status_message_execute_request}] --> {round(time.time() - execution_time_start,4)} seg'
                                    write_log_message(log,message)

                                list_unique_values = list(set(status_code_execute_request_list))
                                if (len(list_unique_values) == 1) and (list_unique_values[0] == 'OK'):

                                    #####################################################################################
                                    ### ETAPA N°8: Se descomprimen las imagenes obtenidas en la ETAPA N°7 --> unzip() ###
                                    #####################################################################################

                                    status_code_unzip,status_message_unzip,_ = unzip(dict_folder_list['path_TMP'])

                                    #log - Se contruye el mensaje y se realiza la escritura.
                                    message = f'#ETAPA 8: Se descomprimen las imagenes obtenidas en la ETAPA 7 que se guardaron en [{destination_path}] --> unzip() --> Estado:[{status_code_unzip}] --> Mensaje:[{status_message_unzip}] --> {round(time.time() - execution_time_start,4)} seg'
                                    write_log_message(log,message)

                                    if status_code_unzip == 'OK':

                                        ####################################################################################
                                        ### ETAPA N°9: Se mueven las imagenes al directorio definitivo --> move_images() ###
                                        ####################################################################################

                                        status_code_move_images,status_message_move_images,_ = move_images(dict_folder_list['path_TMP'],destination_folder)

                                        #log - Se contruye el mensaje y se realiza la escritura.
                                        message = f'#ETAPA 9: Se mueven las imagenes desde [{origin_folder}] a [{destination_folder}] --> move_images() --> Estado:[{status_code_move_images}] --> Mensaje:[{status_message_move_images}] --> {round(time.time() - execution_time_start,4)} seg'
                                        write_log_message(log,message)

                                        if status_code_move_images == 'OK':

                                            ##################################################################################################
                                            ### ETAPA N°10: Se elimina el directorio TMP utilizando durante el proceso --> delete_folder() ###
                                            ##################################################################################################

                                            status_code_delete_folder,status_message_delete_folder,_ = delete_folder(dict_folder_list['path_TMP'])

                                            #log - Se contruye el mensaje y se realiza la escritura.
                                            message = f'#ETAPA 10: Se elimina el directorio [{destination_path}] --> delete_folder() --> Estado:[{status_code_delete_folder}] --> Mensaje:[{status_message_delete_folder}] --> {round(time.time() - execution_time_start,4)} seg'
                                            write_log_message(log,message)

                                            if status_code_delete_folder == 'OK':

                                                ################################################################################################################################
                                                ### ETAPA N°11: Se chequea la cantidad de imagenes obtenidas con respecto a la cantidad teorica --> check_execution_result() ###
                                                ################################################################################################################################

                                                status_code_check_execution,status_message_check_execution,_ = check_execution_result(destination_folder,start_date,end_date,coverages)

                                                message = f'#ETAPA 11: Se chequea la cantidad de imagenes obtenidas con respecto a la cantidad teorica --> check_execution_result() --> Estado:[{status_code_check_execution}] --> Mensaje:[{status_message_check_execution}] --> {round(time.time() - execution_time_start,4)} seg'
                                                write_log_message(log,message)

                                                #log - Se contruye el mensaje y se realiza la escritura.
                                                if status_code_check_execution == 'OK':

                                                    #log - Se contruye el mensaje y se realiza la escritura que da cierre a la ejecucion
                                                    message = f'#SE DA POR FINALIZADO EL PROCESO! --> Las imagenes se encuentran en [{destination_folder}] --> {round(time.time() - execution_time_start,4)} seg'
                                                    write_log_message(log,message)
                                                    log.close()

                                                    return status_code_check_execution

                                                else:
                                                    #log - Se contruye el mensaje y se realiza la escritura.
                                                    write_error_log_message(log)
                                                    return status_code_check_execution
                        
                                            else:
                                                #log - Se contruye el mensaje y se realiza la escritura.
                                                write_error_log_message(log)
                                                return status_code_delete_folder
                                            
                                        else:
                                            #log - Se contruye el mensaje y se realiza la escritura.
                                            write_error_log_message(log)
                                            return status_code_move_images

                                    else:
                                        #log - Se contruye el mensaje y se realiza la escritura.
                                        write_error_log_message(log)
                                        return status_code_unzip
                                    
                                else:
                                    #log - Se contruye el mensaje y se realiza la escritura.
                                    write_error_log_message(log)
                                    return 'NOK'

                            else:
                                #log - Se contruye el mensaje y se realiza la escritura.
                                write_error_log_message(log)
                                return status_code_create_folder

                        else:
                            #log - Se contruye el mensaje y se realiza la escritura.
                            write_error_log_message(log)
                            return status_code_dict_folders
                        
                    else:
                        #log - Se contruye el mensaje y se realiza la escritura.
                        write_error_log_message(log)
                        return status_code_root_folder
                    
                else:
                    #log - Se contruye el mensaje y se realiza la escritura.
                    write_error_log_message(log)
                    return status_code_request_list
                
            else:
                #log - Se contruye el mensaje y se realiza la escritura.
                write_error_log_message(log)
                return status_code_time
            
        else:
            #log - Se contruye el mensaje y se realiza la escritura.
            status_code_load_secrets = 'NOK'
            status_message_load_secrets = 'load_secrets() --> Error: No fue posible leer los secretos para acceder al microservicio (API) de EARTHDATA'
            message = f'#ETAPA N°1: Se cargan los secretos para realizar la conexion al microservicio (API) de EARTHDATA --> load_secrets() --> Estado:[{status_code_load_secrets}] --> Mensaje:[{status_message_load_secrets}] --> {round(time.time() - execution_time_start,4)} seg'
            write_log_message(log,message)
            write_error_log_message(log)
            return status_code_load_secrets
        
    else:
        return status_code_log_file