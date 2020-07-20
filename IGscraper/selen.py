from selenium import webdriver
import json
import time
import pickle
from selenium.webdriver.common.by import By
from datetime import datetime
import regex as re

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



def parserecipe(url):
    # driver.get('https://www.loveandlemons.com/black-bean-burger-recipe/')
    driver.get(url)
    ingredients = []
    method = []
    i=1

    while True:
        try:

            id = driver.find_element_by_xpath('//*[@class="wprm-recipe-container"]').get_attribute("data-recipe-id")
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

            # driver.implicitly_wait(10)
                i+=1
            else:
                return    
                
        except:
            break

    
    recipes.append([url, ingredients, serve.text])
    with open('data.txt', 'w') as outfile:
        json.dump(recipes, outfile)


with webdriver.Chrome("C:/WebDriver/bin/chromedriver.exe", options=options) as driver:
    i=1
    wordlist = ["How"]
    recipes = []
    
    
    while True:
        driver.get('https://www.loveandlemons.com/recipes/main-dish-recipes/')
        if i==15 or len(recipes)==1:
            break
        
        ERROR = False
        
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
        
        parserecipe(driver.find_element_by_xpath(f'//*[@id="recipeindex"]/li[{i}]/a').get_attribute('href'))
        print("PARSED")
        
        i+=1

    # driver.navigate().back()

    
