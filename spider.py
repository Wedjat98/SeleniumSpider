from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(chrome_options=options)
url1 = "https://store.steampowered.com/app/1660280/HIsekai_Loves/"
url2 = "https://store.steampowered.com/news/app/1660280/view/5293421584000418585"
browser.get(url1)
WebDriverWait(browser, 3).until(lambda d: "Steam" in d.title)
key1 = browser.find_element(By.XPATH, '//*[@id="game_area_description"]')
# print(key.text)
with open('key1.txt', mode="w") as f:
    f.write(key1.text)
    f.close()
browser.get(url2)
WebDriverWait(browser, 3).until(lambda d: "Steam" in d.title)
key2 = browser.find_element(By.XPATH, '//*[@id="application_root"]/div/div/div[3]/div[2]/div[1]/div[3]/div[1]/div')
# print(key.text)
with open('key2.txt', mode="wb+") as f:
    f.write(key2.text.encode("utf-8"))
    f.close()
browser.close()
# what
