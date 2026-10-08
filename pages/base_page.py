from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

DEFAULT_TIMEOUT = 10  # giây


class BasePage:
    """Thao tác chung cho mọi page: wait, click, type..."""

    def __init__(self, driver, timeout=DEFAULT_TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        element = self.find(locator)
        element.click()
        element.send_keys(text)

    def page_text(self):
        return self.driver.find_element(By.TAG_NAME, "body").text

    def page_contains_any(self, messages, timeout=5):
        """True nếu trang hiện một trong các thông báo trong danh sách."""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: any(m in self.page_text() for m in messages))
            return True
        except TimeoutException:
            return False