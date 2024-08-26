import openpyxl
class ComplianceReport:
    def __init__(self, non_compliant_rules):
        self.non_compliant_rules = non_compliant_rules
    def generate_report(self, output_file_path):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet["A1"] = "Rule"
        sheet["B1"] = "Reason"
        row = 2
        for rule, reason in self.non_compliant_rules.items():
            sheet[f"A{row}"] = rule
            sheet[f"B{row}"] = reason
            row += 1
        workbook.save(output_file_path)