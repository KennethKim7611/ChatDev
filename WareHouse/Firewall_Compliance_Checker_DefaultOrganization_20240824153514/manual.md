# Firewall Policy Compliance Checker User Manual

## Introduction

The Firewall Policy Compliance Checker is a program designed to check the compliance of firewall rules with a given firewall policy. It takes as input a document containing the firewall policy and an Excel sheet containing the current firewall rules of a company. The program then compares the rules in the Excel sheet with the rules in the policy and flags any non-compliant rules, providing detailed reasoning for each non-compliance.

This user manual provides instructions on how to install the necessary dependencies and how to use the program to check firewall policy compliance.

## Installation

To use the Firewall Policy Compliance Checker, you need to install the following dependencies:

- Python (version 3.6 or higher)
- pandas (version 1.1.4 or higher)
- numpy (version 1.19.2 or higher)

You can install these dependencies by running the following command:

```
pip install -r requirements.txt
```

## Usage

To use the Firewall Policy Compliance Checker, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the directory where the program files are located.

3. Run the following command to start the program:

   ```
   python main.py
   ```

4. The program will open a file dialog to prompt you to select the firewall policy document. Click "Browse" and select the document file.

5. The program will then prompt you to select the firewall rules Excel sheet. Click "Browse" and select the Excel sheet file.

6. The program will load the firewall policy rules and the current firewall rules from the selected files.

7. The program will compare the rules and flag any non-compliant rules with detailed reasoning.

8. The program will display the compliance check results in the console.

9. Review the results to identify any non-compliant rules and the corresponding reasoning.

10. Close the program when you are done reviewing the results.

## Troubleshooting

If you encounter any issues while using the Firewall Policy Compliance Checker, please try the following troubleshooting steps:

- Make sure you have installed the required dependencies as mentioned in the installation section.

- Ensure that the firewall policy document and the firewall rules Excel sheet are in the correct format and contain the necessary information.

- Check for any error messages displayed in the console and refer to the error message for troubleshooting guidance.

- If the issue persists, please contact our support team for further assistance.

## Conclusion

The Firewall Policy Compliance Checker is a useful tool for checking the compliance of firewall rules with a given firewall policy. By following the instructions in this user manual, you can easily install and use the program to identify non-compliant rules and understand the reasoning behind them.