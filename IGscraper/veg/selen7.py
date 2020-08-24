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


def parserecipe(url,title, img):
    
    driver.get(url)
    ingredients = []
    method = []
    i=1
    serveT=""
    timeis=''
    id_global=0
    instructions=[]
    nutrition=[]
    totaltime=0
    

    if (True):

        try:
            elem=driver.find_elements(By.TAG_NAME, 'ul')
            for e in elem:
                if e.get_attribute('class')=='steps':
                    lst = e.find_elements(By.TAG_NAME, 'li')
                    for step in lst:
                        print(step.text)
                        times = re.findall(r'\d+ minutes', step.text)
                        for time in times:
                            print(time)
                            totaltime += int(re.findall(r'\d+', time)[0])
                        instructions.append(step.text)
                elif e.get_attribute('class')=='ingredients__group':
                    inglst=e.find_elements(By.TAG_NAME, 'li')
                    for ing in inglst:
                        print(ing.text)
                        ingredients.append(ing.text)
            
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

           
            # serve=driver.find_element_by_xpath(f'//*[@id="tasty-recipes-{id}"]/div[2]/div[3]/span/span[1]')
            try:

                tpr=driver.find_element(By.CLASS_NAME, 'recipe__header__servings').text
                ides = re.findall(r'\d+', tpr)
                serveT=ides[0]
                print(serveT)

                timeis = str(totaltime)+' minutes'
                print(timeis)
                            
                            
                # yolo=node.find_elements(By.TAG_NAME, 'span')[0].text
                # print(yolo)
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
       
        with open('data7', 'wb') as fp:
            pickle.dump(recipes, fp)   

    else:
        return

     


with webdriver.Chrome("C:/WebDriver/bin/chromedriver.exe", options=options) as driver:
    i=1
    wordlist = ["How"]
    recipes = []
    num=1
    
    while True:

        
        if i==70:
            break

        driver.get(f'https://www.bonappetit.com/recipes/vegetarian/slideshow/easy-vegetarian-dinner-recipes')
      
        
        ERROR = False
        
        
        # visibility = driver.find_element_by_xpath(f'//*[@id="recipeindex"]/li[{i}]').get_attribute('class')
        
        # if 'visible'not in visibility:
        #     ERROR = True
        
        try:
        
            title = driver.find_element_by_xpath(f'//*[@id="main-content"]/article/div[2]/div[1]/div[1]/div[1]/ul/li[{i}]/div[1]/figure/figcaption/div/a/h2/span').text
            print(title)
        except:
          
            
            i+=1
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
                                                                             
        # img = driver.find_element_by_xpath(f'//*[@id="main-content"]/article/div[2]/div[1]/div[1]/div[1]/ul/li[{i}]/div[1]/figure/div/div/div/span/picture/img').get_attribute('src')
        # print(i)
        # Y=1500*i
        # driver.execute_script(f"window.scrollTo(0, {Y})")
        
        # img = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="main-content"]/article/div[2]/div[1]/div[1]/div[1]/ul/li[{i}]/div[1]/figure/div/div/div/span/picture/img'))).get_attribute("src")
        img='none'
        parserecipe(driver.find_element_by_xpath(f'//*[@id="main-content"]/article/div[2]/div[1]/div[1]/div[1]/ul/li[{i}]/div[1]/figure/figcaption/div/a').get_attribute('href'),title, img)
        
        print("PARSED")
        
        i+=1

    # driver.navigate().back()

    
