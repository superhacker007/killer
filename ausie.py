import imaplib, email, re, time, vul, emailme
from email.header import decode_header
from bs4 import BeautifulSoup
from seleniumbase import BaseCase

class IRCCAutomation(BaseCase):
    def get_verification_code(self, email_account, password):
        # Connect to the server
        mail = imaplib.IMAP4_SSL("mail.workgh.com")
        mail.login(email_account, password)
        mail.select("INBOX")

        # Search for the latest email containing the verification code
        status, messages = mail.search(None, 'ALL')
        messages = messages[0].split(b' ')
        latest_email_id = messages[-1]

        # Fetch the email by ID
        status, msg_data = mail.fetch(latest_email_id, '(RFC822)')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else 'utf-8')
                print("Subject:", subject)

                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        try:
                            body = part.get_payload(decode=True).decode()
                        except Exception as e:
                            print(f"Could not decode part: {e}")
                            body = None
                        
                        if body and (content_type == "text/plain" or content_type == "text/html"):
                            # Look for the pattern "Verification code: ######" in the email body
                            code_match = re.search(r'Verification code: (\d{6})', body)
                            if code_match:
                                return code_match.group(1)
                else:
                    # If the message isn't multipart, check the payload directly
                    try:
                        body = msg.get_payload(decode=True).decode()
                    except Exception as e:
                        print(f"Could not decode payload: {e}")
                        body = None
                    
                    if body:
                        code_match = re.search(r'Verification code: (\d{6})', body)
                        if code_match:
                            return code_match.group(1)

        return None


    def test_ircc_automation(self):
        # Setup email account
        clean_firstname = vul.random_male_friend_firstname().replace(' ', '').replace('-', '').lower()
        clean_lastname = vul.generate_random_name().replace(' ', '').replace('-', '').lower()
        email_name = clean_firstname + clean_lastname + str(vul.random.randint(100,1000)) + '@workgh.com'
        emailme.create_email(email_name)
        # Use your method here to create an email
        EMAIL_ACCOUNT = email_name
        PASSWORD = "GreatNews@2024"

        # Step 1: Open the browser in fullscreen mode
        self.open("https://online.immi.gov.au/lusc/register")
        self.maximize_window()
        self.sleep(2)

        # Fill in the email field and click "Send verification code"
        self.type("#email", EMAIL_ACCOUNT)
        self.wait_for_element_visible('button[name="continue"]')
        self.click('button[name="continue"]')
        self.sleep(2)

        # Wait for the email verification code
        print("Waiting for email verification code...")
        self.sleep(30)
        verification_code = self.get_verification_code(EMAIL_ACCOUNT, PASSWORD)

        if verification_code:
            print("Verification code received:", verification_code)
            self.type("#_1a4a0a1b", verification_code)  # Assuming this is the input for the code
            self.sleep(2)
            self.wait_for_element_visible('button[name="continue"]')
            self.click('button[name="continue"]')
            self.sleep(2)
        else:
            print("Verification code not found in the email.")
        
        self.click("#_1a4a0a2b0")  # This targets the radio button
        
        # Fill in checkbox
        self.click("#_1a4a0a2d0_7")  # This targets the checkbox

        # Fill in text fields
        self.type("#_1a4a0a2f1", clean_firstname)  # This targets the first text field with placeholder "required"
        self.type("#_1a4a0a2f2", clean_lastname)  # This targets the second text field

        # Fill in telephone fields
        self.type("#_1a4a0a2f3", "1234567890")  # This targets the first telephone field with placeholder "required"
        self.type("#_1a4a0a2f4", "0987654321")  # This targets the second telephone field

        self.wait_for_element_visible('button[name="continue"]')
        self.click('button[name="continue"]')
        self.sleep(2)

        # Fill in email field
        self.type("#_1a4a0a3a", EMAIL_ACCOUNT)  # This targets the email field

        # Fill in password fields
        self.type("#_1a4a0a3b", PASSWORD)  # This targets the first password field
        self.type("#_1a4a0a3c", PASSWORD)  # This targets the second password field

        # Select options from dropdowns
        self.select_option_by_value("#_1a4a0a3d0-r0-_0b", "1")  # This selects "What is the name of your favourite teacher?" from the first dropdown
        self.type("#_1a4a0a3d0-r0-_0c", "Smith")  # This fills in the answer to the first security question
        
        self.select_option_by_value("#_1a4a0a3d0-r1-_0b", "9")  # This selects "Name your favourite holiday destination." from the second dropdown
        self.type("#_1a4a0a3d0-r1-_0c", "Hawaii")  # This fills in the answer to the second security question
        
        self.select_option_by_value("#_1a4a0a3d0-r2-_0b", "11")  # This selects "What is your favourite movie?" from the third dropdown
        self.type("#_1a4a0a3d0-r2-_0c", "Inception")  # This fills in the answer to the third security question

        # Check a checkbox
        self.click("#_1a4a0a3f")  # This targets the final checkbox

        checkbox_container_xpath = '//div[contains(@aria-labelledby, "-label") and contains(@role, "checkbox")]'
        
        # Scroll to the element to ensure it's in view
        self.scroll_to(checkbox_container_xpath)
        
        # Click the container div (which simulates clicking the hidden checkbox)
        self.click(checkbox_container_xpath)

        self.sleep(2)

        self.click('button[name="submit"]')

        self.sleep(5)

        self.click('button[name="continue"]')

        self.sleep(2)
        self.click('#btn_newapp')

        # Target and click the span containing "Visitor"
        self.sleep(5)
        self.click('//span[contains(text(), "Visitor")]')


        self.sleep(2)

        self.click('//span[contains(text(), "Visitor Visa (600)")]')


        self.sleep(2)

        self.click('#_2a0d0a0a0e0a0a0a5a1a_input')


        self.click('button[name="_2a0be0a0a0g1"]')
        
        

        self.sleep(2)

        # 2. Target and click a radio button using 'name' and 'value' attributes
        self.click('input[name="_2a0b0a0a0e0a0a1a4c1b0"][value="2"]')  # Selects the radio button with value "2"

        # 3. Target and click another radio button using 'name' and 'value' attributes
        self.click('input[name="_2a0b0a0a0e0a0a1a3i1b0"][value="29"]')  # Selects the radio button with value "29"

        # 4. Target and click another radio button using 'name' and 'value' attributes
        self.click('input[name="_2a0b0a0a0e0a0a1a7d1b0"][value="2"]')  # Selects the radio button with value "2"

        # 5. Target and select an option from a dropdown (example: select Afghanistan)
        self.select_option_by_value('#_2a0b0a0a0e0a0a1a2e3a1a_input', 'AFGH')

        # 6. Target and input text into a textarea
        self.type('#_2a0b0a0a0e0a0a1a3bc1b0_input', 'This is the default content.')

        # 7. Select an option from another dropdown (example: select Business)
        self.select_option_by_value('#_2a0b0a0a0e0a0a1a3bb0b0ad971625694e373-1', '2')

        # 8. Click on a button (example: Next button)
        self.click('span.wc_btn_img.wc_btn_imge:contains("Next")')

        self.sleep(5) 

        self.sleep(5) 


        self.sleep(20000) 
        
        self.sleep(3)  # Sleep for observation

        # To keep the browser open for observation

        self.type("#user-control", EMAIL_ACCOUNT)
        self.type("#password-control", PASSWORD)
        self.type("#reenterPassword_input", PASSWORD)
        self.type("#lastName_input", "Doe")
        self.type("#firstName_input", "John")
        self.scroll_to("#telLocation_radio-button-02-input")
        self.click("#telLocation_radio-button-02-input")
        self.type("#telephoneCountryCode_input", "233")
        self.type("#phone-num-control", "1234567890")

        # Wait for the button to be enabled
        self.wait_for_element_visible("#Login.SignUp_action_button0", timeout=20)
        self.wait_for_element_not_present('[id="Login.SignUp_action_button0"][disabled]', timeout=20)
        self.save_screenshot("before_click.png")  # Save screenshot for debugging
        self.click("#Login.SignUp_action_button0")

        # Continue with the rest of the flow...

        self.sleep(3000)  # To keep the browser open for observation

# To run the test with pytest
if __name__ == "__main__":
    from pytest import main
    main(["-v", __file__])
