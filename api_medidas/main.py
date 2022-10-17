import json
from h11 import Data
import requests
import urllib3
import pandas as pd
from pandas.io.json import json_normalize 
import time

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
canal_directo = canales_list[0]
#canales_df = pd.DataFrame(index=str(canales_list['idCanal']),data=canales_list, columns=['unidad_de_medida','descripcion'])

#canales_df=pd.DataFrame(canales_list, columns=['idCanal','unidad_de_medida','descripcion']).set_index('idCanal')


#print(canales_df)
#print(canales_df['unidad_de_medida'])

#canal_directo=str(canales_df.index[canales_df['unidad_de_medida'] == 'kWhD'][0])
#canal_reverso=str(canales_df.index[canales_df['unidad_de_medida'] == 'kWhR'][0])

#print(canal_reverso)
#print('idCanal: ',canales_list[0][0],' - unidad_de_medida: ',canales_list[0][1],' - descripcion: ',canales_list[0][2])
#print('idCanal: ',canales_list[2][0],' - unidad_de_medida: ',canales_list[2][1],' - descripcion: ',canales_list[2][2])

canal_directo = canales_list[0][0]
canal_reverso = canales_list[2][0]

idCoordinado = requests.get(Coordinados, verify=False).text
idCoordinado_info = json.loads(idCoordinado)
idCoordinado_list=[]
for i in idCoordinado_info:
    idCoordinado_list.append([i['idCoordinado']])

#print(idCoordinado_info)
#print (idCoordinado_list[8])
#print( ", ".join(idCoordinado_list))
#print(*idCoordinado_list, sep = ',')

idCoordinado_df = pd.DataFrame(data=idCoordinado_list, columns=['idCoordinado'])

#canales_df=pd.DataFrame(canales_list, columns=['idCanal','unidad_de_medida','descripcion']).set_index('idCanal')

Punto_medidas_list=[]
for x in range(len(idCoordinado_df)):
    Punto_medidas="https://medidas.api.coordinador.cl:443/medidas/api/puntomedidas/" + str(idCoordinado_df.iloc[x]['idCoordinado']) + "?user_key=2f0f565217dcdd994ad5f0b262d23919"
    #print(Punto_medidas)
    try:
        response2 = requests.get(Punto_medidas, verify=False).text
        response_info2 = json.loads(response2)
        for y in response_info2:
            Punto_medidas_list.append([y['idPuntoMedida'],y['idCoordinado'],y['subestacion'],y['tension'],y['region']])
    except:
        print(Punto_medidas)
    
Punto_medidas_df = pd.DataFrame(data=Punto_medidas_list, columns=['idPuntoMedida','idCoordinado','subestacion','tension','region'])  
#print(Punto_medidas_df)
#Punto_medidas_df.to_excel('Punto_medidas.xlsx', index=False)
ano='2022'
mes='09'
medidas_list=[]
#print('ultiomo es: ',len(Punto_medidas_df))
#print(str(Punto_medidas_df.iloc[0,0]))
#print(str(Punto_medidas_df.iloc[1,0]))
#print(str(Punto_medidas_df.iloc[2,0]))
#print(str(Punto_medidas_df.iloc[3,0]))
#print(str(Punto_medidas_df.iloc[4,0]))
#print(str(Punto_medidas_df.iloc[5,0]))
#time.sleep(30)
#len(Punto_medidas_df)
t=True
h=0
k=0
for z in range(len(Punto_medidas_df)):

    try:
        #print("z:   ", z, "-", type(z))
        punto_m=str(Punto_medidas_df.iloc[z,0])
        #print(punto_m)
        #time.sleep(30)
        Medidas="https://medidas.api.coordinador.cl/medidas/api/medidas/" + ano + mes + "/?idCanal=1&idPuntoMedida=" + punto_m + "&user_key=2f0f565217dcdd994ad5f0b262d23919"
        Medidas_r="https://medidas.api.coordinador.cl/medidas/api/medidas/" + ano + mes + "/?idCanal=3&idPuntoMedida=" + punto_m + "&user_key=2f0f565217dcdd994ad5f0b262d23919"
        
        #print("----------------1----------------")
     
        
        medidas_rq= requests.get(Medidas, verify=False).text
        medidas_rq_r= requests.get(Medidas_r, verify=False).text
        #print("----------------2----------------")
        medidas_dict= json.loads(medidas_rq)
        medidas_dict_r= json.loads(medidas_rq_r)
        #print("----------------3----------------")
        points=medidas_dict[0]["mediciones"]
        points_r=medidas_dict_r[0]["mediciones"]
        #print("----------------4----------------")
        medidas_list=[]
        medidas_list_r=[]
        #print("----------------5----------------")
        for y in points:
            if y['principal']:
                medidas_list.append([y['intervalo'],y['intervaloUtc'],y['canalVal1']])
        medidas_df = pd.DataFrame(data=medidas_list, columns=['intervalo','intervaloUtc', punto_m + '_D'])  
        #print("----------------6----------------")
        for yr in points_r:
            if yr['principal']:
                medidas_list_r.append([yr['intervalo'],yr['intervaloUtc'],yr['canalVal3']])
        medidas_df_r = pd.DataFrame(data=medidas_list_r, columns=['intervalo','intervaloUtc', punto_m + '_R'])  
        
        #print("----------------7----------------")
        if t:
            medidas_mes = medidas_df
            medidas_df_r =medidas_df_r.drop(['intervalo', 'intervaloUtc'], axis=1)
            medidas_mes = pd.concat([medidas_mes,medidas_df_r], axis=1)
            t=False
        else:
            medidas_df=medidas_df.drop(['intervalo', 'intervaloUtc'], axis=1)
            medidas_df_r =medidas_df_r.drop(['intervalo', 'intervaloUtc'], axis=1)
            
            medidas_mes = pd.concat([medidas_mes,medidas_df], axis=1)
            medidas_mes = pd.concat([medidas_mes,medidas_df_r], axis=1)
        #response3 = requests.get(Medidas, verify=False).text
        #response_info3 = json.loads(response3)
        #test_df=pd.json_normalize(data=response_info3,record_path=['mediciones'])
        #for j in response_info3:
        #print("----------------8----------------")
        #    Medidas_list.append([j['idCoordinado'],j['idPuntoMedida'],j['periodo'],j['subEstacion'],j['fechaUltimaLectura'],j['bitacora'],j['medidores'],j['canales'],j['mediciones']])
    except:
        print("error en ---> ", z)
        #print(Medidas)
    h=h+1
    if h == 523:
        h=0
        k=k+1
        medidas_list=[]
        medidas_list_r=[]
        medidas_df=pd.DataFrame(None)
        medidas_df_r=pd.DataFrame(None)
        t=True
        medidas_mes.to_excel('mediciones_'+ str(k)+'.xlsx', index=False)
        medidas_mes=pd.DataFrame(None)
    
    
#Medidas_df= pd.DataFrame(data=Medidas_list, columns=['idCoordinado','idPuntoMedida','periodo','subEstacion','fechaUltimaLectura','bitacora','medidores','canales','mediciones'])
#test_df=pd.json_normalize(Medidas_list,record_path=['canalVal1'])

#mediciones_df=pd.DataFrame(data=Medidas_df['mediciones'],columns=['intervalo','canalVal1'])
medidas_mes.to_excel('mediciones.xlsx', index=False)