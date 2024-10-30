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
                        body = part.get_payload(decode=True).decode()
                        if content_type == "text/plain" or content_type == "text/html":
                            code_match = re.search(r'Enter this code \[(\d{6})\]', body)
                            if code_match:
                                return code_match.group(1)
        return None

    def test_ircc_automation(self):
        clean_firstname = vul.random_male_friend_firstname().replace(' ', '').replace('-', '').lower()
        clean_lastname = vul.generate_random_name().replace(' ', '').replace('-', '').lower()
        email_name = clean_firstname + clean_lastname + '@workgh.com'
        emailme.create_email(clean_firstname + clean_lastname)

        EMAIL_ACCOUNT = email_name
        PASSWORD = "GreatNews@2024"

        # Step 1: Open the browser in fullscreen mode
        self.open("https://ircc.canada.ca/visit-visiter/en/get-account-ircc-portal")
        self.maximize_window()  # Maximize the browser window
        self.sleep(2)

        # Fill in the email fields and get the invitation code
        self.type("#email", EMAIL_ACCOUNT)
        self.type("#email_confirm", EMAIL_ACCOUNT)
        self.click("#send-email-button")
        self.sleep(2)
        invite_code = self.get_text("p.inv-code strong")
        print("Invitation code received:", invite_code)

        # Step 2: Navigate to the sign-up page where the invitation code is used
        self.open("https://portal-portail.apps.cic.gc.ca/signup?lang=en")
        self.sleep(2)

        # Fill in the sign-up form
        self.type("#invite-code-control", invite_code)
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
# Wait for the button to be clickable and then click it
        self.wait_for_element_visible("#Login.SignUp_action_button0", timeout=20)
        self.wait_for_element_not_present('[id="Login.SignUp_action_button0"][disabled]', timeout=20)
        self.save_screenshot("before_click.png")  # Save screenshot for debugging
        self.click("#Login.SignUp_action_button0")


        # Wait for the email verification code
        print("Waiting for email verification code...")
        self.sleep(30)
        verification_code = self.get_verification_code(EMAIL_ACCOUNT, PASSWORD)

        if verification_code:
            print("Verification code received:", verification_code)
            self.type("#verification-code-control", verification_code)
            self.click("#Confirm.Title_action_button0")
        else:
            print("Verification code not found in the email.")

        # Log in to the portal
        self.open("https://portal-portail.apps.cic.gc.ca/signin?lang=en")
        self.type("#user-control", EMAIL_ACCOUNT)
        self.type("#password-control", PASSWORD)
        self.click("#Login.SignInTitle_action_button0")

        # Agree to terms
        self.click("#btnIAgree")
        self.sleep(2)

        # Apply for a visa
        self.click("#lobLink_0_0")
        self.sleep(2)
        self.click("input#ackApplyingForTR_chk-input")
        self.click("button span span:contains('Start application')")

        # Fill out application details
        self.click("label[for='hasGroup_radio-button-02-input']")
        self.click("#next_path")
        self.sleep(2)
        self.click("label[for='applyingFor_radio-button-464-input']")
        self.click("label[for='visaPurpose_radio-button-470-input']")
        self.type("#visitDetails_txtArea", "I am visiting my friend in Canada")

        # Select dates
        self.select_option_by_text("#dateComingToCanadaYear_sltDateYear", "2024")
        self.select_option_by_text("#dateComingToCanadaMonth_sltDateMonth", "November")
        self.select_option_by_text("#dateComingToCanadaDay_sltDateDay", "17")
        self.select_option_by_text("#dateComingToCanadaToYear_sltDateYear", "2024")
        self.select_option_by_text("#dateComingToCanadaToMonth_sltDateMonth", "November")
        self.select_option_by_text("#dateComingToCanadaToDay_sltDateDay", "24")

        # Continue application process
        self.click("#next_path")
        self.sleep(2)
        self.click("label[for='hasRepresentative_radio-button-02-input']")
        self.click("#next_path")
        self.sleep(2)
        self.type("#lastName_input", "Doe")
        self.type("#firstName_input", "John")
        self.select_option_by_text("#year_sltDateYear", "1990")
        self.select_option_by_text("#month_sltDateMonth", "August")
        self.select_option_by_text("#day_sltDateDay", "27")
        self.click("label[for='gender_radio-button-02-input']")
        self.click("#next_path")
        self.click("label[for='travelDocument_radio-button-249-input']")
        self.click("label[for='passportType_radio-button-099-input']")
        self.select_option_by_text("#codePassport_select", "GHA (Ghana)")
        self.select_option_by_text("#nationalityPassport_select", "Ghana")
        self.type("#travelDocNum_input", "G34676546")
        self.type("#travelDocNumConfirmation_input", "G34676546")

        # Set passport issue and expiry dates
        self.select_option_by_text("#dateIssuePassportDay_sltDateDay", "27")
        self.select_option_by_text("#dateIssuePassportMonth_sltDateMonth", "August")
        self.select_option_by_text("#dateIssuePassportYear_sltDateYear", "2023")
        self.select_option_by_text("#dateExpiryPassportDay_sltDateDay", "26")
        self.select_option_by_text("#dateExpiryPassportMonth_sltDateMonth", "August")
        self.select_option_by_text("#dateExpiryPassportYear_sltDateYear", "2033")

        # Continue application
        self.click("label[for='hasGreenCard_radio-button-02-input']")
        self.click("label[for='travelledToCanadaInPastTen_radio-button-02-input']")
        self.click("label[for='holdUSVisa_radio-button-02-input']")
        self.click("label[for='travellingByAir_radio-button-01-input']")
        self.click("#next_path")

        # Birth and citizenship information
        self.select_option_by_text("#countryBirth_select", "Ghana")
        self.type("#cityBirth_input", "Accra")
        self.click("label[for='citizenshipOfCountryOrTerritory_radio-button-02-input']")
        self.select_option_by_text("#countryOfCitizenship_select", "Ghana")
        self.click("input#citizenFromBirth_chk-input")
        self.click("#next_path")

        self.sleep(3000)  # To keep the browser open for observation

# To run the test with pytest
if __name__ == "__main__":
    from pytest import main
    main(["-v", __file__])
