

import os
from descarga_ifc import *

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)).rsplit(os.sep, 1)[0]+"\ifc"
ruta=str(ROOT_DIR)
print(ruta)

descarga('PJDX',1,2022,ruta)

#for mes in range(4,10):
#    descarga('PJDX',mes,2022,ruta)
