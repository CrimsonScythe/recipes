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
    
    

    if (True):

        try:
            elem=driver.find_element(By.CLASS_NAME, 'mv-create-instructions').find_elements(By.TAG_NAME, 'li')
            for e in elem:
                print(e.text)
                instructions.append(e.text)
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

            ingre = driver.find_element(By.CLASS_NAME, 'mv-create-ingredients').find_elements(By.TAG_NAME, 'li')
            # elems = driver.find_element(By.XPATH, f'//*[@id="tasty-recipes-{id}"]/div[5]').find_elements(By.TAG_NAME, 'li')
            for ing in ingre:
                print(ing.text)
                ingredients.append(ing.text)

            # serve=driver.find_element_by_xpath(f'//*[@id="tasty-recipes-{id}"]/div[2]/div[3]/span/span[1]')
            try:
                serve=driver.find_element(By.CLASS_NAME, 'mv-create-yield').text
                serveT = re.findall(r'\d+', serve)[0]
                print(serveT)
                # serve=driver.find_element(By.CLASS_NAME, 'wprm-recipe-servings-container').find_elements(By.TAG_NAME, 'span')[1].find_elements(By.TAG_NAME, 'span')[0]
                # serve = serve.text
                # serveT=serve
                # print(serveT)

                times = driver.find_elements(By.CLASS_NAME, 'mv-create-time')
                print(times[0].text)
                print(times[1].text)
                print(times[2].text)
                timeis=re.findall(r'\d+', times[2].text)[0] + ' minutes'
                print(timeis)

            except:
                
                return
        except AssertionError as error:
            print(error)
            return
# //*[@id="tasty-recipes-73229"]/div/div[2]/ul/li[1]
        

        # print(img)
        recipes.append([title, url, ingredients, serveT, img, instructions, nutrition,timeis, 'vegetarian'])
        # with open('data.txt', 'w') as outfile:
            # json.dump(recipes, outfile)

        with open('data10', 'wb') as fp:
            pickle.dump(recipes, fp)   

    else:
        return

     


with webdriver.Chrome("C:/WebDriver/bin/chromedriver.exe", options=options) as driver:
    i=1
    wordlist = ["How"]
    recipes = []
    num=1
    
    while True:

        if num==15:
            num+=1
            i=1
            continue

        if num==21:
            break

        driver.get(f'https://withfoodandlove.com/category/mains/page/{num}')
      
        if i==1 and num==1:
            time.sleep(10)
            
            # driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/a').click()
        
        ERROR = False
        
        
        # visibility = driver.find_element_by_xpath(f'//*[@id="recipeindex"]/li[{i}]').get_attribute('class')
        
        # if 'visible'not in visibility:
        #     ERROR = True
       
    
        try:
            title = driver.find_element_by_xpath(f'/html/body/div[2]/div/div/main/article[{i}]/header/h2/a').text
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
            
        # typ = driver.find_element_by_xpath(f'//*[@id="main-content"]/div/main/article[{i}]/div/div/p/a').text
        
        # if 'DINNER' not in typ:
        #     print('SIDE ERROR')
        #     ERROR = True
            
        if ERROR:
            i+=1
            continue
        
        

        # img = driver.find_element_by_xpath(f'//*[@id="main-content"]/div/main/article[{i}]/div/a').get_attribute('style')
        # imgs=re.findall(r'(?P<url>https?://[^\s]+)', img)
        # for r in imgs:
            # print(r)
            # print(r[:-3])
            # img=r[:-3]

        
        img = driver.find_element_by_xpath(f'/html/body/div[2]/div/div/main/article[{i}]/header/div/a/img').get_attribute('src')
        
        # img = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="recipeindex"]/li[{i}]/a/div[1]/img'))).get_attribute("src")

       
        parserecipe(driver.find_element_by_xpath(f'/html/body/div[2]/div/div/main/article[{i}]/header/h2/a').get_attribute('href'), title, img)
        
        print("PARSED")
        
        i+=1

    # driver.navigate().back()

    
