
import subprocess
import sys

# لیست کتابخانه‌های موردنیاز
required_libraries = [
    "python-telegram-bot==20.3",
    "pytz",
    "python-dotenv"
]

def install_and_import(package):
    try:
        __import__(package.split('==')[0])  # تلاش برای ایمپورت کتابخانه
    except ImportError:
        print(f"{package} در حال نصب است...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])  # نصب کتابخانه

if __name__ == "__main__":
    for lib in required_libraries:
        install_and_import(lib)
    print("تمام کتابخانه‌ها نصب شدند و آماده هستند.")
