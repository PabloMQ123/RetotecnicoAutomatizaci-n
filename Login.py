from selenium import webdriver
import time

from selenium.webdriver.common.by import By

#abrir pagina

url="https://www.saucedemo.com"
tiempo=5
d = webdriver.Chrome()
d.get(url)
d.maximize_window()
usr=d.find_element(By.XPATH,"//*[@id='user-name']").send_keys("standard_user")
time.sleep(tiempo)
pas=d.find_element(By.XPATH,"//*[@id='password']").send_keys("secret_sauce")
time.sleep(tiempo)
btn=d.find_element(By.XPATH,"//*[@id='login-button']")
btn.click()

time.sleep(tiempo)
#Para cerrar la ventana
d.close()