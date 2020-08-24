from selenium import webdriver
import json
import time
import pickle
from selenium.webdriver.common.by import By
from datetime import datetime
import regex as re
import pickle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# VEGGIE
class Recipe:
    def __init__(self, url, ingredients, servings):
        super().__init__()
        self.url = url
        self.ingredients = ingredients
        self.servings = servings
  
options = webdriver.ChromeOptions()


def parserecipe(url, title, serveT, timeis, img):
    
    print(title)
    print(serveT)
    print(timeis)

    driver.get(url)
    ingredients = []
    method = []
    i=1
    id_global=0
    instructions=[]
    nutrition=[]
    
    

    if (True):

        try:
            elem=driver.find_elements(By.TAG_NAME, 'ul')
            for el in elem:
                if 'steps' in el.get_attribute('class'):
                    methlist=el.find_elements(By.TAG_NAME, 'li')
                    for meth in methlist:
                        print(meth.text)
                        instructions.append(meth.text)
        
        except:
            print('EEEE')
            return

        try:
            # id=''
            # id = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/article/div[2]/div[1]/a').get_attribute('href')
            # ids=re.findall(r'\d+', id)
            # id=ids[0]

            # for d in ids:
            #     txt = d.get_attribute('id')
            #     ides = re.findall(r'\d+', txt)
            #     if len(ides) != 0 and len(ides[0])>3:
            #         print(ides)
            #         id =ides[0]
                    

            # print(id)
            # id = driver.find_element_by_xpath('//*[@id="content"]/div[1]/a').get_attribute("href")
            # ids=re.findall(r'\d+', id)
            # id=ids[0]


            headings = driver.find_elements(By.TAG_NAME, 'h3')
            for heading in headings:
                if 'Ingredients' in heading.text or 'INGREDIENTS' in heading.text:
                    ul=heading.find_element(By.XPATH, 'following-sibling::*')
                    lilist=ul.find_elements(By.TAG_NAME, 'li')
                    for li in lilist:
                        print(li.text)
                        ingredients.append(li.text)
            # elems = driver.find_element(By.XPATH, f'//*[@id="tasty-recipes-{id}"]/div[5]').find_elements(By.TAG_NAME, 'li')
        
            
        except AssertionError as error:
            print(error)
            return
# //*[@id="tasty-recipes-73229"]/div/div[2]/ul/li[1]
        

        # print(img)
        recipes.append([title, url, ingredients, serveT, img, instructions, nutrition, timeis, 'vegetarian'])
        # with open('data.txt', 'w') as outfile:
            # json.dump(recipes, outfile)

        with open('data8', 'wb') as fp:
            pickle.dump(recipes, fp)   

    else:
        return

     


with webdriver.Chrome("C:/WebDriver/bin/chromedriver.exe", options=options) as driver:
    i=1
    wordlist = ["How"]
    recipes = []
    num=1
    serveT=''
    timeis=''
    
    while True:

        if num==70:
            break

        driver.get(f'https://www.olivemagazine.com/recipes/vegetarian/page/{num}')
        

        if i==1 and num==1:
            time.sleep(10)
            driver.find_element(By.XPATH, '//*[@id="qcCmpButtons"]/button[2]').click()
        
        ERROR = False
        
        
        # visibility = driver.find_element_by_xpath(f'//*[@id="recipeindex"]/li[{i}]').get_attribute('class')
        
        # if 'visible'not in visibility:
        #     ERROR = True
       
        try:
                                                
            title = driver.find_element_by_xpath(f'//*[@id="main-content"]/div/div/section/div[1]/div/div[{i}]/div/div[1]/div[2]/div[2]/h4/a').text
          
            info = driver.find_element_by_xpath(f'//*[@id="main-content"]/div/div/section/div[1]/div/div[{i}]/div/div[2]').text
            if 'snack' in info or 'SNACK' in info:
                print('skip')
                i+=1
                continue
            else:
                timeis=driver.find_element_by_xpath(f'//*[@id="main-content"]/div/div/section/div[1]/div/div[{i}]/div/div[2]/span[1]').text
                serve=driver.find_element_by_xpath(f'//*[@id="main-content"]/div/div/section/div[1]/div/div[{i}]/div/div[2]/span[2]').text
                # print(timeis)
                serveT = re.findall(r'\d+', serve)[0]
                # print(serveT)
            
        except:
          
            num+=1
            i=1
            continue
       
        for word in wordlist:
            if word in title:
                print("ERROR")
                ERROR = True
                break
            # check number
        if (re.search(r'\d', title)):
            print("NUMBER ERROR")
            ERROR = True
            
            
        if ERROR:
            i+=1
            continue
        
        img = driver.find_element_by_xpath(f'//*[@id="main-content"]/div/div/section/div[1]/div/div[{i}]/div/div[1]/div[1]/a/picture/img').get_attribute('src')
        # imgs=re.findall(r'(?P<url>https?://[^\s]+)', img)
        # for r in imgs:
        #     # print(r)
        #     # print(r[:-3])
        #     img=r[:-3]


        
        # img = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="recipeindex"]/li[{i}]/a/div[1]/img'))).get_attribute("src")

       
        parserecipe(driver.find_element_by_xpath(f'//*[@id="main-content"]/div/div/section/div[1]/div/div[{i}]/div/div[1]/div[2]/div[2]/h4/a').get_attribute('href'), title, serveT, timeis, img)
        
        print("PARSED")
        
        i+=1

    # driver.navigate().back()

    
