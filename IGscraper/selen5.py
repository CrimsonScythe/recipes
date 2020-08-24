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

class Recipe:
    def __init__(self, url, ingredients, servings):
        super().__init__()
        self.url = url
        self.ingredients = ingredients
        self.servings = servings
  
options = webdriver.ChromeOptions()


def parserecipe(url,title, img):
    
    driver.get(url)
    ingredients = []
    method = []
    i=1
    serveT=""
    id_global=0
    instructions=[]
    nutrition=[]
    timeis=""
    dates=driver.find_elements(By.TAG_NAME, 'meta')
    month=0
    for date in dates:
        if date.get_attribute('property')=='article:published_time':
            final = date.get_attribute('content')
    

            fin = int(final[5:7])
            month=fin

    if (True):

        try:
            elem=driver.find_element(By.CLASS_NAME, 'tasty-recipes-instructions').find_elements(By.TAG_NAME, 'li')
            for e in elem:
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

            ingre = driver.find_element(By.CLASS_NAME, 'tasty-recipes-ingredients').find_elements(By.TAG_NAME, 'li')
            # elems = driver.find_element(By.XPATH, f'//*[@id="tasty-recipes-{id}"]/div[5]').find_elements(By.TAG_NAME, 'li')
            for ing in ingre:
                print(ing.text)
                ingredients.append(ing.text)

            # serve=driver.find_element_by_xpath(f'//*[@id="tasty-recipes-{id}"]/div[2]/div[3]/span/span[1]')
            try:
                serve = driver.find_element(By.CLASS_NAME, 'tasty-recipes-yield').find_element(By.TAG_NAME, 'span')
                print(serve.text)
                serveT=serve.text

                prept = driver.find_element(By.CLASS_NAME, 'tasty-recipes-prep-time').text
                cookt = driver.find_element(By.CLASS_NAME, 'tasty-recipes-cook-time').text
                timeis=prept+' '+cookt
                print(timeis)
            except:
                return
        except AssertionError as error:
            print(error)
            return
# //*[@id="tasty-recipes-73229"]/div/div[2]/ul/li[1]
        

        # print(img)
        recipes.append([title,url, ingredients, serveT, img, instructions, nutrition, timeis, 'all'])
        # with open('data.txt', 'w') as outfile:
            # json.dump(recipes, outfile)

        with open('data5', 'wb') as fp:
            pickle.dump(recipes, fp)   

    else:
        return

     


with webdriver.Chrome("C:/WebDriver/bin/chromedriver.exe", options=options) as driver:
    i=1
    wordlist = ["How"]
    recipes = []
    num=1
    
    while True:

        if num==7:
            break

        driver.get(f'https://pinchofyum.com/recipes?fwp_dinner=meat%2Cquick-and-easy&fwp_paged={num}')
      
        
        ERROR = False
        
        
        # visibility = driver.find_element_by_xpath(f'//*[@id="recipeindex"]/li[{i}]').get_attribute('class')
        
        # if 'visible'not in visibility:
        #     ERROR = True
        
        try:
            title = driver.find_element_by_xpath(f'/html/body/div[2]/div[2]/div/div[2]/main/div[1]/article[{i}]/div').text
            print(title)
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
        
        img = driver.find_element_by_xpath(f'/html/body/div[2]/div[2]/div/div[2]/main/div[1]/article[{i}]/img').get_attribute('src')
        
        # img = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="recipeindex"]/li[{i}]/a/div[1]/img'))).get_attribute("src")

        
        parserecipe(driver.find_element_by_xpath(f'/html/body/div[2]/div[2]/div/div[2]/main/div[1]/article[{i}]/a').get_attribute('href'), title, img)
        
        print("PARSED")
        
        i+=1

    # driver.navigate().back()

    
