import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class InfoPage(BasePage):

    PAGE_URL = Links.INFO_PAGE

    DOCUMENTS_AND_SCAN_MENU_BUTTON = ("xpath", '//*[@id="documents-and-scans-menu"]')

    @allure.step("Click_documents_and_scans_menu")
    def click_documents_and_scans_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.DOCUMENTS_AND_SCAN_MENU_BUTTON)).click()
