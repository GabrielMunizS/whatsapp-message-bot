from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import urllib
import time
import os

nav = webdriver.Chrome()
nav.get("https://web.whatsapp.com")


while len(nav.find_elements(By.ID, 'side')) < 1:
    time.sleep(1)
time.sleep(2) 

sheet = pd.read_excel("Envios.xlsx")
display(sheet[['nome', 'mensagem', 'arquivo']])


for line in sheet.index:
  
    name = sheet.loc[line, "nome"]
    msg = sheet.loc[line, "mensagem"]
    file = sheet.loc[line, "arquivo"]
    phone_n = sheet.loc[line, "telefone"]
    
    text = msg.replace("fulano", name) # "fulano" means someone or a random person
    text = urllib.parse.quote(text)

   
    link = f"https://web.whatsapp.com/send?phone={phone_n}&text={text}"
    
    nav.get(link)
    
    while len(nav.find_elements(By.ID, 'side')) < 1:
        time.sleep(1)
    time.sleep(2) 
    

    if len(nav.find_elements(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]')) < 1:
        
        nav.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
        
        if file != "N":
            All_d_way = os.path.abspath(f"arquivos/{file}")
            nav.find_element(By.XPATH, 
                                   '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span').click()
            nav.find_element(By.XPATH, 
                                   '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[4]/button/input').send_keys(All_d_way)
            time.sleep(2)
            nav.find_element(By.XPATH, 
                                   '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div').click()
            
        time.sleep(5)
