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
        # self.method = method

# PROXY = "35.230.21.108:80"

# webdriver.DesiredCapabilities.CHROME['proxy'] = {

#     "httpProxy": PROXY,
#     "ftpProxy": PROXY,
#     "sslProxy": PROXY,
#     "proxyType": "MANUAL",

# }

options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 123.1.0.26.115 (iPhone11,8; iOS 13_3; en_US; en-US; scale=2.00; 828x1792; 190542906)")




def getAmount(root):
    try:
        quan= root.find_element(By.CLASS_NAME, 'wprm-recipe-ingredient-amount')
        return quan
    except:
        pass


def getUnit(root):
    try:
        unit= root.find_element(By.CLASS_NAME, 'wprm-recipe-ingredient-unit')
        return unit
    except:
        pass



def parserecipe(url, title, img):
    # driver.get('https://www.loveandlemons.com/black-bean-burger-recipe/')
    
    driver.get(url)
    ingredients = []
    method = []
    i=1
    serveT=""
    id_global=0
    instructions=[]
    nutrition=[]
    
    
    if (True):
        

        try:
            elem=driver.find_element(By.CLASS_NAME, 'instructions').find_elements(By.TAG_NAME, 'li')
            for e in elem:
                print(e.text)
                instructions.append(e.text)
        except:
            return

        try:
        
            # id = driver.find_element_by_xpath('//*[@id="content"]/div[1]/a').get_attribute("href")
            # ids=re.findall(r'\d+', id)
            # id=ids[0]
            
            # ingre = driver.find_element(By.CLASS_NAME, 'tasty-recipes-ingredients').find_elements(By.TAG_NAME, 'li')
            ingre = driver.find_element(By.CLASS_NAME, 'ingredients').find_elements(By.TAG_NAME, 'li')
            # elems = driver.find_element(By.XPATH, f'//*[@id="tasty-recipes-{id}"]/div/div[1]').find_elements(By.TAG_NAME, 'li')
            for ing in ingre:
                print(ing.text)
                ingredients.append(ing.text)

            # serve=driver.find_element_by_xpath(f'//*[@id="tasty-recipes-{id}"]/header/div[2]/div[2]/ul/li[4]/span[2]/span[1]')
            serve = driver.find_elements(By.TAG_NAME, 'span')
            for s in serve:
                if s.get_attribute('itemprop') == 'recipeYield':
                    serveT = s.text[0]
            print(serveT)
            ps = driver.find_elements(By.TAG_NAME, 'strong')
            for p in ps:
                if p.text== 'total time:':
                    # print(p.text)
                    sib=p.find_element(By.XPATH, 'following-sibling::*')
                    # print(sib.text)
                    timeis=sib.text
            
            print(timeis)
            ERR=False
            isveg = driver.find_elements(By.CLASS_NAME, 'post-meta')
            for l in isveg:
                if 'ENTREE' in l.text:
                    print(l.text)
                else:
                    ERR=True

            if ERR:
                return

        except:
            return
# //*[@id="tasty-recipes-73229"]/div/div[2]/ul/li[1]
        

        # print(img)
        recipes.append([title, url, ingredients, serveT, img, instructions, nutrition, timeis, 'vegetarian'])
        # with open('data.txt', 'w') as outfile:
            # json.dump(recipes, outfile)

        with open('data3', 'wb') as fp:
            pickle.dump(recipes, fp)   

    else:
        return

    # while True:
    #     try:

            

    #         id = driver.find_element_by_xpath('//*[@class="wprm-recipe-container"]').get_attribute("data-recipe-id")
    #         id_global = id
    #         # print(id)
    #         root = driver.find_element_by_xpath(xpath=f'//*[@id="wprm-recipe-container-{id}"]/div/div[12]/div/ul/li[{i}]')
            
            
     
    #         amount = getAmount(root)
    #         unit = getUnit(root)
            
            
    #         ing = root.find_element(By.CLASS_NAME, 'wprm-recipe-ingredient-name')
    #         serve=driver.find_element_by_xpath(f'//*[@id="wprm-recipe-container-{id}"]/div/div[8]/span[2]')
    
    #         date=driver.find_element_by_xpath('/html/head/meta[20]').get_attribute("content")


    #         month = int(date[5:7])
    #         if (datetime.today().month-1 == month):
                
                
    #             amountStr=""
    #             unitStr=""
    #             print(ing.text)
    #             if (amount is not None):
    #                 amountStr = amount.text
    #                 print(amount.text)
    #             if (unit is not None):
    #                 unitStr = unit.text
    #                 print(unit.text)
    #             # print(serve.text)
                

    #             ingredients.append(amountStr+' '+unitStr + ' ' + ing.text)
    #             serveT=serve.text
    #         # driver.implicitly_wait(10)
    #             i+=1
    #         else:
    #             return    
                
    #     except:
    #         break

     


with webdriver.Chrome("C:/WebDriver/bin/chromedriver.exe", options=options) as driver:
    i=1
    wordlist = ["How"]
    recipes = []
    num=1
    
    
    while True:

        # if len(recipes)==3:
        #     break
        if num==6:
            break

        driver.get(f'https://damndelicious.net/category/vegetarian/page/{num}')
        
        
        ERROR = False
        
        
        
        # visibility = driver.find_element_by_xpath(f'//*[@id="recipeindex"]/li[{i}]').get_attribute('class')
        
        # if 'visible'not in visibility:
        #     ERROR = True
        try:

            title = driver.find_element_by_xpath(f'//*[@id="content"]/div[1]/div[{i}]/a/h4').text
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
        
        img = driver.find_element_by_xpath(f'//*[@id="content"]/div[1]/div[{i}]/a/img').get_attribute('src')
        # img = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="recipeindex"]/li[{i}]/a/div[1]/img'))).get_attribute("src")

        
        parserecipe(driver.find_element_by_xpath(f'//*[@id="content"]/div[1]/div[{i}]/a').get_attribute('href'),title, img)
        
        print("PARSED")
        
        i+=1

    # driver.navigate().back()

    
