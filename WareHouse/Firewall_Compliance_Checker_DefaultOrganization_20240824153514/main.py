'''
This is the main file of the firewall policy compliance checker application.
It imports the necessary modules and contains the main function to run the application.
'''
import tkinter as tk
from tkinter import filedialog
from firewall_checker import FirewallChecker
def main():
    # Create the main application window
    root = tk.Tk()
    root.withdraw()
    # Prompt the user to select the firewall policy document
    policy_file_path = filedialog.askopenfilename(title="Select Firewall Policy Document")
    if not policy_file_path:  # Check if the user canceled the file selection
        print("File selection canceled. Exiting...")
        return
    # Prompt the user to select the firewall rules Excel sheet
    rules_file_path = filedialog.askopenfilename(title="Select Firewall Rules Excel Sheet")
    if not rules_file_path:  # Check if the user canceled the file selection
        print("File selection canceled. Exiting...")
        return
    # Create an instance of the FirewallChecker class
    checker = FirewallChecker(policy_file_path, rules_file_path)
    # Run the compliance check and display the results
    checker.check_compliance()
    checker.display_results()
if __name__ == "__main__":
    main()