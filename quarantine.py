import pandas as pd
import socket
import platform
import subprocess

file_path='Quarantine_List.xlsx'
data=pd.read_excel(file_path)
data=data.fillna('')
user_start=input('Automatic(A) or Manual(M): ')
match_found = False
if user_start == 'M':
 user_input = input("enter the value of PDB GPU OR SWB Manually: ")
   # Check if the input is a string or numeric value
 if user_input.replace('.', '', 1).isdigit():  # Check if input is numeric
       user_input_num = float(user_input)
       search_value = user_input_num
 else:
       user_input_str = user_input
       search_value = user_input_str
   # Search for a match across all cells

 for row_index, row in data.iterrows():
       for col_index, value in row.items():
           if isinstance(search_value, float) and isinstance(value, (int, float)) and value == search_value:
               match_found = True
               break
           elif isinstance(search_value, str) and str(value) == search_value:
               match_found = True
               break
       if match_found:
           break
elif user_start=='A':
    print('this is automatic')
    hostname=socket.gethostname()
    output=subprocess.check_output(['uname', '-a'], universal_newlines=True)
    ip_addr = socket.gethostbyname(hostname)
    system=platform.system()
    release=platform.release()
    version=platform.version()
    print(f'hostname:{hostname}')
    print(f'ip_addr: {ip_addr}')
    print(f'system: {system}')
    print(f'release: {release}')
    print(f'version: {version}')
    print(f'output:{output}')
    

        
if match_found:
    print('\033[91mMatch found!!!!!!!!!!! shut down server and replace \033[0m ' + '' +  user_input)
    print(user_input)
    
else:
    print('\033[92mNo match found. for GPU\033[0m' )
    print('\033[92mNo match found. for SWB\033[0m' )
    print('\033[92mNo match found. for PDB\033[0m' )