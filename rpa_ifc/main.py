from cgitb import text
from re import X
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
#driver=webdriver.Chrome('RPA_IFC/webdriver/chromedriver.exe')

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
service = Service('RPA_IFC/webdriver/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)

# abrir la web
driver.get('https://web.ifc.coordinador.cl/')
#driver.find_element_by_xpath('//*[@id="pdf-proceso-listado"]/div/div[1]/span').send_keys('BADX')

#seleccionaProceso = driver.find_element_by_id('pdf-proceso-listado')
#seleccionaProceso.select_by_index(1)
#driver.find_element_by_id('pdf-proceso-listado').click()
#driver.find_element_by_class_name('mat-option-text').send_keys('BADX')

#Select(driver.find_element(By.ID,"pdf-proceso-listado"))

#select = Select(driver.find_element_by_id('pdf-proceso-listado'))
#time.sleep(5)
time.sleep(1)
#seleccion=
driver.find_element(By.XPATH,'//*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/app-filtros-despliegue-publico/div[1]/mat-form-field[1]/div/div[1]/div').click()
#time.sleep(5)
#x=Select(driver.find_element(By.XPATH,'//*[@id="pdf-proceso-listado"]'))
#time.sleep(5)
#x=Select(driver.find_element(By.XPATH,'//*[@id="pdf-proceso-listado"]'))
#select.first_selected_option
#lista=x.options
#x.options
#x.select_by_visible_text('BADX')

#ok
#seleccion=driver.find_element(By.XPATH,'//*[@id="mat-option-3"]').click()

#seleccion=driver.find_element(By.XPATH,'//*[@id="cdk-overlay-0"]/div').click()
#driver.find_element(By.XPATH,'//*[@id="cdk-overlay-0"]/div/mat-option').find_element(By.XPATH,'EFAC').click()

proceso=[]

#for i=1 to 

for i in range(1, 7):
    proceso.append(driver.find_element(By.XPATH,'//*[@id="cdk-overlay-0"]/div/mat-option[' + str(i) + ']').text)

#p[1]=driver.find_element(By.XPATH,'//*[@id="cdk-overlay-0"]/div/mat-option[1]').text
#p[2]=driver.find_element(By.XPATH,'//*[@id="cdk-overlay-0"]/div/mat-option[2]').text
#p[3]=driver.find_element(By.XPATH,'//*[@id="cdk-overlay-0"]/div/mat-option[3]').text
#p[4]=driver.find_element(By.XPATH,'//*[@id="cdk-overlay-0"]/div/mat-option[4]').text
#p[5]=driver.find_element(By.XPATH,'//*[@id="cdk-overlay-0"]/div/mat-option[5]').text
#p[6]=driver.find_element(By.XPATH,'//*[@id="cdk-overlay-0"]/div/mat-option[6]').text
#p[7]=driver.find_element(By.XPATH,'//*[@id="cdk-overlay-0"]/div/mat-option[7]').text

for i in range(1, 7):
    print("Proceso N°",i,"=", proceso[i-1], proceso.index(proceso[i-1]) )

#proceso_ejemplo="PJDX"
proceso_ejemplo="BAEN"
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="cdk-overlay-0"]/div/mat-option[' + str(proceso.index(proceso_ejemplo)+1) + ']').click()

#//*[@id="pdf-anio-listado"]
#//*[@id="pdf-anio-listado"]/div
#//*[@id="pdf-anio-listado"]/div/div[1]/span/span
#//*[@id="pdf-anio-listado"]/div/div[1]/span/span
#//*[@id="pdf-anio-listado"]/div/div[1]/span/span

#//*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/app-filtros-despliegue-publico/div[1]/mat-form-field[2]/div/div[1]/div
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/app-filtros-despliegue-publico/div[1]/mat-form-field[2]/div/div[1]/div').click()


#//*[@id="pdf-anio-listado"]/div/div[1]
#//*[@id="pdf-anio-listado"]/div
#//*[@id="pdf-anio-listado"]

#//*[@id="mat-option-11"]
#//*[@id="cdk-overlay-1"]/div


ano=[]
for j in range(1, 5):
    ano.append(driver.find_element(By.XPATH,'//*[@id="cdk-overlay-1"]/div/mat-option[' + str(j) + ']').text)

for j in range(1, 5):
    print("Año: ",j,"=", ano[j-1], ano.index(ano[j-1]) )

ano_ejemplo="2022"
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="cdk-overlay-1"]/div/mat-option[' + str(ano.index(ano_ejemplo)+1) + ']').click()



#//*[@id="pdf-mes-listado"]/div/div[1]/span

#//*[@id="pdf-mes-listado"]
#//*[@id="pdf-mes-listado"]/div
#//*[@id="pdf-mes-listado"]/div/div[1]/span
#MES   //*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/app-filtros-despliegue-publico/div[1]/mat-form-field[3]

driver.find_element(By.XPATH,'//*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/app-filtros-despliegue-publico/div[1]/mat-form-field[3]/div/div[1]/div').click()
mes=[]
for j in range(1, 12):
    mes.append(driver.find_element(By.XPATH,'//*[@id="cdk-overlay-2"]/div/mat-option[' + str(j) + ']').text)

for j in range(1, 12):
    print("Mes: ",j,"=", mes[j-1], mes.index(mes[j-1]) )

mes_ejemplo="Agosto"
mes_ejemplo="Marzo"
driver.find_element(By.XPATH,'//*[@id="cdk-overlay-2"]/div/mat-option[' + str(mes.index(mes_ejemplo)+1) + ']').click()

#X

#//*[@id="pd-descargar-uno"]
#//*[@id="pd-descargar-uno"]
#//*[@id="mat-expansion-panel-header-13"]/span/div[7]/a
#//*[@id="mat-expansion-panel-header-15"]/span/div[7]/a
#//*[@id="mat-expansion-panel-header-15"]/span/div[7]
#//*[@id="mat-expansion-panel-header-15"]/span
#//*[@id="mat-expansion-panel-header-15"]
#//*[@id="pd-expasion-panel-"]
#//*[@id="pd-expasion-panel-"]
#//*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/div/mat-card/div[1]
#//*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/div/mat-card

#//*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/div/mat-card/div[1]
#//*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/div/mat-card/div[1]
#//*[@id="mat-expansion-panel-header-76"]/span/div[7]/a
#//*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/div/mat-card/div[1]
#//*[@id="mat-select-4"]/div/div[1]/span/span
#//*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/div/mat-card/div[2]/div[2]/mat-paginator/div/div/div[2]/button[2]/span/svg/path
#//*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/div/mat-card/div[2]/div[2]/mat-paginator/div/div/div[2]/button[2]/span/svg
#//*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/div/mat-card/div[2]/div[2]/mat-paginator/div/div/div[2]/button[2]/span/svg/path
#//*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/div/mat-card/div[2]/div[2]/mat-paginator/div/div/div[2]/button[2]
#driver.find_element(By.XPATH,'//*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/div/mat-card/div[2]/div[2]/mat-paginator/div/div/div[2]/button[2]').
# //*[@id="mat-option-716"]  //*[@id="cdk-overlay-2"]/div
# driver.
time.sleep(5)
#if "disabled" in driver.find_element(By.XPATH,'//*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/div/mat-card/div[2]/div[2]/mat-paginator/div/div/div[2]/button[1]'). :
#    print("disabled")
    # //*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/div/mat-card/div[2]/div[2]/mat-paginator/div/div/div[2]/button[2]/span/svg/path
if EC.url_changes((By.XPATH,'//*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/div/mat-card/div[2]/div[2]/mat-paginator/div/div/div[2]/button[1]/span/svg/path')):
    print("Boton Previous esta activo")
else:
    print("Boton Previous NO esta activo")
    
#if driver.find_element(By.XPATH,'//*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/div/mat-card/div[2]/div[2]/mat-paginator/div/div/div[2]/button[2]').is_enabled :
 #   print("Boton Next esta activo")
#else:
#    print("Boton Next NO esta activo")
#.....

driver.find_element(By.XPATH,'//*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/div/mat-card/div[2]/div[2]/mat-paginator/div/div/div[1]/mat-form-field').click()
largo=driver.find_elements(By.XPATH,'//*[@id="cdk-overlay-3"]/div/mat-option/span[@class="mat-option-text"]')
print('LARGO: ',len(largo))
#print(largo)

elemento=len(largo)
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="cdk-overlay-3"]/div/mat-option['+str(elemento)+']').click()
time.sleep(5)
#driver.find_element(By.XPATH,'//*[@id="cdk-overlay-3"]/div/mat-option['+str(len(largo)-1)+']').click()
#-------
paginas=driver.find_element(By.XPATH,'//*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/div/mat-card/div[2]/div[2]/mat-paginator/div/div/div[2]/div').text
# driver.find_element(By.XPATH,'//*[@id="mat-select-4"]').click()

#1 - 25 of 41

print('paginas: ', paginas)


#//*[@id="cdk-overlay-12"]/div
#//*[@id="cdk-overlay-12"]     -pane
#//*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/div/mat-card/div[2]/div[2]/mat-paginator/div/div/div[1]/mat-form-field
time.sleep(2)
#largo=len(driver.find_element(By.XPATH,'//*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/div/mat-card/div[2]/div[2]/mat-paginator/div/div/div[1]/mat-form-field/div/div[1]/div'))
#largo=[]

#//*[@id="mat-option-688"]

#largo=driver.find_element(By.CSS_SELECTOR,'div.cdk-overlay-pane') 
#//*[@id="mat-option-694"]/span
#/html/body/div[3]/div[2]/div/div
#/html/body/div[3]/div[2]/div/div/mat-option[1]/span


#registros=int(paginas[-2:])

registros=int(paginas[paginas.index('of ')+3:])
registrospp=int(paginas[paginas.index('- ')+2:paginas.index(' of')])
print('registros: ', registros)
print('registros por pagina: ', registrospp)
print('paginas completas: ',registros//registrospp)
print('paginas adicional?: ', 'si' if registros%registrospp>0 else 'no' )
totalp=registros//registrospp + (1 if registros%registrospp>0 else 0)
print('total de paginas: ', registros//registrospp + (1 if registros%registrospp>0 else 0))





time.sleep(3)
#driver.find_element(By.XPATH,'//*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/div/mat-card/div[2]/div[2]/mat-paginator/div/div/div[2]/button[2]').click()

for i in range (1,totalp) :
    driver.find_element(By.XPATH,'//*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/div/mat-card/div[2]/div[2]/mat-paginator/div/div/div[2]/button[2]').click()


time.sleep(3)
#driver.find_element(By.XPATH,'//*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/div/mat-card/div[2]/div[2]/mat-paginator/div/div/div[2]/button[2]').click()


#//*[@id="cdk-overlay-12"]/div
#//*[@id="mat-option-696"]
#//*[@id="mat-option-696"]/span
#mat-option[
    
#//*[@id="cdk-overlay-12"]


#/html/body/div[3]/div[2]/div/div/mat-option[3]/span
#//*[@id="mat-option-2"]/span
#//*[@id="mat-option-2"]
#//*[@id="cdk-overlay-0"]/div
#//*[@id="mat-option-6"]/span
#//*[@id="mat-option-6"]/div
#driver.find_element(By.XPATH,'//*[@id="cdk-overlay-0"]/div/mat-option[3]').click()
#/p[text()='Acceder'] xpath = //md-option[text() = 'IBM Software training']
#seleccion.find_element(By.CLASS_NAME,'mat-option-text').find_element(By.)
#//*[@id="pdf-buscar-proceso"]
#seleccion=driver.find_element(By.XPATH,'//*[@id="mat-input-3"]').send_keys('EFAC')
#driver.find_element(By.XPATH,'//*[@id="mat-option-709"]/span').click()
#//*[@id="mat-option-709"]/span
#//*[@id="mat-option-2"]/span
#//*[@id="cdk-overlay-0"]/div
#//*[@id="mat-option-1"]/span
#time.sleep(5)          //*[@id="mat-option-709"]/span
time.sleep(3)
#driver.find_element(By.NAME,'BADX')
#//*[@id="mat-option-709"]/span
#<span class="mat-option-text"> EFAC </span>
#time.sleep(5)
driver.quit()
