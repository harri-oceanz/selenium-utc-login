"""Các test case đăng nhập THẤT BẠI trên vanphongdientu.utc.edu.vn."""
import pytest

from base.base_test import BaseTest
from pages.login_page import LoginPage, MSG_THIEU_USER, MSG_THIEU_PASS, MSG_SAI


class TestLoginE2E(BaseTest):

    @pytest.fixture(autouse=True)
    def init_page(self, init_driver):
        """Mở sẵn trang đăng nhập trước mỗi test."""
        self.login_page = LoginPage(self.driver)
        self.login_page.open_page()

    def check_login_failed(self, user, pwd, messages):
        """Đăng nhập rồi kiểm tra: có thông báo lỗi và vẫn ở trang đăng nhập."""
        self.login_page.login(user, pwd)
        assert self.login_page.has_message(messages), "Không thấy thông báo lỗi mong đợi"
        assert self.login_page.still_on_login(), "Không được vào trang chủ"

    # ---------------------------------------------------------------
    # Loại test case: Phân lớp tương đương (lớp không hợp lệ: username rỗng)
    # ---------------------------------------------------------------
    def test_tc01_de_trong_username(self):
        """TC01: Để trống username, nhập password 1256 -> báo chưa nhập tên đăng nhập."""
        self.check_login_failed("", "1256", [MSG_THIEU_USER])

    # ---------------------------------------------------------------
    # Loại test case: Phân lớp tương đương (lớp không hợp lệ: password rỗng)
    # ---------------------------------------------------------------
    def test_tc02_de_trong_password(self):
        """TC02: Nhập username huongnt, để trống password -> báo chưa nhập mật khẩu."""
        self.check_login_failed("huongnt", "", [MSG_THIEU_PASS])

    # ---------------------------------------------------------------
    # Loại test case: Phân lớp tương đương (username đúng, password sai)
    # ---------------------------------------------------------------
    def test_tc03_dung_ten_sai_mat_khau(self):
        """TC03: Username đúng huongnt, password sai utc@235 -> tài khoản hoặc mật khẩu không đúng."""
        self.check_login_failed("huongnt", "utc@235", [MSG_SAI])

    # ---------------------------------------------------------------
    # Loại test case: Phân lớp tương đương (username sai, password đúng)
    # ---------------------------------------------------------------
    def test_tc04_sai_ten_dung_mat_khau(self):
        """TC04: Username sai huongthunguyen, password đúng 123456@utc -> báo sai tài khoản."""
        self.check_login_failed("huongthunguyen", "123456@utc", [MSG_SAI])

    # ---------------------------------------------------------------
    # Loại test case: Phân lớp tương đương (cả hai ô cùng rỗng)
    # ---------------------------------------------------------------
    def test_tc05_de_trong_ca_hai(self):
        """TC05: Để trống cả username và password -> báo chưa nhập tên đăng nhập."""
        self.check_login_failed("", "", [MSG_THIEU_USER])

    # ---------------------------------------------------------------
    # Loại test case: Đoán lỗi (Error Guessing) - username chỉ có khoảng trắng
    # ---------------------------------------------------------------
    def test_tc06_username_khoang_trang(self):
        """TC06: Username toàn khoảng trắng, password đúng -> không được đăng nhập."""
        self.check_login_failed("   ", "123456@utc", [MSG_THIEU_USER, MSG_SAI])

    # ---------------------------------------------------------------
    # Loại test case: Đoán lỗi (Error Guessing) - password chỉ có khoảng trắng
    # ---------------------------------------------------------------
    def test_tc07_password_khoang_trang(self):
        """TC07: Username đúng, password toàn khoảng trắng -> không được đăng nhập."""
        self.check_login_failed("huongnt", "   ", [MSG_THIEU_PASS, MSG_SAI])

    # ---------------------------------------------------------------
    # Loại test case: Đoán lỗi (Error Guessing) - phân biệt chữ hoa/thường ở username
    # ---------------------------------------------------------------
    def test_tc08_username_viet_hoa(self):
        """TC08: Username viết hoa HUONGNT, password đúng -> báo sai tài khoản."""
        self.check_login_failed("HUONGNT", "123456@utc", [MSG_SAI])

    # ---------------------------------------------------------------
    # Loại test case: Đoán lỗi (Error Guessing) - phân biệt chữ hoa/thường ở password
    # ---------------------------------------------------------------
    def test_tc09_password_sai_hoa_thuong(self):
        """TC09: Username đúng, password sai chữ hoa 123456@UTC -> báo sai tài khoản."""
        self.check_login_failed("huongnt", "123456@UTC", [MSG_SAI])

    # ---------------------------------------------------------------
    # Loại test case: Đoán lỗi (Error Guessing) - ký tự đặc biệt
    # ---------------------------------------------------------------
    def test_tc10_username_ky_tu_dac_biet(self):
        """TC10: Username chứa ký tự đặc biệt huong@#$% -> báo sai tài khoản."""
        self.check_login_failed("huong@#$%", "123456@utc", [MSG_SAI])

    # ---------------------------------------------------------------
    # Loại test case: Phân tích giá trị biên (username vượt độ dài thông thường)
    # ---------------------------------------------------------------
    def test_tc11_username_qua_dai(self):
        """TC11: Username dài 100 ký tự, password đúng -> báo sai tài khoản, trang không lỗi."""
        self.check_login_failed("a" * 100, "123456@utc", [MSG_SAI])

    # ---------------------------------------------------------------