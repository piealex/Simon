#from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#ser = Service("/Users/piealex/Simon/chromedriver")
ser = Service("./chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

#chromedriver = "/Users/piealex/Simon"

#driver = webdriver.Chrome(executable_path='/Users/piealex/Simon/chromedriver')

#driver = webdriver.Chrome(chromedriver)

#opening a webpage

#driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")

driver.quit()