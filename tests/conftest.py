import os

import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Chụp màn hình sau mỗi test, lưu vào thư mục screenshots/."""
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        instance = getattr(item, "instance", None)
        d = getattr(instance, "driver", None)
        if d:
            os.makedirs("screenshots", exist_ok=True)
            kq = "PASS" if rep.passed else "FAIL"
            d.save_screenshot(f"screenshots/{item.name}_{kq}.png")