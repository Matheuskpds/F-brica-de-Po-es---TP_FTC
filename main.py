import os
from AFD.afd import ler_arquivo
from APD.apd import ler_arquivo_apd
from MOORE.moore import ler_arquivo_moore
from MEALY.mealy import ler_arquivo_mealy


titulo = """
 _____      _                            _                                    _             
/  ___|    | |                          | |                                  (_)            
\ `--.  ___| | ___  ___ __ _  ___     __| | ___   _ __ ___   __ _  __ _ _   _ _ _ __   __ _ 
 `--. \/ _ \ |/ _ \/ __/ _` |/ _ \   / _` |/ _ \ | '_ ` _ \ / _` |/ _` | | | | | '_ \ / _` |
/\__/ /  __/ |  __/ (_| (_| | (_) | | (_| |  __/ | | | | | | (_| | (_| | |_| | | | | | (_| |
\____/ \___|_|\___|\___\__,_|\___/   \__,_|\___| |_| |_| |_|\__,_|\__, |\__,_|_|_| |_|\__,_|
                                                                     | |                    
                                                                     |_|                                                                           
__________________________________________________________________________________________________________________________________________________                                                                          
  ___  _      _ _                        _   _   _                _                            _                _              _         _      _ 
 |   \(_)__ _(_) |_ ___   __ _ _  _ __ _| | | |_(_)_ __  ___   __| |___   _ __  __ _ __ _ _  _(_)_ _  __ _   __| |___ ___ ___ (_)__ _ __| |__ _(_)
 | |) | / _` | |  _/ -_) / _` | || / _` | | |  _| | '_ \/ _ \ / _` / -_) | '  \/ _` / _` | || | | ' \/ _` | / _` / -_|_-</ -_)| / _` / _` / _` |_ 
 |___/|_\__, |_|\__\___| \__, |\_,_\__,_|_|  \__|_| .__/\___/ \__,_\___| |_|_|_\__,_\__, |\_,_|_|_||_\__,_| \__,_\___/__/\___|/ \__,_\__,_\__,_(_)
        |___/               |_|                   |_|                                  |_|                                  |__/

                                
 ___          _____ _____ ____  
|_  |  ___   |  _  |   __|    \ 
 _| |_|___|  |     |   __|  |  |
|_____|      |__|__|__|  |____/ 
                                
                                
 ___        _____ _____ ____    
|_  |___   |  _  |  _  |    \   
|  _|___|  |     |   __|  |  |  
|___|      |__|__|__|  |____/        

                                          
 ___        _____ _____ _____ _____ _____ 
|_  |___   |     |     |     | __  |   __|
|_  |___|  | | | |  |  |  |  |    -|   __|
|___|      |_|_|_|_____|_____|__|__|_____|
                                          
                                          
 ___        _____ _____ _____ __    __ __ 
| | |___   |     |   __|  _  |  |  |  |  |
|_  |___|  | | | |   __|     |  |__|_   _|
  |_|      |_|_|_|_____|__|__|_____| |_|
"""

pocoes_afd = """                                                                                                      
__________________________________________________________________________________________________________________________________________________                                     
 _____ _____ ____      _ 
|  _  |   __|    \ ___|_|
|     |   __|  |  |_ -|_ 
|__|__|__|  |____/|___|_|

 ___          _____                      _        _                                                               
|_  |  ___   |  _  |___ ___ ___ ___    _| |___   | |_ _ ___                                                       
 _| |_|___|  |   __| . |  _| .'| . |  | . | -_|  | | | |- _|                                                      
|_____|      |__|  |___|___|__,|___|  |___|___|  |_|___|___|                                                      
                                                                                                                  
                                                                                                                  
 ___        _____                      _                    _     _               _               ___             
|_  |___   |  _  |___ ___ ___ ___    _| |___    ___ ___ ___|_|___| |_ ___ ___ ___|_|___    ___   |  _|___ ___ ___ 
|  _|___|  |   __| . |  _| .'| . |  | . | -_|  |  _| -_|_ -| |_ -|  _| -_|   |  _| | .'|  | .'|  |  _| . | . | . |
|___|      |__|  |___|___|__,|___|  |___|___|  |_| |___|___|_|___|_| |___|_|_|___|_|__,|  |__,|  |_| |___|_  |___|
                                                                                                         |___|    
                                                                                                                  
 ___        _____                      _                                                                          
|_  |___   |  _  |___ ___ ___ ___    _| |___    ___ _____ ___ ___                                                 
|_  |___|  |   __| . |  _| .'| . |  | . | . |  | .'|     | . |  _|                                                
|___|      |__|  |___|___|__,|___|  |___|___|  |__,|_|_|_|___|_|

"""
pocoes_apd = """
__________________________________________________________________________________________________________________________________________________                                                                                             
 _____ _____ ____      _                                                                        
|  _  |  _  |    \ ___|_|                                                                       
|     |   __|  |  |_ -|_                                                                        
|__|__|__|  |____/|___|_|                                                                       
                                                                                                
                                                                                                
 ___          _____                      _                        _ _   _               _       
|_  |  ___   |  _  |___ ___ ___ ___    _| |___    ___ ___ ___ ___| | |_|_|_____ ___ ___| |_ ___ 
 _| |_|___|  |   __| . |  _| .'| . |  | . | -_|  | -_|   |  _| . | |   | |     | -_|   |  _| . |
|_____|      |__|  |___|___|__,|___|  |___|___|  |___|_|_|___|___|_|_|_|_|_|_|_|___|_|_|_| |___|
                                                                                                
                                                                                                
 ___        _____                      _                                                        
|_  |___   |  _  |___ ___ ___ ___    _| |___    _ _ ___ ___                                     
|  _|___|  |   __| . |  _| .'| . |  | . | -_|  | | | . | . |                                    
|___|      |__|  |___|___|__,|___|  |___|___|   \_/|___|___|
__________________________________________________________________________________________________________________________________________________  
"""
pocoes_moore = """
__________________________________________________________________________________________________________________________________________________                                                                                                                                                                   
 _____ _____ _____ _____ _____ _                                              
|     |     |     | __  |   __|_|                                             
| | | |  |  |  |  |    -|   __|_                                              
|_|_|_|_____|_____|__|__|_____|_|                                             
                                                                              
                                                                              
 ___          _____         _            _                                    
|_  |  ___   |_   _|___ ___| |_ ___    _| |___    ___ ___ ___ ___ ___ ___ ___ 
 _| |_|___|    | | | -_|_ -|  _| -_|  | . | -_|  |  _| -_| .'|  _| . | -_|_ -|
|_____|        |_| |___|___|_| |___|  |___|___|  |_| |___|__,|___|___|___|___|
__________________________________________________________________________________________________________________________________________________  
"""
pocoes_mealy = """
__________________________________________________________________________________________________________________________________________________                                                                                                                                                                                                                                     
 _____ _____ _____ __    __ __ _                                              
|     |   __|  _  |  |  |  |  |_|                                             
| | | |   __|     |  |__|_   _|_                                              
|_|_|_|_____|__|__|_____| |_| |_|                                             
                                                                              
                                                                              
 ___          _____         _            _                                    
|_  |  ___   |_   _|___ ___| |_ ___    _| |___    ___ ___ ___ ___ ___ ___ ___ 
 _| |_|___|    | | | -_|_ -|  _| -_|  | . | -_|  |  _| -_| .'|  _| . | -_|_ -|
|_____|        |_| |___|___|_| |___|  |___|___|  |_| |___|__,|___|___|___|___|
__________________________________________________________________________________________________________________________________________________  
"""

erro = """
__________________________________________________________________________________________________________________________________________________  
                                                                                 __ 
 _____             _                                   _     _           _      |  |
|     |___ ___ _ _|_|___ ___    ___ ___ ___    ___ _ _|_|___| |_ ___ ___| |_ ___|  |
| | | | .'| . | | | |   | .'|  |   | .'| . |  | -_|_'_| |_ -|  _| -_|   |  _| -_|__|
|_|_|_|__,|_  |___|_|_|_|__,|  |_|_|__,|___|  |___|_,_|_|___|_| |___|_|_|_| |___|__|
            |_|
__________________________________________________________________________________________________________________________________________________  
"""
pocao_concluida = """
__________________________________________________________________________________________________________________________________________________
                                                                                                          __ 
 _____                                    _     _   _                                                    |  |
|  _  |___ ___ ___ ___    ___ ___ ___ ___| |_ _|_|_| |___    ___ ___ _____    ___ _ _ ___ ___ ___ ___ ___|  |
|   __| . |  _| .'| . |  |  _| . |   |  _| | | | | . | .'|  |  _| . |     |  |_ -| | |  _| -_|_ -|_ -| . |__|
|__|  |___|___|__,|___|  |___|___|_|_|___|_|___|_|___|__,|  |___|___|_|_|_|  |___|___|___|___|___|___|___|__|
__________________________________________________________________________________________________________________________________________________
"""
pocao_errada = """
__________________________________________________________________________________________________________________________________________________
                                                     __ 
 _____                                              |  |
|   __|___ ___ ___    ___ ___    ___ ___ ___ ___ ___|  |
|   __|  _|  _| . |  |   | .'|  | . | . |  _| .'| . |__|
|_____|_| |_| |___|  |_|_|__,|  |  _|___|___|__,|___|__|
                                |_|
__________________________________________________________________________________________________________________________________________________
"""


titulo = """
 _____      _                            _                                    _             
/  ___|    | |                          | |                                  (_)            
\ `--.  ___| | ___  ___ __ _  ___     __| | ___   _ __ ___   __ _  __ _ _   _ _ _ __   __ _ 
 `--. \/ _ \ |/ _ \/ __/ _` |/ _ \   / _` |/ _ \ | '_ ` _ \ / _` |/ _` | | | | | '_ \ / _` |
/\__/ /  __/ |  __/ (_| (_| | (_) | | (_| |  __/ | | | | | | (_| | (_| | |_| | | | | | (_| |
\____/ \___|_|\___|\___\__,_|\___/   \__,_|\___| |_| |_| |_|\__,_|\__, |\__,_|_|_| |_|\__,_|
                                                                     | |                    
                                                                     |_|                                                                           
__________________________________________________________________________________________________________________________________________________                                                                          
  ___  _      _ _                        _   _   _                _                            _                _              _         _      _ 
 |   \(_)__ _(_) |_ ___   __ _ _  _ __ _| | | |_(_)_ __  ___   __| |___   _ __  __ _ __ _ _  _(_)_ _  __ _   __| |___ ___ ___ (_)__ _ __| |__ _(_)
 | |) | / _` | |  _/ -_) / _` | || / _` | | |  _| | '_ \/ _ \ / _` / -_) | '  \/ _` / _` | || | | ' \/ _` | / _` / -_|_-</ -_)| / _` / _` / _` |_ 
 |___/|_\__, |_|\__\___| \__, |\_,_\__,_|_|  \__|_| .__/\___/ \__,_\___| |_|_|_\__,_\__, |\_,_|_|_||_\__,_| \__,_\___/__/\___|/ \__,_\__,_\__,_(_)
        |___/               |_|                   |_|                                  |_|                                  |__/

                                
 ___          _____ _____ ____  
|_  |  ___   |  _  |   __|    \ 
 _| |_|___|  |     |   __|  |  |
|_____|      |__|__|__|  |____/ 
                                
                                
 ___        _____ _____ ____    
|_  |___   |  _  |  _  |    \   
|  _|___|  |     |   __|  |  |  
|___|      |__|__|__|  |____/        

                                          
 ___        _____ _____ _____ _____ _____ 
|_  |___   |     |     |     | __  |   __|
|_  |___|  | | | |  |  |  |  |    -|   __|
|___|      |_|_|_|_____|_____|__|__|_____|
                                          
                                          
 ___        _____ _____ _____ __    __ __ 
| | |___   |     |   __|  _  |  |  |  |  |
|_  |___|  | | | |   __|     |  |__|_   _|
  |_|      |_|_|_|_____|__|__|_____| |_|
"""

pocoes_afd = """                                                                                                      
__________________________________________________________________________________________________________________________________________________                                     
 _____ _____ ____      _ 
|  _  |   __|    \ ___|_|
|     |   __|  |  |_ -|_ 
|__|__|__|  |____/|___|_|

 ___          _____                      _        _                                                               
|_  |  ___   |  _  |___ ___ ___ ___    _| |___   | |_ _ ___                                                       
 _| |_|___|  |   __| . |  _| .'| . |  | . | -_|  | | | |- _|                                                      
|_____|      |__|  |___|___|__,|___|  |___|___|  |_|___|___|                                                      
                                                                                                                  
                                                                                                                  
 ___        _____                      _                    _     _               _               ___             
|_  |___   |  _  |___ ___ ___ ___    _| |___    ___ ___ ___|_|___| |_ ___ ___ ___|_|___    ___   |  _|___ ___ ___ 
|  _|___|  |   __| . |  _| .'| . |  | . | -_|  |  _| -_|_ -| |_ -|  _| -_|   |  _| | .'|  | .'|  |  _| . | . | . |
|___|      |__|  |___|___|__,|___|  |___|___|  |_| |___|___|_|___|_| |___|_|_|___|_|__,|  |__,|  |_| |___|_  |___|
                                                                                                         |___|    
                                                                                                                  
 ___        _____                      _                                                                          
|_  |___   |  _  |___ ___ ___ ___    _| |___    ___ _____ ___ ___                                                 
|_  |___|  |   __| . |  _| .'| . |  | . | . |  | .'|     | . |  _|                                                
|___|      |__|  |___|___|__,|___|  |___|___|  |__,|_|_|_|___|_|

"""
pocoes_apd = """
__________________________________________________________________________________________________________________________________________________                                                                                             
 _____ _____ ____      _                                                                        
|  _  |  _  |    \ ___|_|                                                                       
|     |   __|  |  |_ -|_                                                                        
|__|__|__|  |____/|___|_|                                                                       
                                                                                                
                                                                                                
 ___          _____                      _                        _ _   _               _       
|_  |  ___   |  _  |___ ___ ___ ___    _| |___    ___ ___ ___ ___| | |_|_|_____ ___ ___| |_ ___ 
 _| |_|___|  |   __| . |  _| .'| . |  | . | -_|  | -_|   |  _| . | |   | |     | -_|   |  _| . |
|_____|      |__|  |___|___|__,|___|  |___|___|  |___|_|_|___|___|_|_|_|_|_|_|_|___|_|_|_| |___|
                                                                                                
                                                                                                
 ___        _____                      _                                                        
|_  |___   |  _  |___ ___ ___ ___    _| |___    _ _ ___ ___                                     
|  _|___|  |   __| . |  _| .'| . |  | . | -_|  | | | . | . |                                    
|___|      |__|  |___|___|__,|___|  |___|___|   \_/|___|___|
__________________________________________________________________________________________________________________________________________________  
"""
pocoes_moore = """
__________________________________________________________________________________________________________________________________________________                                                                                                                                                                   
 _____ _____ _____ _____ _____ _                                              
|     |     |     | __  |   __|_|                                             
| | | |  |  |  |  |    -|   __|_                                              
|_|_|_|_____|_____|__|__|_____|_|                                             
                                                                              
                                                                              
 ___          _____         _            _                                    
|_  |  ___   |_   _|___ ___| |_ ___    _| |___    ___ ___ ___ ___ ___ ___ ___ 
 _| |_|___|    | | | -_|_ -|  _| -_|  | . | -_|  |  _| -_| .'|  _| . | -_|_ -|
|_____|        |_| |___|___|_| |___|  |___|___|  |_| |___|__,|___|___|___|___|
__________________________________________________________________________________________________________________________________________________  
"""
pocoes_mealy = """
__________________________________________________________________________________________________________________________________________________                                                                                                                                                                                                                                     
 _____ _____ _____ __    __ __ _                                              
|     |   __|  _  |  |  |  |  |_|                                             
| | | |   __|     |  |__|_   _|_                                              
|_|_|_|_____|__|__|_____| |_| |_|                                             
                                                                              
                                                                              
 ___          _____         _            _                                    
|_  |  ___   |_   _|___ ___| |_ ___    _| |___    ___ ___ ___ ___ ___ ___ ___ 
 _| |_|___|    | | | -_|_ -|  _| -_|  | . | -_|  |  _| -_| .'|  _| . | -_|_ -|
|_____|        |_| |___|___|_| |___|  |___|___|  |_| |___|__,|___|___|___|___|
__________________________________________________________________________________________________________________________________________________  
"""

erro = """
__________________________________________________________________________________________________________________________________________________  
                                                                                 __ 
 _____             _                                   _     _           _      |  |
|     |___ ___ _ _|_|___ ___    ___ ___ ___    ___ _ _|_|___| |_ ___ ___| |_ ___|  |
| | | | .'| . | | | |   | .'|  |   | .'| . |  | -_|_'_| |_ -|  _| -_|   |  _| -_|__|
|_|_|_|__,|_  |___|_|_|_|__,|  |_|_|__,|___|  |___|_,_|_|___|_| |___|_|_|_| |___|__|
            |_|
__________________________________________________________________________________________________________________________________________________  
"""
pocao_concluida = """
__________________________________________________________________________________________________________________________________________________
                                                                                                          __ 
 _____                                    _     _   _                                                    |  |
|  _  |___ ___ ___ ___    ___ ___ ___ ___| |_ _|_|_| |___    ___ ___ _____    ___ _ _ ___ ___ ___ ___ ___|  |
|   __| . |  _| .'| . |  |  _| . |   |  _| | | | | . | .'|  |  _| . |     |  |_ -| | |  _| -_|_ -|_ -| . |__|
|__|  |___|___|__,|___|  |___|___|_|_|___|_|___|_|___|__,|  |___|___|_|_|_|  |___|___|___|___|___|___|___|__|
__________________________________________________________________________________________________________________________________________________
"""
pocao_errada = """
__________________________________________________________________________________________________________________________________________________
                                                     __ 
 _____                                              |  |
|   __|___ ___ ___    ___ ___    ___ ___ ___ ___ ___|  |
|   __|  _|  _| . |  |   | .'|  | . | . |  _| .'| . |__|
|_____|_| |_| |___|  |_|_|__,|  |  _|___|___|__,|___|__|
                                |_|
__________________________________________________________________________________________________________________________________________________
"""

def menu():
    loop_menu = 1
    while loop_menu == 1:
        os.system('cls')
        print(titulo)
        maquina = int(input())

        if(maquina == 1): 
            print(pocoes_afd)
            pocao = int(input())
            if(pocao == 1):
                caminho = "AFD/maquina1.txt"
            elif(pocao == 2):
                caminho = "AFD/maquina2.txt"
            elif(pocao == 3):
                caminho = "AFD/maquina3.txt"
            else:
                print(erro)
            
            afd = ler_arquivo(caminho)
            if afd.processar_input(caminho):
                print(pocao_concluida)
            else:
                print(pocao_errada)

        elif(maquina == 2):
            print(pocoes_apd)
            pocao = int(input())
            if(pocao == 1):
                caminho = "APD/maquina_APD1.txt"
            elif(pocao == 2):
                caminho = "APD/maquina_APD2.txt"
            else:
                print(erro)
            
            apd = ler_arquivo_apd(caminho)
            if apd.processar_input_apd(caminho):
                print(pocao_concluida)
            else:
                print(pocao_errada)
        elif(maquina == 3):
            print(pocoes_moore)
            pocao = int(input())
            if(pocao == 1):
                caminho = "MOORE/moore.txt"
            else:
                print(erro)
            moore = ler_arquivo_moore(caminho)

            moore.processar_input_moore()
        elif(maquina == 4):
            print(pocoes_mealy)
            pocao = int(input())
            if(pocao == 1):
                caminho = "MEALY/mealy.txt"
            else:
                print(erro)
            mealy = ler_arquivo_mealy(caminho)


            mealy.processar_input_mealy()

        print("Deseja continuar? 1 - Sim | 0 - Não")
        loop_menu = int(input())
menu()