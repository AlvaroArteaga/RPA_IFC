import json
import requests
import urllib3
import pandas as pd
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
medidas="https://medidas.api.coordinador.cl/medidas/api/medidas/202209/?idCanal=1&idPuntoMedida=CLROMERO_220_J1_AEC&user_key=2f0f565217dcdd994ad5f0b262d23919"

medidas_rq= requests.get(medidas, verify=False).text
medidas_dict= json.loads(medidas_rq)

points=medidas_dict[0]["mediciones"]

medidas_list=[]
for y in points:
  
    if y['principal']:
        medidas_list.append([y['intervalo'],y['intervaloUtc'],y['canalVal1']])

Punto_medidas_df = pd.DataFrame(data=medidas_list, columns=['intervalo','intervaloUtc','CLROMERO_220_J1_AEC_canal1'])  

#print(medidas_list)
Punto_medidas_df.to_excel('mediciones2.xlsx', index=False)
#x=filter(lambda c: c[][2] =='true', points)

#x=filter(lambda p: p.principal == 'true', points)
#print(medidas_dict[0]["mediciones"][0])
#filtered = [project for project in projects if project.repo == "repo1"]
#x=[point for point in points if point.principal == 'true']


