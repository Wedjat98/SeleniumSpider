from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
browser = webdriver.PhantomJS()
url = "https://store.steampowered.com/app/1660280/HIsekai_Loves/"
browser.get(url)
WebDriverWait(browser,10).until(lambda d : "Steam" in d.title)
key = browser.find_element(By.XPATH,'//*[@id="game_area_description"]')
print(key)
browser.close()
