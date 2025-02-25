import allure
import pytest

from base.base_test import BaseTest


class TestE2E(BaseTest):
    @allure.title("Test_E2E")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.info_page.is_opened()
        self.info_page.click_documents_and_scans_menu()
        self.document_page.is_opened()
        self.document_page.document_search_by_parameters("R029256118")
        self.document_page.search_button()
        self.document_page.save()
        self.document_page.get_screenshot()

