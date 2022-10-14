import json
import requests
import urllib3
import pandas as pd

Canales="https://medidas.api.coordinador.cl/medidas/api/canales/?user_key=2f0f565217dcdd994ad5f0b262d23919"
Coordinados="https://medidas.api.coordinador.cl:443/medidas/api/coordinados/?user_key=2f0f565217dcdd994ad5f0b262d23919"
Medidas="https://medidas.api.coordinador.cl:443/medidas/api/medidas/:fecha/?idCanal=1&idPuntoMedida=idpuntomedida&user_key=2f0f565217dcdd994ad5f0b262d23919"
Punto_medidas="https://medidas.api.coordinador.cl:443/medidas/api/puntomedidas/:idcoordinado?user_key=2f0f565217dcdd994ad5f0b262d23919"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
response = requests.get(Canales, verify=False).text

response_info = json.loads(response)
#print(response_info)

canales_list=[]

for idcanalm in response_info:
    canales_list.append([idcanalm['idCanal'],idcanalm['slug'],idcanalm['descripcion']])

#print(canales_list)

#canales_df = pd.DataFrame(index=str(canales_list['idCanal']),data=canales_list, columns=['unidad_de_medida','descripcion'])

canales_df=pd.DataFrame(canales_list, columns=['idCanal','unidad_de_medida','descripcion']).set_index('idCanal')


#print(canales_df)
#print(canales_df['unidad_de_medida'])

canal_directo=str(canales_df.index[canales_df['unidad_de_medida'] == 'kWhD'][0])
canal_reverso=str(canales_df.index[canales_df['unidad_de_medida'] == 'kWhR'][0])

print(canal_reverso)
print(canal_directo)