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

# ---------------------------------------------------------------
# Loại test case: Đoán lỗi (Error Guessing) - phân biệt chữ hoa/thường ở username
# ---------------------------------------------------------------
def test_tc08_username_viet_hoa(login_page):
    """TC08: Username viết hoa HUONGNT, password đúng -> tài khoản không đúng."""
    login_page.login("HUONGNT", "123456@utc")
    assert login_page.has_message([MSG_SAI]), "Không thấy thông báo tài khoản không đúng"
    assert login_page.still_on_login(), "Không được vào trang chủ"

# ---------------------------------------------------------------
# Loại test case: Đoán lỗi (Error Guessing) - phân biệt chữ hoa/thường ở password
# ---------------------------------------------------------------
def test_tc09_password_sai_hoa_thuong(login_page):
    """TC09: Username đúng, password sai chữ hoa 123456@UTC -> tài khoản không đúng."""
    login_page.login("huongnt", "123456@UTC")
    assert login_page.has_message([MSG_SAI]), "Không thấy thông báo tài khoản không đúng"
    assert login_page.still_on_login(), "Không được vào trang chủ"

# ---------------------------------------------------------------
# Loại test case: Đoán lỗi (Error Guessing) - ký tự đặc biệt
# ---------------------------------------------------------------
def test_tc10_username_ky_tu_dac_biet(login_page):
    """TC10: Username chứa ký tự đặc biệt huong@#$% -> tài khoản không đúng."""
    login_page.login("huong@#$%", "123456@utc")
    assert login_page.has_message([MSG_SAI]), "Không thấy thông báo tài khoản không đúng"
    assert login_page.still_on_login(), "Không được vào trang chủ"

# ---------------------------------------------------------------
# Loại test case: Phân tích giá trị biên (username vượt độ dài thông thường)
# ---------------------------------------------------------------
def test_tc11_username_qua_dai(login_page):
    """TC11: Username dài 100 ký tự, password đúng -> tài khoản không đúng, trang không lỗi."""
    login_page.login("a" * 100, "123456@utc")
    assert login_page.has_message([MSG_SAI]), "Không thấy thông báo tài khoản không đúng"
    assert login_page.still_on_login(), "Không được vào trang chủ"

# ---------------------------------------------------------------
# Loại test case: Phân tích giá trị biên (password vượt độ dài thông thường)
# ---------------------------------------------------------------
def test_tc12_password_qua_dai(login_page):
    """TC12: Username đúng, password dài 100 ký tự -> tài khoản không đúng, trang không lỗi."""
    login_page.login("huongnt", "a" * 100)
    assert login_page.has_message([MSG_SAI]), "Không thấy thông báo tài khoản không đúng"
    assert login_page.still_on_login(), "Không được vào trang chủ"