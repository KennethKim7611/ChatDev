import tkinter as tk
from tkinter import filedialog, messagebox
import datetime
import openpyxl
import os

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Excel Editor")
        self.geometry("400x200")
        self.file_path = None
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Select an Excel file:")
        self.label.pack(pady=10)
        self.select_button = tk.Button(self, text="Select File", command=self.select_file)
        self.select_button.pack(pady=5)
        self.file_name_label = tk.Label(self, text="")
        self.file_name_label.pack(pady=5)
        self.submit_button = tk.Button(self, text="Submit", command=self.submit)
        self.submit_button.pack(pady=10)

    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        if self.file_path:
            file_name = self.file_path.split('/')[-1]
            self.file_name_label.config(text=f"Selected file: {file_name}")

    def submit(self):
        if self.file_path is None:
            messagebox.showerror("Error", "Please select an Excel file.")
            return
        name = os.getlogin()  # Get the logged-in username
        try:
            workbook = openpyxl.load_workbook(self.file_path)
            sheet = workbook.active
            sheet["C1"] = "Date"
            sheet["C2"] = datetime.datetime.now()
            sheet["D1"] = "Signature"
            sheet["D2"] = name
            workbook.save(self.file_path)
            messagebox.showinfo("Success", "Excel file has been edited and saved.")
            self.open_file()
            self.after(1000, self.destroy)  # Close the application after 1 second
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def open_file(self):
        try:
            os.startfile(self.file_path)
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = Application()
    app.mainloop()
