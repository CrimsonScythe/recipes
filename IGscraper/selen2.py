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



def parserecipe(url, title,  img):
    # driver.get('https://www.loveandlemons.com/black-bean-burger-recipe/')
    
    driver.get(url)
    ingredients = []
    method = []
    i=1
    serveT=""
    timeis=""
    id_global=0
    instructions=[]
    nutrition=[]
    
    dates=driver.find_elements(By.TAG_NAME, 'meta')
    month=0
    for date in dates:
        if date.get_attribute('property')=='article:published_time':
            final = date.get_attribute('content')
    
            # print(date)

            fin = int(final[5:7])
            month=fin

# datetime.today().month-1 == month
    if (True):
        

        try:
            elem=driver.find_element(By.CLASS_NAME, 'tasty-recipes-instructions').find_elements(By.TAG_NAME, 'li')
            for e in elem:
                print(e.text)
                instructions.append(e.text)
        except:
            return

        try:
        
            id = driver.find_element_by_xpath('//*[@id="content"]/div[1]/a').get_attribute("href")
            ids=re.findall(r'\d+', id)
            id=ids[0]
            ingre = driver.find_element(By.CLASS_NAME, 'tasty-recipes-ingredients').find_elements(By.TAG_NAME, 'li')
            # elems = driver.find_element(By.XPATH, f'//*[@id="tasty-recipes-{id}"]/div/div[1]').find_elements(By.TAG_NAME, 'li')
            for ing in ingre:
                print(ing.text)
                ingredients.append(ing.text)

            serve=driver.find_element(By.CLASS_NAME, 'tasty-recipes-yield').find_elements(By.TAG_NAME, 'span')

            
            # serve=driver.find_element_by_xpath(f'//*[@id="tasty-recipes-{id}"]/header/div[2]/div[2]/ul/li[4]/span[2]/span[1]')
            serveT=serve[0].text
            print(serveT)
            # tim=driver.find_element_by_xpath(f'//*[@id="tasty-recipes-{id}"]/header/div[2]/div[2]/ul/li[3]/span[2]')
            # timeis=tim.text
            # //*[@id="tasty-recipes-71053"]/header/div[2]/div[2]/ul/li[4]/span[2]
            # //*[@id="tasty-recipes-73229"]/header/div[2]/div[2]/ul/li[4]/span[2]
            # //*[@id="tasty-recipes-71053"]/header/div[2]/div[2]/ul/li[4]/span[2]
            
            tim=driver.find_element(By.CLASS_NAME, 'tasty-recipes-total-time')
            # tim=driver.find_element(By.CLASS_NAME, 'total-time').find_elements(By.TAG_NAME, 'span')
            # tim=driver.find_element(By.CLASS_NAME, 'tasty-recipes-total-time')
            timeis=tim.text
            print(timeis)
        except:
            # print(er)
            return

        
# //*[@id="tasty-recipes-73229"]/div/div[2]/ul/li[1]
        

        # print(img)
        recipes.append([title, url, ingredients, serveT, img, instructions, nutrition, timeis, 'all'])
        # with open('data.txt', 'w') as outfile:
            # json.dump(recipes, outfile)

        with open('data2', 'wb') as fp:
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
    
    # https://www.gimmesomeoven.com/all-recipes/?fwp_course=main-course&fwp_per_page=100
    while True:

        # if len(recipes)==5:
        #     break

        if num==4:
            break

        driver.get('https://www.gimmesomeoven.com/all-recipes/?fwp_course=main-course&fwp_paged={num}&fwp_per_page=100')
        
        
        ERROR = False
        
        
        
        # visibility = driver.find_element_by_xpath(f'//*[@id="recipeindex"]/li[{i}]').get_attribute('class')
        
        # if 'visible'not in visibility:
        #     ERROR = True

        try:
            title = driver.find_element_by_xpath(f'//*[@id="content"]/div[2]/div[{i}]/a').get_attribute('title')
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
        
        img = driver.find_element_by_xpath(f'//*[@id="content"]/div[2]/div[{i}]/a/img').get_attribute('src')
        # img = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="recipeindex"]/li[{i}]/a/div[1]/img'))).get_attribute("src")

        
        parserecipe(driver.find_element_by_xpath(f'//*[@id="content"]/div[2]/div[{i}]/a').get_attribute('href'), title, img)
        
        print("PARSED")
        
        i+=1

    # driver.navigate().back()

    
