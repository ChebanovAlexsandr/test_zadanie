

import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class DocumentPage(BasePage):
    PAGE_URL = Links.DOCUMENT_PAGE

    BARCODE = ("xpath", '//input[@data-placeholder="Штрих-код документа"]')
    SEARCH_BUTTON = ("xpath", '//*[@id="search-dialog-button-search"]')
    BURGER_MENU = ("xpath", '//*[@id="data-table-menu-button"]')
    SAVE_DOCUMENT = ("xpath", '//*[@id="context-menu-parent-button"]')
    SAVE_DOCUMENT_2 = ("xpath", '//*[@id="context-menu-item-button"][5]')
    COPY_LINK = ("xpath", '//*[@id="link-download-dialog-value"]')
    MASSAGE = ("xpath", '//*[@id="snack-bar-message"]')

    def document_search_by_parameters(self, barcode):
        with allure.step(f"Search by '{barcode}'"):
            barcode_document = self.wait.until(EC.element_to_be_clickable(self.BARCODE))
            barcode_document.send_keys(barcode)

    @allure.step("Search click")
    def search_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()

    @allure.step("Save document")
    def save(self):
        self.wait.until(EC.element_to_be_clickable(self.BURGER_MENU)).click()
        self.wait.until(EC.element_to_be_clickable(self.SAVE_DOCUMENT)).click()
        self.wait.until(EC.element_to_be_clickable(self.SAVE_DOCUMENT_2)).click()
        link = self.wait.until(EC.visibility_of_element_located(self.COPY_LINK))
        self.driver.get(link.text)
        massage = self.wait.until(EC.visibility_of_element_located(self.MASSAGE))
        assert massage.text == "Документ загружен", "Документ не загружен"


