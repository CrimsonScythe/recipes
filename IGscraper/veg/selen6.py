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


def parserecipe(url, img):
    
    driver.get(url)
    ingredients = []
    method = []
    i=1
    serveT=""
    id_global=0
    instructions=[]
    nutrition=[]
    timeis=''
    dates=driver.find_elements(By.TAG_NAME, 'meta')
    month=0
    # for date in dates:
    #     if date.get_attribute('property')=='article:published_time':
    #         final = date.get_attribute('content')
    

    #         fin = int(final[5:7])
    #         month=fin

    if (True):
        
        try:
            
            elem=driver.find_element(By.CLASS_NAME, 'post-method-steps__collection').find_elements(By.TAG_NAME, 'li')
            
            for e in elem:
                # subbed = re.sub(r'STEP+?\s\d+', '', e.text)
                # print(subbed)
                # instructions.append(subbed)
                print(e.text)
                instructions.append(e.text)
        except:
            return

        try:
            # id=''
            # ids = driver.find_elements(By.TAG_NAME, 'div')
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

            ingre = driver.find_element(By.CLASS_NAME, 'list-group').find_elements(By.TAG_NAME, 'li')
            # elems = driver.find_element(By.XPATH, f'//*[@id="tasty-recipes-{id}"]/div[5]').find_elements(By.TAG_NAME, 'li')
            for ing in ingre:
                print(ing.text)
                ingredients.append(ing.text)

            # serve=driver.find_element_by_xpath(f'//*[@id="tasty-recipes-{id}"]/div[2]/div[3]/span/span[1]')
            try:
                
                serves = driver.find_elements(By.CLASS_NAME, 'recipe-key-data__item')
                for ser in serves:
                    txt=ser.find_element(By.TAG_NAME, 'span').text
                    print(txt)
                    # if ser.text
                # print(serve.text)
                # serveT=serve.text

                # timeis = driver.find_element(By.CLASS_NAME, 'tasty-recipes-total-time').text
                # print(timeis)
            except:
                return
        except AssertionError as error:
            print(error)
            return
# //*[@id="tasty-recipes-73229"]/div/div[2]/ul/li[1]
        

        # print(img)
        recipes.append([url, ingredients, serveT, img, instructions, nutrition, timeis])
        # with open('data.txt', 'w') as outfile:
            # json.dump(recipes, outfile)

        with open('data6', 'wb') as fp:
            pickle.dump(recipes, fp)   

    else:
        return

     


with webdriver.Chrome("C:/WebDriver/bin/chromedriver.exe", options=options) as driver:
    i=1
    wordlist = ["How"]
    recipes = []
    num=1
    title=''

    while True:

        if num==15:
            break

        driver.get(f'https://www.olivemagazine.com/recipes/vegetarian/page/{num}')
      
        
        ERROR = False
        
        
        # visibility = driver.find_element_by_xpath(f'//*[@id="recipeindex"]/li[{i}]').get_attribute('class')
        
        # if 'visible'not in visibility:
        #     ERROR = True
        
       
        try:
            
            title = driver.find_element_by_xpath(f'//*[@id="main-content"]/div/div/section/div[1]/div/div[{i}]/div/div[1]/div[2]/div[2]/h4/a').text
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
        
        # img = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="recipeindex"]/li[{i}]/a/div[1]/img'))).get_attribute("src")


        parserecipe(driver.find_element_by_xpath(f'//*[@id="main-content"]/div/div/section/div[1]/div/div[{i}]/div/div[1]/div[2]/div[2]/h4/a').get_attribute('href'), img)
        

        print("PARSED")
        
        i+=1

    # driver.navigate().back()

    
