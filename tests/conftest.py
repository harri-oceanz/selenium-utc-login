import os

import pytest
from selenium import webdriver

from pages.login_page import LoginPage


@pytest.fixture
def driver():
    """Mở Chrome mới (phiên sạch) cho mỗi test, đóng lại khi xong."""
    d = webdriver.Chrome()
    d.maximize_window()
    yield d
    d.quit()


@pytest.fixture
def login_page(driver):
    """Mở sẵn trang đăng nhập."""
    page = LoginPage(driver)
    page.open()
    return page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Chụp màn hình sau mỗi test, lưu vào thư mục screenshots/."""
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        d = item.funcargs.get("driver")
        if d:
            os.makedirs("screenshots", exist_ok=True)
            kq = "PASS" if rep.passed else "FAIL"
            d.save_screenshot(f"screenshots/{item.name}_{kq}.png")