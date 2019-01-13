from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

driver=webdriver.Chrome("/Users/tanmayarora/Downloads/chromedriver")

driver.get("https://tinder.com/")
driver.maximize_window()

time.sleep(3)

driver.find_element_by_xpath("//*[@id='modal-manager']/div/div/div[2]/div/div[3]/div[2]/button").click()

time.sleep(2)

search1=driver.find_element_by_name("phone_number")
#search1.click()
time.sleep(1)

search1.send_keys("8826232880")

time.sleep(1)

driver.find_element_by_xpath("//*[@id='modal-manager']/div/div/div[2]/button/span").click()
#above clicks the continue button after entering the phone number

time.sleep(20)

driver.find_element_by_xpath("//*[@id='modal-manager']/div/div/div[2]/button").click()

time.sleep(8)

driver.find_element_by_xpath("//*[@id='content']/div/span/div/div[2]/div/div/div[3]/button[1]").click()

time.sleep(1)

driver.find_element_by_xpath("//*[@id='content']/div/span/div/div[2]/div/div/div[3]/button[1]/span").click()

time.sleep(20)

for i in range(30):
	#driver.find_element_by_xpath("//*[@id='content']/div/span/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[4]/span/svg/g/g/path").click()
	#driver.find_element_by_css_selector("button__text.Pos(r).Z(1)").click()
	driver.find_element_by_css_selector('body').send_keys(Keys.RIGHT)
	time.sleep(3)

time.sleep(50)


#driver.quit()
