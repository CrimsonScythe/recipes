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

def getInstructions(root, id):
    try:
        print("tryin...")
        meth = root.find_element(By.CLASS_NAME, 'wprm-recipe-instruction-text')
        print(meth)
        print(meth.text)
        return meth
    except:
        pass
    # i=1
    # while True:
    #     try:
    #         # //*[@id="wprm-recipe-container-48965"]/div/div[13]/div/ul
    #         print(id)
    #         # method = driver.find_element_by_xpath(xpath=f'//*[@id="wprm-recipe-container-{id}"]/div/div[13]/div/ul/li{i}').find_element(By.TAG_NAME, 'div')
    #         method = driver.find_element(By.CLASS_NAME, 'wprm-recipe-instruction-text')
    #         print(method)
    #         print(method.text)
    #         i+=1
    #     except:
    #         break


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

def getImg(root, i):
    try:
        if (i==20):
            print("YES")
        img = root.find_element_by_xpath(f'//*[@id="recipeindex"]/li[{i}]/a/div[1]/img').get_attribute('src')
        # print(img)
        
        return img
    except:
        pass


def parserecipe(url, img):
    # driver.get('https://www.loveandlemons.com/black-bean-burger-recipe/')
    
    driver.get(url)
    ingredients = []
    method = []
    i=1
    serveT=""
    id_global=0
    instructions=[]
    nutrition=[]
    
    try:
        elem=driver.find_element(By.CLASS_NAME, 'wprm-recipe-instructions').find_elements(By.TAG_NAME, 'li')
        for e in elem:
            instructions.append(e.text)
    except:
        pass

    while True:
        try:

            id = driver.find_element_by_xpath('//*[@class="wprm-recipe-container"]').get_attribute("data-recipe-id")
            id_global = id
            # print(id)
            root = driver.find_element_by_xpath(xpath=f'//*[@id="wprm-recipe-container-{id}"]/div/div[12]/div/ul/li[{i}]')
            
            
     
            amount = getAmount(root)
            unit = getUnit(root)
            
            
            ing = root.find_element(By.CLASS_NAME, 'wprm-recipe-ingredient-name')
            serve=driver.find_element_by_xpath(f'//*[@id="wprm-recipe-container-{id}"]/div/div[8]/span[2]')
            date=driver.find_element_by_xpath('/html/head//meta[@property="article:published_time"]').get_attribute("content")


            month = int(date[5:7])
            if (datetime.today().month-1 == month):
                
                
                amountStr=""
                unitStr=""
                print(ing.text)
                if (amount is not None):
                    amountStr = amount.text
                    print(amount.text)
                if (unit is not None):
                    unitStr = unit.text
                    print(unit.text)
                # print(serve.text)
                

                ingredients.append(amountStr+' '+unitStr + ' ' + ing.text)
                serveT=serve.text
            # driver.implicitly_wait(10)
                i+=1
            else:
                return    
                
        except:
            break

    
# //*[@id="wprm-recipe-container-48965"]/div/div[13]/div/ul
    
    # mRoot = driver.find_element_by_xpath(xpath=f'//*[@id="wprm-recipe-container-{id_global}"]/div/div[13]/div/ul/li')
    # meth=getInstructions(mRoot, id)
    print(img)
    recipes.append([url, ingredients, serveT, img, instructions, nutrition])
    # with open('data.txt', 'w') as outfile:
        # json.dump(recipes, outfile)

    with open('data', 'wb') as fp:
        pickle.dump(recipes, fp)    


with webdriver.Chrome("C:/WebDriver/bin/chromedriver.exe", options=options) as driver:
    i=1
    wordlist = ["How"]
    recipes = []
    
    
    while True:
        driver.get('https://www.loveandlemons.com/recipes/main-dish-recipes/')
        if len(recipes)==5:
            break
        
        ERROR = False
        
        
        
        visibility = driver.find_element_by_xpath(f'//*[@id="recipeindex"]/li[{i}]').get_attribute('class')
        
        if 'visible'not in visibility:
            ERROR = True

        title = driver.find_element_by_xpath(f'//*[@id="recipeindex"]/li[{i}]/a/div[3]/div[1]').text
    

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
        
        # img = driver.find_element_by_xpath(f'//*[@id="recipeindex"]/li[{i}]/a/div[1]/img').get_attribute('src')
        img = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="recipeindex"]/li[{i}]/a/div[1]/img'))).get_attribute("src")

        
        parserecipe(driver.find_element_by_xpath(f'//*[@id="recipeindex"]/li[{i}]/a').get_attribute('href'), img)
        
        print("PARSED")
        
        i+=1

    # driver.navigate().back()

    
