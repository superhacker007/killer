import requests
from bs4 import BeautifulSoup
from seleniumbase import BaseCase

class FormAutomationApp:
    def __init__(self, url):
        self.url = url
        self.soup = None

    def fetch_site_structure(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.text, 'html.parser')
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

    def analyze_forms(self):
        forms = self.soup.find_all('form')
        form_details = []

        for form in forms:
            inputs = form.find_all(['input', 'textarea', 'select', 'button'])
            form_data = {
                'action': form.get('action'),
                'method': form.get('method', 'get'),
                'inputs': []
            }

            for input_element in inputs:
                input_type = input_element.get('type', 'text')
                input_name = input_element.get('name')
                input_id = input_element.get('id')
                input_placeholder = input_element.get('placeholder')

                form_data['inputs'].append({
                    'type': input_type,
                    'name': input_name,
                    'id': input_id,
                    'placeholder': input_placeholder
                })

            form_details.append(form_data)

        return form_details

    def generate_seleniumbase_code(self, forms):
        generated_code = """
import time
from seleniumbase import BaseCase

class FormBot(BaseCase):
    def test_fill_forms(self):
        self.open("{url}")
        self.maximize_window()
        self.sleep(2)
        """

        generated_code = generated_code.format(url=self.url)

        for form in forms:
            if form['method'].lower() == 'post':
                submit_action = 'self.submit()'
            else:
                submit_action = 'self.click(\'button[type="submit"]\')'

            for input_field in form['inputs']:
                if input_field['type'] in ['text', 'password', 'email', 'tel']:
                    generated_code += f"""
        self.type("#{input_field['id']}", "test_{input_field['name']}")
                    """
                elif input_field['type'] == 'radio':
                    generated_code += f"""
        self.click("#{input_field['id']}")
                    """
                elif input_field['type'] == 'checkbox':
                    generated_code += f"""
        self.click("#{input_field['id']}")
                    """
                elif input_field['type'] == 'submit':
                    generated_code += f"""
        {submit_action}
                    """
                # Add more input types as needed

        generated_code += """
        self.sleep(5)  # Keep the browser open to see the result
        """

        return generated_code

    def run(self):
        self.fetch_site_structure()
        forms = self.analyze_forms()
        selenium_code = self.generate_seleniumbase_code(forms)
        print(selenium_code)

if __name__ == "__main__":
    url = "https://ircc.canada.ca/visit-visiter/en/get-account-ircc-portal"
    app = FormAutomationApp(url)
    app.run()
