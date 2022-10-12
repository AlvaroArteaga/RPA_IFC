from sre_constants import AT_NON_BOUNDARY
import pandas as pd
import glob
from pandas import ExcelWriter

hoja1='1_Cobro_Peajes'
hoja2='2_Pago_Peajes'
hoja3='3_Cambio_Regimen'
# getting excel files to be merged from the Desktop 
#mes='Abril'
ano='2022'
#mes='Mayo'
#mes='Junio'
#mes='Julio'
#mes='Agosto'
ruta = "E:\GitHub\RPA_IFC\ifc"
#ruta = "E:\GitHub\RPA_IFC\ifc"
#print(ruta)
# read all the files with extension .xlsx i.e. excel 
archivos = glob.glob(ruta + "\*.xlsx")
#print('Archivos excel:', archivos)

# marco de datos vacío para el nuevo archivo de salida de Excel con los archivos de Excel combinados
#outputxlsx = pd.DataFrame()

# for loop to iterate all excel files
#for file in archivos:
   # using concat for excel files
   # after reading them with read_excel()
  # df = pd.concat(pd.read_excel( file, sheet_name=None), ignore_index=True, sort=False)

   # appending data of excel files
 #  outputxlsx = outputxlsx.append( df, ignore_index=True)

#print('Final Excel sheet now generated at the same location:')
#outputxlsx.to_excel("C:/Users/amit_/Desktop/Output.xlsx", index=False)

## Method 2 gets all sheets of a given file
df1_total = pd.DataFrame()
df2_total = pd.DataFrame()
df3_total = pd.DataFrame()
for file in archivos:                         # loop through Excel files
    if file.endswith('.xlsx'):
        excel_file = pd.ExcelFile(file)
        sheets = excel_file.sheet_names         # loop through sheets inside an Excel file
        
        #df1 = excel_file.parse(sheet_name = hoja1)
        #Read all data and do not skip any row:
        #df1 = pd.read_excel(file, sheet_name=hoja1)
        #Find index of first row with 'No." in the first column and take everything till the end:
        #df1 = df1.iloc[df1[df1.iloc[:, 0].eq('Id_Cliente')].index[0]:, :].reset_index(drop=True)
        #Set first row as columns:

        #df1.columns = df1.iloc[0]
        #Drop first row (we do not need it because there are column names repeated there):
        # data  = data.replace('', np.nan).dropna()
        #df1['ifc_mes']=mes
        #df1['ifc_año']=ano
        #df1 = df1.drop(0).reset_index(drop=True)
        #df1.dropna()
        df1 = excel_file.parse(sheet_name = hoja1, header=0)
        df1_total = df1_total.append(df1)
        
        df2 = excel_file.parse(sheet_name = hoja2, header=0)
        df2.rename({'Id_Cliente': 'N°Cliente'}, axis=1)

        #df2['ifc_mes']=mes
        #df2['ifc_año']=ano
        
        df2_total = df2_total.append(df2)
        
        df3 = excel_file.parse(sheet_name = hoja3, header=0)
        
        #df3['ifc_mes']=mes
        #df3['ifc_año']=ano
        
        
        df3_total = df3_total.append(df3)
        #df_total.to_excel('combined_file.xlsx')

        #nan_value = float("NaN") 
        #df1_total.replace("", nan_value, inplace=True) 
        #df1_total.dropna(how='all', axis=1, inplace=True)
        #df2_total.replace("", nan_value, inplace=True) 
        #df2_total.dropna(how='all', axis=1, inplace=True)
        #df3_total.replace("", nan_value, inplace=True) 
        #df3_total.dropna(how='all', axis=1, inplace=True)
dict_Distribuidor = {"FRONTEL" : 'Empresa Eléctrica de la Frontera S.A.',
"LUZ OSORNO" : 'Compañía Eléctrica de Osorno S.A',
"SAESA" : 'Sociedad Austral de Electricidad S.A.',
"COELCHA" : 'Cooperativa Eléctrica Charrúa Ltda.',
"cooperativa_de_consumo_de_energia_electrica_chillan_ltda." : 'Cooperativa de Consumo de Energía Eléctrica Chillán Ltda.'
}
df1_total["Distribuidor"]=df1_total['Distribuidor'].map(dict_Distribuidor).fillna(df1_total['Distribuidor'])

dict_RUT_Distribuidor={"76073164-1" : '76.073.164-1',
"96531500-4" : '96.531.500-4',
"76073162-5" : '76.073.162-5',
"80237700-2" : '80.237.700-2',
"80.237.700-3" : '80.237.700-2',
"80.237.700-4" : '80.237.700-2'
}
df1_total["RUT Distribuidor"]=df1_total['RUT Distribuidor'].map(dict_RUT_Distribuidor).fillna(df1_total['RUT Distribuidor'])


dict_Suministrador={    " ENEL GENERACIÓN CHILE S.A" : 'Enel Generación Chile S.A.',
" ENGIE ENERGIA CHILE S.A." : 'Engie Energía Chile S.A.',
"76.208.888-6" : 'EMOAC SpA',
"76.418.918-3" : 'Guacolda Energía SpA',
"76.472.262-0" : 'Imelsa Energía SpA',
"77.285.492-7" : 'Cinergia Chile SpA',
"77.302.440-5" : 'TecnoRed S.A.',
"77.333.033-6" : 'Acierta Energía SpA',
"91.081.000-6" : 'Enel Generación Chile S.A.',
"94.272.000-9" : 'AES Andes S.A.',
"96.505.760-9" : 'Colbún S.A.',
"ACCIONA ENERGIA CHILE HOLDING S.A." : 'Acciona Energía Chile Holdings S.A.',
"ACCIONA ENERGIA CHILE HOLDINGS S.A." : 'Acciona Energía Chile Holdings S.A.',
"ACIERTA ENERGIA SPA" : 'Acierta Energía SpA',
"Acierta Energía SpA" : 'Energy Asset SpA',
"ACIERTA ENERGIA SPA ." : 'Acierta Energía SpA',
"ACIERTA ENERGIA SPSA" : 'Acierta Energía SpA',
"AES ANDES S.A." : 'AES Andes S.A.',
"AES GENER S.A" : 'AES Andes S.A.',
"AES GENER S.A." : 'AES Andes S.A.',
"aes_andes_s.a." : 'AES Andes S.A.',
"ANTUKO GENERACIÓN S.A." : 'Antuko Generación S.A.',
"ARAUCO BIOENERGÍA S.A." : 'Arauco Bioenergía S.A.',
"ATRIA ENERGIA SPA" : 'Atria Energía SpA',
"BESALCO ENERGIA RENOVABLE S.A." : 'Besalco Energía Renovable S.A.',
"BIOENERGIAS FORESTALES SPA" : 'Bioenergías Forestales SpA',
"CAREN" : 'Empresa Eléctrica Carén S.A.',
"Cerro Dominador CSP S.A" : 'Cerro Dominador CSP S.A.',
"CERRO DOMINADOR CSP S.A." : 'Cerro Dominador CSP S.A.',
"cerro_dominador_csp_s.a." : 'Cerro Dominador CSP S.A.',
"CGE COMERCIALIZADORA SPA" : 'CGE Comercializadora SpA',
"CHILQUINTA ENERGIA S.A." : 'Chilquinta Distribución S.A.',
"Chilquinta Energía S.A." : 'Chilquinta Distribución S.A.',
"CINERGIA CHILE SPA" : 'Cinergia Chile SpA',
"COCHRANE" : 'Empresa Eléctrica Cochrane SpA',
"COLBUN" : 'Colbún S.A.',
"COLBUN S. A." : 'Colbún S.A.',
"COLBUN S.A" : 'Colbún S.A.',
"Colbún S.A" : 'Colbún S.A.',
"COLBUN S.A." : 'Colbún S.A.',
"COLBUN_GENERACION" : 'Colbún S.A.',
"colbun_s.a." : 'Colbún S.A.',
"COOP REG ELECTRICA LLANQUIHUE LTDA." : 'Cooperativa Regional Eléctrica Llanquihue Ltda',
"Cooperativa Eléctrica Los Angeles LTDA" : 'Cooperativa Eléctrica Los Angeles LTDA',
"cooperativa_de_consumo_de_energia_electrica_chillan_ltda." : 'Cooperativa de Consumo de Energía Eléctrica Chillán Ltda.',
"CRELL" : 'Cooperativa Regional Eléctrica Llanquihue Ltda',
"DUQUECO SPA" : 'Duqueco SpA',
"ECOM GENERACION SPA" : 'ECOM Generación SpA',
"ECOM GENERACION SPA ." : 'ECOM Generación SpA',
"ecom_generacion_spa" : 'ECOM Generación SpA',
"ELECTRICA NUEVA ENERGIA S.A." : 'Eléctrica Nueva Energía S.A.',
"EMBALSE ANCOA" : 'Hidroeléctrica Embalse Ancoa SpA',
"EMOAC SPA" : 'EMOAC SpA',
"EMOAC SPA." : 'EMOAC SpA',
"emoac_spa" : 'EMOAC SpA',
"EMPRESA ELECTRICA RUCATAYO S.A." : 'Empresa Eléctrica Rucatayo S.A.',
"EMPRESA ELÉCTRICA RUCATAYO S.A." : 'Empresa Eléctrica Rucatayo S.A.',
"EMPRESA ELELCTRICA CAREN S.A." : 'Empresa Eléctrica Carén S.A.',
"empresa_electrica_caren_s.a." : 'Empresa Eléctrica Carén S.A.',
"EMPRESAS LIPIGAS S A" : 'Empresas Lipigas S.A.',
"EMPRESAS LIPIGAS S.A." : 'Empresas Lipigas S.A.',
"ENEL DISTRIBUCION CHILE S.A." : 'Enel Distribución Chile S.A.',
"ENEL DISTRIBUCIÓN CHILE S.A." : 'Enel Distribución Chile S.A.',
"ENEL GENERACION  CHILE S.A. " : 'Enel Generación Chile S.A.',
"ENEL GENERACION CHILE" : 'Enel Generación Chile S.A.',
"ENEL GENERACION CHILE S.A" : 'Enel Generación Chile S.A.',
"ENEL GENERACIÓN CHILE S.A" : 'Enel Generación Chile S.A.',
"ENEL GENERACION CHILE S.A." : 'Enel Generación Chile S.A.',
"ENEL_GENERACION" : 'Enel Generación Chile S.A.',
"enel_generacion_chile_s.a." : 'Enel Generación Chile S.A.',
"ENERGIA COYANCO" : 'Energía Coyanco S.A.',
"ENERGIA COYANCO S.A" : 'Energía Coyanco S.A.',
"ENERGIA COYANCO S.A." : 'Energía Coyanco S.A.',
"ENERGIA LEON S.A." : 'Parque Eólico Cabo Leones I S.A.',
"ENERGÍAS UCUQUER S.A." : 'Energías Ucuquer S.A.',
"ENERGY ASSET SPA" : 'Energy Asset SpA',
"ENERGYASSET" : 'Energy Asset SpA',
"Enerquinta S.A." : 'Enerquinta S.A.',
"ENERQUINTA S.A." : 'Enerquinta S.A.',
"ENGIE ENERGIA CHILE S.A" : 'Engie Energía Chile S.A.',
"ENGIE ENERGIA CHILE S.A." : 'Engie Energía Chile S.A.',
"ENGIE ENERGÍA CHILE S.A." : 'Engie Energía Chile S.A.',
"ENOR CHILE S.A" : 'Enorchile S.A.',
"ENORCHILE S.A." : 'Enorchile S.A.',
"FRONTEL" : 'Empresa Eléctrica de la Frontera S.A.',
"GENERADORA ELECTRICA KALTEMP LIMITADA" : 'Generadora Eléctrica Kaltemp Ltda.',
"GM HOLDINGS" : 'GM Holdings S.A.',
"GR POWER CHILE SPA" : 'GR Power Chile SpA',
"gr_power_chile_spa" : 'GR Power Chile SpA',
"GUACOLDA" : 'Guacolda Energía SpA',
"GUACOLDA ENERGÍA SPA" : 'Guacolda Energía SpA',
"HELIO ATACAMA" : 'Helio Atacama Tres SpA',
"HIDROELECTRICA RIO COLORADO" : 'Hidroeléctrica Río Colorado S.A.',
"IMELSA ENERGIA SPA" : 'Imelsa Energía SpA',
"IMELSA ENERGIA SpA" : 'Imelsa Energía SpA',
"imelsa_energia_spa" : 'Imelsa Energía SpA',
"LIPIGAS S.A" : 'Empresas Lipigas S.A.',
"LUZ OSORNO" : 'Compañía Eléctrica de Osorno S.A',
"NORVIND S.A" : 'Norvind S.A.',
"NORVIND S.A." : 'Norvind S.A.',
"PACIFIC HYDRO CHILE S.A." : 'Pacific Hydro Chile S.A.',
"PARQUE EOLICO LEBU" : 'Parque Eólico Lebu-Toro SpA',
"SAESA" : 'Sociedad Austral de Electricidad S.A.',
"SAFIRA ENERGIA CHILE" : 'Safira Energía Chile SpA',
"SAFIRA ENERGIA CHILE SPA" : 'Safira Energía Chile SpA',
"SAFIRA_ENERGIA_CHILE" : 'Safira Energía Chile SpA',
"SGA. " : 'Sociedad Generadora Austral S.A.',
"SOC.  GENERADORA AUSTRAL S.A. " : 'Sociedad Generadora Austral S.A.',
"Sociedad Austral de Electricidad, SAESA" : 'Sociedad Austral de Electricidad S.A.',
"SOCIEDAD GENERADORA AUSTRAL S.A." : 'Sociedad Generadora Austral S.A.',
"TECNORED S.A" : 'TecnoRed S.A.',
"TECNORED S.A." : 'TecnoRed S.A.'
}
df1_total["Suministrador"]=df1_total['Suministrador'].map(dict_Suministrador).fillna(df1_total['Suministrador'])


dict_RUT_Suministrador={"72117900-1" : '72.117.900-1',
"76005335-K" : '76.005.335-K',
"76030638-K" : '76.030.638-K',
"76043122-2" : '76.043.122-2',
"76055851-6" : '76.055.851-6',
"76062635-K" : '76.062.635-K',
"76065596-1" : '76.065.596-1',
"76073162-5" : '76.073.162-5',
"76073164-1" : '76.073.164-1',
"76143821-2" : '76.143.821-2',
"76149809-6" : '76.149.809-6',
"76208888-6" : '76.208.888-6',
"76237256-8" : '76.237.256-8',
"76249099-4" : '76.249.099-4',
"76254033-9" : '76.254.033-9',
"76271425-6" : '76.271.425-6',
"76418918-3" : '76.418.918-3',
"76437712-5" : '76.437.712-5',
"76472262-0" : '76.472.262-0',
"76827288-3" : '76.827.288-3',
"76832212-0" : '76.832.212-0',
"76833300-9" : '76.833.300-9',
"76850128-9" : '76.850.128-9',
"76996007-4" : '76.996.007-4',
"77005421-4" : '77.005.421-4',
"77149610-5" : '77.149.610-5',
"77209283-0" : '77.209.283-0',
"77285492-7" : '77.285.492-7',
"77316204-2" : '77.316.204-2',
"77333033-6" : '77.333.033-6',
"77402185-k" : '77.402.185-k',
"77476390-2" : '77.476.390-2',
"78036610-9" : '78.036.610-9',
"78830660-1" : '78.830.660-1',
"79664330-7" : '79.664.330-7',
"79696240-2" : '79.696.240-2',
"79826410-9" : '79.826.410-9',
"79918090-1" : '79.918.090-1',
"79943600-0" : '79.943.600-0',
"80237700-2" : '80.237.700-2',
"81106900-0" : '81.106.900-0',
"81836000-2" : '81.836.000-2',
"82262600-9" : '82.262.600-9',
"83382700-6" : '83.382.700-6',
"86435900-0" : '86.435.900-0',
"88006900-4" : '88.006.900-4',
"88680500-4" : '88.680.500-4',
"90227000-0" : '90.227.000-0',
"90286000-2" : '90.286.000-2',
"90687000-2" : '90.687.000-2',
"91081000-6" : '91.081.000-6',
"94272000-9" : '94.272.000-9',
"95304000-K" : '95.304.000-K',
"96505760-9" : '96.505.760-9',
"96531500-4" : '96.531.500-4',
"96547510-9" : '96.547.510-9',
"96618010-2" : '96.618.010-2',
"96623750-3" : '96.623.750-3',
"96774300-3" : '96.774.300-3',
"96775140-5" : '96.775.140-5',
"96800570-7" : '96.800.570-7',
"96874030-K" : '96.874.030-K',
"96928510-K" : '96.928.510-K',
"99528750-1" : '99.528.750-1',
"99539360-3" : '99.539.360-3',
"Acierta Energía SpA" : '77.333.033-6',
"AES Andes S.A." : '94.272.000-9',
"Cinergia Chile SpA" : '77.285.492-7',
"Colbún S.A." : '96.505.760-9',
"EMOAC SpA" : '76.208.888-6',
"Enel Generación Chile S.A." : '91.081.000-6',
"Guacolda Energía SpA" : '76.418.918-3',
"Imelsa Energía SpA" : '76.472.262-0',
"TecnoRed S.A." : '77.302.440-5'
}

df1_total["RUT Suministrador"]=df1_total['RUT Suministrador'].map(dict_RUT_Suministrador).fillna(df1_total['RUT Suministrador'])

dict_TipoDTE={"NOTA DE CRÉDITO" : 'Nota Crédito',
"FACTURA" : 'Factura'
}


df1_total["TipoDTE"]=df1_total['TipoDTE'].map(dict_TipoDTE).fillna(df1_total['TipoDTE'])



dict_Empresa_Dx={"Enel Distribución Chile S.A." : 'ENEL DISTRIBUCIÓN',
"copelec" : 'COPELEC'   
}
df1_total["Empresa_Dx"]=df1_total['Empresa_Dx'].map(dict_Empresa_Dx).fillna(df1_total['Empresa_Dx'])


dict_Comuna={"ANCUD" : 'Ancud',
"ANGOL" : 'Angol',
"ANTUCO" : 'Antuco',
"ARAUCO" : 'Arauco',
"BULNES" : 'Bulnes',
"bulnes" : 'Bulnes',
"CABRERO" : 'Cabrero',
"CALBUCO" : 'Calbuco',
"CAÑETE" : 'Cañete',
"CASABLANCA" : 'Casablanca',
"CASTRO" : 'Castro',
"chillan" : 'Chillán',
"chillan_viejo" : 'Chillan Viejo',
"CHONCHI" : 'Chonchi',
"coihueco" : 'Coihueco',
"COLLIPULLI" : 'Collipulli',
"CORRAL" : 'Corral',
"CUNCO" : 'Cunco',
"CURACAUTÍN" : 'Curacautín',
"CURANILAHUE" : 'Curanilahue',
"DALCAHUE" : 'Dalcahue',
"EL CARMEN" : 'El Carmen',
"ERCILLA" : 'Ercilla',
"FREIRE" : 'Freire',
"FRESIA" : 'Fresia',
"FRUTILLAR" : 'Frutillar',
"GALVARINO" : 'Galvarino',
"GORBEA" : 'Gorbea',
"LA CALERA" : 'Calera',
"LA UNIÓN" : 'La Unión',
"LAJA" : 'Laja',
"LANCO" : 'Lanco',
"LAUTARO" : 'Lautaro',
"LEBU" : 'Lebu',
"LLANQUIHUE" : 'Llanquihue',
"LLAY LLAY" : 'Llaillay',
"Lo Barnechea (Luz Andes)" : 'Lo Barnechea',
"LONCOCHE" : 'Loncoche',
"LOS ÁLAMOS" : 'Los Álamos',
"Los Angeles" : 'Los Ángeles',
"LOS ÁNGELES" : 'Los Ángeles',
"LOS LAGOS" : 'Los Lagos',
"LOS SAUCES" : 'Los Sauces',
"LOTA" : 'Lota',
"LUMACO" : 'Lumaco',
"MÁFIL" : 'Máfil',
"MARIQUINA" : 'Mariquina',
"MAULLÍN" : 'Maullín',
"MELIPEUCO" : 'Melipeuco',
"MULCHÉN" : 'Mulchén',
"NACIMIENTO" : 'Nacimiento',
"NEGRETE" : 'Negrete',
"NUEVA IMPERIAL" : 'Nueva Imperial',
"OSORNO" : 'Osorno',
"PADRE LAS CASAS" : 'Padre Las Casas',
"PAILLACO" : 'Paillaco',
"PANGUIPULLI" : 'Panguipulli',
"PEMUCO" : 'Pemuco',
"PERQUENCO" : 'Perquenco',
"pinto" : 'Pinto',
"PROVIDENCIA" : 'Providencia',
"PUERTO MONTT" : 'Puerto Montt',
"PUERTO OCTAY" : 'Puerto Octay',
"PUERTO VARAS" : 'Puerto Varas',
"PURRANQUE" : 'Purranque',
"PUYEHUE" : 'Puyehue',
"QUELLÓN" : 'Quellón',
"QUEMCHI" : 'Quemchi',
"ranquil" : 'Ránquil',
"RENAICO" : 'Renaico',
"RÍO BUENO" : 'Río Bueno',
"RÍO NEGRO" : 'Río Negro',
"SAN IGNACIO" : 'San Ignacio',
"SAN PABLO" : 'San Pablo',
"san_carlos" : 'San Carlos',
"SANTA BÁRBARA" : 'Santa Bárbara',
"SANTA JUANA" : 'Santa Juana',
"TEMUCO" : 'Temuco',
"TEODORO SCHMIDT" : 'Teodoro Schmidt',
"TRAIGUEN" : 'Traiguén',
"TRAIGUÉN" : 'Traiguén',
"TUCAPEL" : 'Tucapel',
"VALDIVIA" : 'Valdivia',
"VALPARAÍSO" : 'Valparaíso',
"VICTORIA" : 'Victoria',
"VILCUN" : 'Vilcún',
"YUNGAY" : 'Yungay',
}

df1_total["Comuna"]=df1_total['Comuna'].map(dict_Comuna).fillna(df1_total['Comuna'])


dict_Sistema_Transmision={"STXF" : 'STX F',
"SISTEMA E" : 'STX E',
"SISTEMA F" : 'STX F',
"STx E" : 'STX E',
"STx F" : 'STX F',
"stx_e" : 'STX E',
}

df1_total["Sistema_Transmisión"]=df1_total['Sistema_Transmisión'].map(dict_Sistema_Transmision).fillna(df1_total['Sistema_Transmisión'])


dict_Tipo_Suministro={"Caso 2" : 'AS',
"AEREO" : 'Aéreo',
"Caso 3" : 'SS',
"Caso 1" : 'SA',
"1" : 'Aéreo',
"Aereo" : 'Aéreo'
}

df1_total["Tipo_Suministro"]=df1_total['Tipo_Suministro'].map(dict_Tipo_Suministro).fillna(df1_total['Tipo_Suministro'])


dict_Tarifa={"AT4.3" : 'Peajes AT',
"ATP" : 'Peajes AT',
"BTP" : 'Peajes BT',
"PEAJE_AT" : 'Peajes AT',
"peajes_at" : 'Peajes AT'
}
df1_total["Tarifa"]=df1_total['Tarifa'].map(dict_Tarifa).fillna(df1_total['Tarifa'])

dict_Tipo_Proceso={"LIQUIDACION" : 'Liquidación',
"Liquidacion" : 'Liquidación',
"Refacturacion" : 'Refacturación',
"Reliquidación" : 'Refacturación'    
}
df1_total["Tipo Proceso"]=df1_total['Tipo Proceso'].map(dict_Tipo_Proceso).fillna(df1_total['Tipo Proceso'])


dict_Regimen={"REGULADO" : 'Regulado',
"LIBRE" : 'Libre'
}

df3_total["RegimenActual"]=df3_total['RegimenActual'].map(dict_Regimen).fillna(df3_total['RegimenActual'])
df3_total["RegimenFuturo"]=df3_total['RegimenFuturo'].map(dict_Regimen).fillna(df3_total['RegimenFuturo'])
#mes="2022"
with ExcelWriter("E:\GitHub\RPA_IFC\ifc\pjdx_"+ano+".xlsx") as writer:
    df1_total.to_excel(writer, hoja1, index=False)
    df2_total.to_excel(writer, hoja2, index=False)
    df3_total.to_excel(writer, hoja3, index=False)