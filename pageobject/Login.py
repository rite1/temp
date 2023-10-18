from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
    baseurl="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    Webelemnt_username="username"
    Webelemnt_password="password"

    def __init__(self,driver):
        self.driver=driver

    def Set_username(self,username):
        self.driver.find_element(By.NAME,self.Webelemnt_username).send_keys("username")

    def Set_password(self,password):
        self.driver.find_element(By.NAME,self.Webelemnt_password).send_keys("password")

    def Set_Btn(self):
        self.driver.find_element(By.TAG_NAME, "#button").click()


