import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'launch chrome browser')
def step_impl(context):
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(options=options)
    context.driver.maximize_window()
    time.sleep(2)


@when(u'open AbcdSchool forum')
def step_impl(context):
    context.driver.get("https://kcc.aptcoder.com/community/")


@then(u'verify login page with login keyword')
def step_impl(context):
    time.sleep(2)
    context.driver.implicitly_wait(0.5)
    login = context.driver.find_element(By.XPATH, "//*[@id='menu-item-2386']/a")
    context.driver.execute_script("arguments[0].click();", login)


@then(u'Enter Username and password')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="wpforo-wrap"]/div[3]/div[1]/'
                                                     'div/div/div/form/div/div/div/div/div/'
                                                     'div[1]/div[1]/input').clear()
    context.driver.find_element(By.XPATH, '//*[@id="wpforo-wrap"]/div[3]/div[1]/'
                                          'div/div/div/form/div/div/div/div/div/'
                                          'div[1]/div[1]/input').send_keys("ronitsdet")
    context.driver.find_element(By.XPATH, '//*[@id="wpforo-wrap"]/div[3]/div[1]/div/div/div/'
                                          'form/div/div/div/div/div/div[2]/div[1]/input').clear()
    context.driver.find_element(By.XPATH, '//*[@id="wpforo-wrap"]/div[3]/div[1]/div/div/div/'
                                          'form/div/div/div/div/div/div[2]/div[1]/input').send_keys("Python@12345")


@then(u'Click on login button')
def step_impl(context):
    time.sleep(2)
    login_button = context.driver.find_element(By.XPATH, '//*[@id="wpforo-wrap"]/div[3]/div[1]/div/div/div/'
                                                         'form/div/div/div/div/div/div[5]/div[1]/input')
    context.driver.execute_script("arguments[0].click();", login_button)


@then(u'Verify login successful or not')
def step_impl(context):
    time.sleep(2)
    # check if there is logout button that means we are successfully login
    text = context.driver.find_element(By.XPATH, '//*[@id="menu-item-2387"]/a').text
    if text == "Logout":
        assert True, f"Logout : {text}"
    else:
        assert False, f"Logout : {text}"


@then(u'close browser')
def step_impl(context):
    time.sleep(1)
    context.driver.close()
