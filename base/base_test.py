import pytest
from selenium import webdriver

PAGE_LOAD_TIMEOUT = 30  # giây


class BaseTest:
    """Lớp cha của mọi test: khởi tạo và đóng WebDriver."""

    @pytest.fixture(autouse=True)
    def init_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
        yield
        self.driver.quit()