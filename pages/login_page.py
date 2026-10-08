from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://vanphongdientu.utc.edu.vn/Login"

# Thông báo mong đợi (theo slide của thầy). Nếu trang thật ghi khác thì sửa ở đây.
MSG_THIEU_USER = "Bạn chưa nhập tên đăng nhập"
MSG_THIEU_PASS = "Bạn chưa nhập mật khẩu"
MSG_SAI = "Tài khoản không đúng"


class LoginPage:
    """Các thao tác trên trang đăng nhập."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(URL)
        self.wait.until(EC.presence_of_element_located((By.NAME, "username")))

    def login(self, user, pwd):
        ou = self.driver.find_element(By.NAME, "username")
        op = self.driver.find_element(By.NAME, "userpwd")
        ou.click()
        ou.send_keys(user)
        op.click()
        op.send_keys(pwd)
        self.driver.find_element(By.XPATH, "//input[@value='Đăng nhập']").click()

    def page_text(self):
        return self.driver.find_element(By.TAG_NAME, "body").text

    def has_message(self, messages, timeout=5):
        """True nếu trang hiện một trong các thông báo trong danh sách."""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: any(m in self.page_text() for m in messages))
            return True
        except TimeoutException:
            return False

    def still_on_login(self):
        """True nếu vẫn ở trang đăng nhập (chưa vào được trang chủ)."""
        return ("Login" in self.driver.current_url
                and len(self.driver.find_elements(By.NAME, "userpwd")) > 0)