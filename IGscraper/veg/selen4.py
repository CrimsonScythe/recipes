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


def parserecipe(url, title, img):
    
    driver.get(url)
    ingredients = []
    method = []
    i=1
    serveT=""
    timeis=''
    id_global=0
    instructions=[]
    nutrition=[]
    
    # dates=driver.find_elements(By.TAG_NAME, 'meta')
    # month=0
    # for date in dates:
    #     if date.get_attribute('property')=='article:published_time':
    #         final = date.get_attribute('content')
    

    #         fin = int(final[5:7])
    #         month=fin

    if (True):

        try:
            elem=driver.find_element(By.CLASS_NAME, 'wprm-recipe-instructions').find_elements(By.TAG_NAME, 'li')
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

            ingre = driver.find_element(By.CLASS_NAME, 'wprm-recipe-ingredients').find_elements(By.TAG_NAME, 'li')
            # elems = driver.find_element(By.XPATH, f'//*[@id="tasty-recipes-{id}"]/div[5]').find_elements(By.TAG_NAME, 'li')
            for ing in ingre:
                print(ing.text)
                ingredients.append(ing.text)

            # serve=driver.find_element_by_xpath(f'//*[@id="tasty-recipes-{id}"]/div[2]/div[3]/span/span[1]')
            try:
                headers=driver.find_elements(By.CLASS_NAME, 'wprm-recipe-time-header')
                for h in headers:
                    if h.text=='Total Time':
                        nodet=h.find_element(By.XPATH, 'following-sibling::*')
                        timeis=nodet.text
                        print(timeis)
                    if h.text=='Serves':
                        nodes=h.find_element(By.XPATH, 'following-sibling::*')
                        serveT=nodes.text
                        print(serveT)
                # divs=driver.find_elements(By.TAG_NAME, 'div')
                # for di in divs:
                #     if 'TOTAL' in di.text:
                #         if 'TIME' in di.text:
                #             nodem=di.find_element(By.XPATH, 'following-sibling::*')
                #             timeis=nodem.text
                #             print(nodem.text)
                    
                #     if 'SERVES' in di.text:
                #         nodes=di.find_element(By.XPATH, 'following-sibling::*')
                #         serveT=nodes.text
                #         print(serveT.text)
                            
                
                
            except:
                return
        except AssertionError as error:
            print(error)
            return
# //*[@id="tasty-recipes-73229"]/div/div[2]/ul/li[1]
        

        # print(img)
        recipes.append([title, url, ingredients, serveT, img, instructions, nutrition, timeis, 'vegetarian'])
        # with open('data.txt', 'w') as outfile:
            # json.dump(recipes, outfile)

        with open('data4', 'wb') as fp:
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

        driver.get(f'https://www.101cookbooks.com/dinner_ideas/page/{num}')
        
        
        ERROR = False
        
        # //*[@id="main"]/div[1]/div[3]/div[2]/h5/a
        # //*[@id="main"]/div[1]/div[4]/div[2]/h5/a
        # //*[@id="main"]/div[1]/div[5]/div[2]/h5/a
        # visibility = driver.find_element_by_xpath(f'//*[@id="recipeindex"]/li[{i}]').get_attribute('class')
        
        # if 'visible'not in visibility:
        #     ERROR = True
        try:
            title = driver.find_element_by_xpath(f'//*[@id="main"]/div[1]/div[{2+i}]/div[2]/h5/a').text
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
        
        img = driver.find_element_by_xpath(f'//*[@id="main"]/div[1]/div[{2+i}]/div[1]/a/img').get_attribute('src')
        # img = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="recipeindex"]/li[{i}]/a/div[1]/img'))).get_attribute("src")


        parserecipe(driver.find_element_by_xpath(f'//*[@id="main"]/div[1]/div[{2+i}]/div[2]/h5/a').get_attribute('href'), title, img)
        
        print("PARSED")
        
        i+=1

    # driver.navigate().back()

    
