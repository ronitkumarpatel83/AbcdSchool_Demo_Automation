import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@then(u'Enter wrong Username and password')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="wpforo-wrap"]/div[3]/div[1]/'
                                          'div/div/div/form/div/div/div/div/div/'
                                          'div[1]/div[1]/input').clear()
    context.driver.find_element(By.XPATH, '//*[@id="wpforo-wrap"]/div[3]/div[1]/'
                                          'div/div/div/form/div/div/div/div/div/'
                                          'div[1]/div[1]/input').send_keys("ronitpatel")
    context.driver.find_element(By.XPATH, '//*[@id="wpforo-wrap"]/div[3]/div[1]/div/div/div/'
                                          'form/div/div/div/div/div/div[2]/div[1]/input').clear()
    context.driver.find_element(By.XPATH, '//*[@id="wpforo-wrap"]/div[3]/div[1]/div/div/div/'
                                          'form/div/div/div/div/div/div[2]/div[1]/input').send_keys("i dont know")


@then(u'Verify login is unsuccessful')
def step_impl(context):
    time.sleep(2)
    # check if there is Welcome! text in login page
    # i am using this text cause there isn't invalid message
    # after unsuccessful login in the top right corner pop-up a error message for 1 sec
    welcome_text = context.driver.find_element(By.XPATH, '//*[@id="wpforo-wrap"]/div[3]/div[1]/div/div/div/form/div/div/h3').text
    if welcome_text == "Welcome!":
        assert True, f"Logout : {welcome_text}"
    else:
        assert False, f"Logout : {welcome_text}"
