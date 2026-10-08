from selenium.webdriver.common.by import By

from pages.base_page import BasePage

URL = "https://vanphongdientu.utc.edu.vn/Login"

# Thông báo lỗi của trang
MSG_THIEU_USER = "Bạn chưa nhập tên đăng nhập"
MSG_THIEU_PASS = "Bạn chưa nhập mật khẩu"
MSG_SAI = "Tài khoản hoặc mật khẩu không đúng"


class LoginPage(BasePage):
    """Form đăng nhập."""

    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "userpwd")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Đăng nhập']")

    def open_page(self):
        self.open(URL)
        self.find(self.USERNAME)

    def login(self, user, pwd):
        self.type(self.USERNAME, user)
        self.type(self.PASSWORD, pwd)
        self.click(self.LOGIN_BUTTON)

    def has_message(self, messages, timeout=5):
        return self.page_contains_any(messages, timeout)

    def still_on_login(self):
        """True nếu vẫn ở trang đăng nhập (chưa vào được trang chủ)."""
        return ("Login" in self.driver.current_url
                and len(self.find_all(self.PASSWORD)) > 0)