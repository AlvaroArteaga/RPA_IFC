from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
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
driver.find_element(By.XPATH,'//*[@id="mat-tab-content-0-0"]/div/app-despliegue-publico/app-filtros-despliegue-publico/div[1]/mat-form-field[1]/div/div[1]/div').click()
#time.sleep(5)
#x=Select(driver.find_element(By.XPATH,'//*[@id="pdf-proceso-listado"]'))
#time.sleep(5)
#x=Select(driver.find_element(By.XPATH,'//*[@id="pdf-proceso-listado"]'))
#select.first_selected_option
#lista=x.options
#x.options
#x.select_by_visible_text('BADX')
time.sleep(5)
driver.quit() 