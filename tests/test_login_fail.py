"""Các test case đăng nhập THẤT BẠI trên vanphongdientu.utc.edu.vn."""
from pages.login_page import MSG_THIEU_USER, MSG_THIEU_PASS, MSG_SAI


# ---------------------------------------------------------------
# Loại test case: Phân lớp tương đương (lớp không hợp lệ: username rỗng)
# ---------------------------------------------------------------
def test_tc01_de_trong_username(login_page):
    """TC01: Để trống username, nhập password 1256 -> báo chưa nhập tên đăng nhập."""
    login_page.login("", "1256")
    assert login_page.has_message([MSG_THIEU_USER]), "Không thấy thông báo thiếu username"
    assert login_page.still_on_login(), "Không được vào trang chủ"

# ---------------------------------------------------------------
# Loại test case: Phân lớp tương đương (lớp không hợp lệ: password rỗng)
# ---------------------------------------------------------------
def test_tc02_de_trong_password(login_page):
    """TC02: Nhập username huongnt, để trống password -> báo chưa nhập mật khẩu."""
    login_page.login("huongnt", "")
    assert login_page.has_message([MSG_THIEU_PASS]), "Không thấy thông báo thiếu password"
    assert login_page.still_on_login(), "Không được vào trang chủ"