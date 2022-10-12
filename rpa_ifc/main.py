

import os
from descarga_ifc import *

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)).rsplit(os.sep, 1)[0]+"\ifc"
ruta=str(ROOT_DIR)

#Procesos =['BADX', 'BAEN', 'EFAC','FETR','PJDX','PMGD','RCUT']

Procesos =['BAEN', 'EFAC','FETR','PJDX','PMGD','RCUT']

#print(ruta)

#for mes in range(1,13):
#    descarga('PJDX',mes,2022,ruta)
for  proceso in Procesos:
    for mes in range(1,13):
        descarga(proceso,mes,2022,ruta)
#for mes in range(1,13):
#    descarga('BAEN',mes,2022,ruta)

#for mes in range(4,10):
#    descarga('PJDX',mes,2022,ruta)
