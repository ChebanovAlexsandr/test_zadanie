import pytest

from config.data import Data

from pages.login_page import LoginPage
from pages.info_page import InfoPage
from pages.document_page import DocumentPage

class BaseTest:
    data: Data

    """Анатация типов"""
    login_page: LoginPage
    info_page: InfoPage
    document_page: DocumentPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.login_page = LoginPage(driver)
        request.cls.info_page = InfoPage(driver)
        request.cls.document_page = DocumentPage(driver)
