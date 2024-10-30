import vul, emailme
from seleniumbase import BaseCase

class MaltaAutomation(BaseCase):
    def digital_malt(self, params):
        # Setup email account
        clean_firstname = params['firstname'].replace(' ', '').replace('-', '').lower()
        clean_lastname = params['firstname'].replace(' ', '').replace('-', '').lower()
        username = clean_firstname + clean_lastname + str(vul.random.randint(100,1000))
        email_name = username + '@workgh.com'
        emailme.create_email(email_name)
        # Use your method here to create an email
        EMAIL_ACCOUNT = email_name
        PASSWORD = "GreatNews@2024"

        # Step 1: Open the browser in fullscreen mode
        self.open("https://portal.residencymalta.gov.mt/register")
        self.maximize_window()
        self.sleep(2)

        # Fill in the email field and click "Send verification code"
        self.type("#mat-input-0", clean_firstname)
        self.type("#mat-input-1", clean_lastname)
        self.type("#mat-input-2", EMAIL_ACCOUNT)
        self.type("#mat-input-3", username)
        self.type("#Password", PASSWORD)
        self.type("#ComfirmPassword", PASSWORD)

        self.wait_for_element_visible('button.mat-primary:contains("SIGN UP")', timeout=30)
        
        # Wait for the button to no longer be disabled
        self.wait_for_element_not_present('button.mat-primary[disabled]', timeout=30)
        
        # Click the button
        self.click('button.mat-primary:contains("SIGN UP")')

        self.sleep(10)

        self.open(f'https://portal.residencymalta.gov.mt/ActivateUser/{username}')

        self.open('https://portal.residencymalta.gov.mt/login')

        self.sleep(5)

        self.type("#mat-input-0", username)
        self.type("#Password", PASSWORD)
        
        self.sleep(5)
        # Wait until the button is enabled and then click it
        self.wait_for_element_visible('//button[.//span[text()="CONTINUE"] and not(@disabled)]', timeout=30)
        self.click('//button[.//span[text()="CONTINUE"] and not(@disabled)]')

        self.sleep(5)

        self.open('https://portal.residencymalta.gov.mt/application-forms')
