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

# ---------------------------------------------------------------
# Loại test case: Phân lớp tương đương (username đúng, password sai)
# ---------------------------------------------------------------
def test_tc03_dung_ten_sai_mat_khau(login_page):
    """TC03: Username đúng huongnt, password sai utc@235 -> tài khoản không đúng."""
    login_page.login("huongnt", "utc@235")
    assert login_page.has_message([MSG_SAI]), "Không thấy thông báo tài khoản không đúng"
    assert login_page.still_on_login(), "Không được vào trang chủ"

# ---------------------------------------------------------------
# Loại test case: Phân lớp tương đương (username sai, password đúng)
# ---------------------------------------------------------------
def test_tc04_sai_ten_dung_mat_khau(login_page):
    """TC04: Username sai huongthunguyen, password đúng 123456@utc -> tài khoản không đúng."""
    login_page.login("huongthunguyen", "123456@utc")
    assert login_page.has_message([MSG_SAI]), "Không thấy thông báo tài khoản không đúng"
    assert login_page.still_on_login(), "Không được vào trang chủ"

# ---------------------------------------------------------------
# Loại test case: Phân lớp tương đương (cả hai ô cùng rỗng)
# ---------------------------------------------------------------
def test_tc05_de_trong_ca_hai(login_page):
    """TC05: Để trống cả username và password -> báo chưa nhập tên đăng nhập."""
    login_page.login("", "")
    assert login_page.has_message([MSG_THIEU_USER]), "Không thấy thông báo thiếu username"
    assert login_page.still_on_login(), "Không được vào trang chủ"

# ---------------------------------------------------------------
# Loại test case: Đoán lỗi (Error Guessing) - username chỉ có khoảng trắng
# ---------------------------------------------------------------
def test_tc06_username_khoang_trang(login_page):
    """TC06: Username toàn khoảng trắng, password đúng -> không được đăng nhập."""
    login_page.login("   ", "123456@utc")
    assert login_page.has_message([MSG_THIEU_USER, MSG_SAI]), "Không thấy thông báo lỗi"
    assert login_page.still_on_login(), "Không được vào trang chủ"

# ---------------------------------------------------------------
# Loại test case: Đoán lỗi (Error Guessing) - password chỉ có khoảng trắng
# ---------------------------------------------------------------
def test_tc07_password_khoang_trang(login_page):
    """TC07: Username đúng, password toàn khoảng trắng -> không được đăng nhập."""
    login_page.login("huongnt", "   ")
    assert login_page.has_message([MSG_THIEU_PASS, MSG_SAI]), "Không thấy thông báo lỗi"
    assert login_page.still_on_login(), "Không được vào trang chủ"