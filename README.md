Repository này chứa mã nguồn dự án bài tập môn Kiểm thử Phần mềm, tập trung vào việc tự động hóa kiểm thử các kịch bản đăng nhập thất bại trên hệ thống Văn phòng điện tử UTC. Dự án được thiết kế theo mô hình Page Object Model (POM) để tối ưu hóa việc bảo trì và mở rộng code.🛠 Công nghệ sử dụngNgôn ngữ: Python 3.13Framework kiểm thử: Selenium WebDriver 4, pytestTrình duyệt: Google Chrome (Tự động quản lý ChromeDriver)Kiến trúc thiết kế: Page Object Model (POM)📁 Cấu trúc thư mụcDự án được phân chia rõ ràng giữa phần thiết lập, cấu hình trang và kịch bản test:Plaintextselenium-utc-login/
├── base/
│   └── base_test.py        # Cấu hình khởi tạo WebDriver, thiết lập timeout chung
├── pages/                  # Lớp Page Object quản lý giao diện
│   ├── base_page.py        # Các hàm thao tác chung (wait, click, send_keys,...)
│   └── login_page.py       # Định nghĩa các Elements và hành động trên form Đăng nhập
├── tests/                  # Kịch bản kiểm thử (Test Scripts)
│   ├── conftest.py         # Hooks của pytest (hỗ trợ chụp ảnh màn hình tự động)
│   └── test_login_e2e.py   # 12 Test case kiểm tra luồng đăng nhập thất bại (E2E)
├── docs/
│   └── TestCase_Login_UTC.xlsx  # Bảng thiết kế Test Case chi tiết
├── pytest.ini              # File cấu hình tùy chỉnh cho pytest
└── requirements.txt        # Danh sách thư viện cần thiết
⚙️ Cài đặt & Môi trườngYêu cầu hệ thống: Máy tính cần được cài đặt sẵn Google Chrome và Python 3.13+.Clone repository:Bashgit clone https://github.com/hkdung2005-tech/selenium-utc-login.git
cd selenium-utc-login
Cài đặt thư viện:Nên tạo môi trường ảo (virtual environment) trước khi cài đặt:Bashpip install -r requirements.txt
🚀 Hướng dẫn chạy TestHệ thống được cấu hình để tự động chụp ảnh màn hình sau mỗi test case. Các file ảnh kết quả sẽ được lưu tại thư mục screenshots/ với hậu tố _PASS.png hoặc _FAIL.png.Chạy toàn bộ bộ kiểm thử (12 Test Cases):Bashpytest -v
Chạy một Test Case cụ thể (Ví dụ: TC03):Bashpytest -v -k tc03
🧪 Danh sách Test CaseChi tiết về các bước thực hiện (Steps) và Kết quả mong đợi (Expected Output) được đính kèm trong file docs/TestCase_Login_UTC.xlsx.IDMô tả Kịch bản Kiểm thửKỹ thuật Thiết kế Test CaseTC01Để trống trường UsernamePhân lớp tương đươngTC02Để trống trường PasswordPhân lớp tương đươngTC03Nhập đúng Username, sai PasswordPhân lớp tương đươngTC04Nhập sai Username, đúng PasswordPhân lớp tương đươngTC05Để trống cả Username và PasswordPhân lớp tương đươngTC06Username chỉ chứa ký tự khoảng trắng (Space)Đoán lỗi (Error Guessing)TC07Password chỉ chứa ký tự khoảng trắng (Space)Đoán lỗi (Error Guessing)TC08Username viết hoa toàn bộ ký tựĐoán lỗi (Error Guessing)TC09Password nhập sai định dạng chữ Hoa/ThườngĐoán lỗi (Error Guessing)TC10Username chứa các ký tự đặc biệtĐoán lỗi (Error Guessing)TC11Username vượt ngưỡng giới hạn (100 ký tự)Phân tích giá trị biênTC12Password vượt ngưỡng giới hạn (100 ký tự)Phân tích giá trị biên📌 Quy ước Commit CodeDự án áp dụng quy chuẩn quản lý phiên bản nghiêm ngặt. Mỗi test case khi hoàn thiện sẽ được tạo một commit độc lập để dễ dàng theo dõi và rollback khi cần:Cú pháp: Add TC<id>: <Mô gọn ngắn tả>Ví dụ: Add TC01: Kịch bản để trống username
