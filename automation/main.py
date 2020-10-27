
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
import requests
import json

browser1 = webdriver.Chrome()

def main():
    
        browser1.get('https://www.instagram.com/accounts/emailsignup/')
        time.sleep(0.25)
        
        browser1.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()
        time.sleep(0.25)
      

        browser1.execute_script("window.open('');")
        browser1.switch_to.window(browser1.window_handles[1])
        browser1.get('https://www.fakemail.net/')
        time.sleep(1)
        email = browser1.find_element_by_xpath('//*[@id="email"]').text
        print(email)
        time.sleep(0.25)


        response1 = requests.get("https://api.namefake.com/")
        response2 = requests.get("https://www.random.org/integers/?num=1&min=1&max=100&col=1&base=10&format=plain&rnd=new")
        response3 = requests.get("https://randomuser.me/api/")
        

        browser1.switch_to.window(browser1.window_handles[0])
        browser1.find_element_by_name('emailOrPhone').send_keys(email)
        browser1.find_element_by_name('fullName').send_keys(response1.json()['name'])
        browser1.find_element_by_name('username').send_keys(response3.json()['results'][0]['login']['username'], response2.json())
        browser1.find_element_by_name('password').send_keys('password123')
        time.sleep(1)
        browser1.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[7]/div/button').click()
        
        time.sleep(1)
        select = Select(browser1.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[1]/select'))
        time.sleep(0.25)
        select.select_by_value('1')
        time.sleep(0.25)
        select2 = Select(browser1.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select'))
        time.sleep(0.25)
        select2.select_by_value('1')
        time.sleep(0.25)
        select3 = Select(browser1.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select'))
        time.sleep(0.25)
        select3.select_by_value('1990')
        time.sleep(1)
        
        browser1.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/div[6]/button').click()
        
        time.sleep(10)
        browser1.switch_to.window(browser1.window_handles[-1])
        time.sleep(5)
        browser1.get('https://www.fakemail.net/')
        time.sleep(0.25)
        code = browser1.find_element_by_xpath('//*[@id="schranka"]/tr[1]/td[2]').text
        final_code = code[:6]
        print(code)

        
        time.sleep(1)
        browser1.switch_to.window(browser1.window_handles[0])

        time.sleep(1)
        browser1.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div[2]/form/div/div[1]/input').send_keys(final_code)
        browser1.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div[2]/form/div/div[2]').click()
        
main()
