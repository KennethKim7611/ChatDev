import tkinter as tk
from tkinter import filedialog
import openai_api
import compliance_report
class FirewallComplianceChecker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Firewall Compliance Checker")
        self.root.geometry("400x200")
        self.policy_folder_path = ""
        self.rules_file_path = ""
        self.select_policy_folder_button = tk.Button(self.root, text="Select Policy Folder", command=self.select_policy_folder)
        self.select_policy_folder_button.pack(pady=10)
        self.select_rules_file_button = tk.Button(self.root, text="Select Rules File", command=self.select_rules_file)
        self.select_rules_file_button.pack(pady=10)
        self.check_compliance_button = tk.Button(self.root, text="Check Compliance", command=self.check_compliance)
        self.check_compliance_button.pack(pady=10)
        self.root.mainloop()
    def select_policy_folder(self):
        self.policy_folder_path = filedialog.askdirectory()
    def select_rules_file(self):
        self.rules_file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    def check_compliance(self):
        if self.policy_folder_path == "":
            print("Please select the policy folder.")
            return
        if self.rules_file_path == "":
            print("Please select the rules file.")
            return
        # Call the OpenAI API to check compliance
        openai_api_instance = openai_api.OpenAIAPI('YOUR_API_KEY')
        non_compliant_rules = openai_api_instance.check_compliance(self.policy_folder_path, self.rules_file_path)
        if non_compliant_rules:
            # Generate compliance report
            report = compliance_report.ComplianceReport(non_compliant_rules)
            report.generate_report("compliance_report.xlsx")
        else:
            print("All firewall rules are compliant.")
if __name__ == "__main__":
    app = FirewallComplianceChecker()