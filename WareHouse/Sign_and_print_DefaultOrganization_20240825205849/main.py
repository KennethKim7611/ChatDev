import tkinter as tk
from tkinter import filedialog, ttk
import os
import openpyxl
from datetime import datetime
import subprocess
import sys

class ExcelPrinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Excel Printer App")
        self.root.geometry("400x350")
        self.root.configure(bg="#E6F3FF")  # Light blue background

        self.file_path = tk.StringVar()
        self.value1 = tk.StringVar()
        self.value2 = tk.StringVar()
        self.file_path.set("[None selected]")

        self.create_widgets()

    def create_widgets(self):
        # Style configuration
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TButton', background='#4A90E2', foreground='white', font=('Arial', 10))
        style.map('TButton', background=[('active', '#3A7BCE')])
        style.configure('TLabel', background='#E6F3FF', font=('Arial', 10))
        style.configure('TFrame', background='#E6F3FF')

        main_frame = ttk.Frame(self.root, padding="20 20 20 0")
        main_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(main_frame, text="Current selected file path:").pack(pady=(0, 5))
        ttk.Label(main_frame, textvariable=self.file_path, wraplength=350).pack()

        ttk.Button(main_frame, text="Select File", command=self.select_file).pack(pady=15)

        values_frame = ttk.Frame(main_frame)
        values_frame.pack(fill=tk.X, pady=10)

        ttk.Label(values_frame, text="Value 1:").grid(row=0, column=0, sticky='e', padx=(0, 10))
        ttk.Label(values_frame, textvariable=self.value1).grid(row=0, column=1, sticky='w')

        ttk.Label(values_frame, text="Value 2:").grid(row=1, column=0, sticky='e', padx=(0, 10))
        ttk.Label(values_frame, textvariable=self.value2).grid(row=1, column=1, sticky='w')

        ttk.Button(main_frame, text="Sign & Print", command=self.sign_and_print).pack(pady=15)

        ttk.Label(main_frame, text="By submitting you certify that these values are correct",
                  font=('Arial', 8, 'italic')).pack()

        ttk.Label(self.root, text="Developed by Kenneth Kim - kim.k.22@pg.com",
                  font=('Arial', 8), anchor='e').pack(side="bottom", fill="x", pady=10)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        if file_path:
            self.file_path.set(file_path)
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.active
            self.value1.set(sheet["A2"].value)
            self.value2.set(sheet["B2"].value)

    def sign_and_print(self):
        file_path = self.file_path.get()
        if file_path:
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.active
            sheet["C2"].value = os.getlogin()
            sheet["D2"].value = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            workbook.save(file_path)
            if sys.platform.startswith('win'):
                subprocess.run(['print', file_path], shell=True)
            elif sys.platform.startswith('linux'):
                subprocess.run(['lp', file_path], shell=True)
            elif sys.platform.startswith('darwin'):
                subprocess.run(['lpr', file_path], shell=True)

root = tk.Tk()
app = ExcelPrinterApp(root)
root.mainloop()