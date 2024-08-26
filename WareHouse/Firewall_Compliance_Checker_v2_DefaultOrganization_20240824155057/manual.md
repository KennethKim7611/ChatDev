# Firewall Compliance Checker User Manual

## Introduction
The Firewall Compliance Checker is a program designed to check the compliance of firewall rules against a company's policy. It leverages the OpenAI API to perform the compliance check and generates a detailed report for non-compliant rules.

## Main Functions
The Firewall Compliance Checker provides the following main functions:

1. Select Policy Folder: Allows the user to select the folder that contains the documents of firewall policies. These documents act as the knowledge base for the compliance check.

2. Select Rules File: Allows the user to select the source Excel (.xlsx) file that contains the current firewall rules of the company.

3. Check Compliance: Performs the compliance check using the selected policy folder and rules file. It calls the OpenAI API to check the rules' compliance against the company policy. If there are non-compliant rules, it generates an Excel report explaining each non-compliant rule and providing evidence from the policies.

## Installation
To use the Firewall Compliance Checker, follow these steps:

1. Install Python: Make sure you have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/

2. Install Dependencies: Open a terminal or command prompt and navigate to the project directory. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Obtain OpenAI API Key: Sign up for an OpenAI account and obtain an API key. Replace `'YOUR_API_KEY'` in the `main.py` file with your actual API key.

## Usage
To use the Firewall Compliance Checker, follow these steps:

1. Run the Program: Open a terminal or command prompt and navigate to the project directory. Run the following command to start the program:

   ```
   python main.py
   ```

2. Select Policy Folder: Click on the "Select Policy Folder" button and choose the folder that contains the firewall policy documents.

3. Select Rules File: Click on the "Select Rules File" button and choose the Excel file that contains the current firewall rules of the company.

4. Check Compliance: Click on the "Check Compliance" button to perform the compliance check. If there are non-compliant rules, a compliance report will be generated and saved as `compliance_report.xlsx` in the project directory.

## Example
Here is an example scenario to demonstrate the usage of the Firewall Compliance Checker:

1. Run the Program: Open a terminal or command prompt and navigate to the project directory. Run the following command to start the program:

   ```
   python main.py
   ```

2. Select Policy Folder: Click on the "Select Policy Folder" button and choose the folder that contains the firewall policy documents.

3. Select Rules File: Click on the "Select Rules File" button and choose the Excel file that contains the current firewall rules of the company.

4. Check Compliance: Click on the "Check Compliance" button to perform the compliance check. If there are non-compliant rules, a compliance report will be generated and saved as `compliance_report.xlsx` in the project directory.

5. Review the Compliance Report: Open the `compliance_report.xlsx` file to view the detailed report of non-compliant firewall rules. Each non-compliant rule will be listed along with the reason for non-compliance and evidence from the policy documents.

## Conclusion
The Firewall Compliance Checker is a powerful tool for checking the compliance of firewall rules against a company's policy. It provides an easy-to-use interface for selecting the policy folder and rules file, and generates a detailed report for non-compliant rules. By leveraging the OpenAI API, it ensures accurate and efficient compliance checking.