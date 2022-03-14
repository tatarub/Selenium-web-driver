from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions, wait
from selenium.webdriver.common.by import By

driver = Chrome()

driver.get('https://www.google.ro/')
link = driver.find_element_by_id('L2AGLb')
link.click()

findField = driver.find_element_by_name("q")
findField.send_keys("facebook")
findField.submit()

connect = driver.find_element_by_partial_link_text("Conectare")
connect.click()

coockie = driver.find_element_by_id("accept-cookie-banner-label")
coockie.click()

usernameField = driver.find_element_by_id("m_login_email")
passwordField = driver.find_element_by_id("m_login_password")
 
usernameField.send_keys("maeia4343@gmail.com")
passwordField.send_keys("bfnfnfnfdd")

connectf = driver.find_element_by_name("login")
connectf.click()

wait = WebDriverWait(driver,20)
wait.until(expected_conditions.element_to_be_clickable((By.ID, 'dismiss_link')))

errorMessage = driver.find_element_by_class_name("_52je")
driver.get_screenshot_as_file('proof.png')
assert errorMessage.text == "Ai nevoie de ajutor să-ţi găseşti contul?"


