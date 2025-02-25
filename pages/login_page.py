import time

import allure

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    USERNAME_FIELD = ("xpath", '//input[@id="loginform-username-input"]')
    PASSWORD_FIELD = ("xpath", '//input[@id="loginform-password-input"]')
    SUBMIT_BUTTON = ("xpath", '//button[@id="loginform-enter-button"]')

    @allure.step("Enter_login")
    def enter_login(self, login):  # Шаг заполнения поля логин, принемаеть в себя логин
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)

    @allure.step("Enter_password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step("Enter_button")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
