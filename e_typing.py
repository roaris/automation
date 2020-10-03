from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver = webdriver.Chrome('')
url =  'https://www.e-typing.ne.jp/app/jsa_std/typing.asp?t=trysc.trysc.trysc.std.0&u=&s=0'
driver.get(url)
sleep(2)

driver.find_element_by_xpath('//*[@id="start_btn"]').click()
sleep(2)

driver.find_element_by_xpath('/html').send_keys(Keys.SPACE)
sleep(3.5)

while True:
    try:
        target = driver.find_element_by_xpath('//*[@id="sentenceText"]/div/span[2]').text
        
        for c in target:
           driver.find_element_by_xpath('/html').send_keys(c)
        
        sleep(1.5)
    except NoSuchElementException:
        break