import openai
class OpenAIAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key
    def check_compliance(self, policy_folder_path, rules_file_path):
        # Implement the logic to check compliance using the OpenAI API
        # You can use the policy_folder_path and rules_file_path to read the necessary files
        # Example code to print the paths
        print("Policy Folder Path:", policy_folder_path)
        print("Rules File Path:", rules_file_path)
        # Placeholder code to simulate non-compliant rules
        non_compliant_rules = {
            "Rule 1": "Reason 1",
            "Rule 2": "Reason 2",
            "Rule 3": "Reason 3"
        }
        return non_compliant_rules