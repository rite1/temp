from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageobject.Login import Login
from selenium import webdriver
import pytest
from selenium.webdriver.support import expected_conditions as ec
class Test_login:
    baseurl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    usn="Admin"
    pwd="admin123"
    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=Login(self.driver)

        self.driver.implicitly_wait(10)
        self.lp.Set_username(self.usn)
        self.lp.Set_password(self.pwd)
        self.lp.Set_Btn()
        wait=WebDriverWait(self.driver,10)
        ele=wait.until(ec.element_to_be_clickable(By.TAG_NAME,"#button"))
