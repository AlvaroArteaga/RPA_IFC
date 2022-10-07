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
mes='Junio'
#mes='Julio'
#mes='Agosto'
#actualizar ruta variable
ruta = "C:\GitHub\RPA_IFC\ifc\PJDX\\2022\\" + mes
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
        df1 = pd.read_excel(file, sheet_name=hoja1)
        #Find index of first row with 'No." in the first column and take everything till the end:
        df1 = df1.iloc[df1[df1.iloc[:, 0].eq('Id_Cliente')].index[0]:, :].reset_index(drop=True)
        #Set first row as columns:

        df1.columns = df1.iloc[0]
        #Drop first row (we do not need it because there are column names repeated there):
        # data  = data.replace('', np.nan).dropna()
        df1['ifc_mes']=mes
        df1['ifc_año']=ano
        df1 = df1.drop(0).reset_index(drop=True)
        #df1.dropna()
        #df1 = excel_file.parse(sheet_name = hoja1, header=0)
        df1_total = df1_total.append(df1)
        
        df2 = excel_file.parse(sheet_name = hoja2, header=0)
        
        df2['ifc_mes']=mes
        df2['ifc_año']=ano
        
        df2_total = df2_total.append(df2)
        
        df3 = excel_file.parse(sheet_name = hoja3, header=0)
        
        df3['ifc_mes']=mes
        df3['ifc_año']=ano
        
        
        df3_total = df3_total.append(df3)
        #df_total.to_excel('combined_file.xlsx')

        nan_value = float("NaN") 
        df1_total.replace("", nan_value, inplace=True) 
        df1_total.dropna(how='all', axis=1, inplace=True)
        df2_total.replace("", nan_value, inplace=True) 
        df2_total.dropna(how='all', axis=1, inplace=True)
        df3_total.replace("", nan_value, inplace=True) 
        df3_total.dropna(how='all', axis=1, inplace=True)

#mes="2022"
#actualizar ruta variable
with ExcelWriter("C:\GitHub\RPA_IFC\ifc\pjdx_"+mes+ano+".xlsx") as writer:
    df1_total.to_excel(writer, hoja1, index=False)
    df2_total.to_excel(writer, hoja2, index=False)
    df3_total.to_excel(writer, hoja3, index=False)