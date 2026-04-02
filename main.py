# main.py
import sys
import os

# Ép Python nhận diện thư mục gốc (Nơi chứa file main.py)
if getattr(sys, 'frozen', False):
    # Nếu chạy bằng file .exe
    ROOT_DIR = sys._MEIPASS
else:
    # Nếu chạy bằng code .py
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Đưa thư mục gốc lên ưu tiên số 1 khi tìm kiếm module
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# Bây giờ mới import các thư viện
import tkinter as tk
from services.updater import check_and_update
from ui.app_window import MucLucApp

def run():
    # Kiểm tra bản cập nhật ngầm lúc mở App
    check_and_update(is_manual=False)
    
    root = tk.Tk()
    app = MucLucApp(root)
    root.mainloop()

if __name__ == "__main__":
    run()