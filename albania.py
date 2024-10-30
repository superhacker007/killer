"""A complete end-to-end test for an e-commerce website."""
from seleniumbase import BaseCase
import random, os

class MyTestClass(BaseCase):
    def test_click_at_coordinates_beyond_viewport(self):
        self.open("https://e-visa.al/register")  # Replace with the actual URL of your test page

        # Fill in the form as per the original test
        randmail = random.randint(1, 10000)
        self.maximize_window()
        self.type("#first-name", "John")
        self.type("#last-name", "Tetteh")

        # Activate dropdown and select 'Ghana'
        self.click('div#vs1__combobox')
        self.type('input.vs__search', 'Ghana')
        self.sleep(1)  # Wait for dropdown options to load
        self.click('li[id^="vs1__option"]:contains("Ghana")')
        self.assert_text("Ghana", 'div#vs1__combobox .vs__selected-options span.vs__selected')

        # Fill in the rest of the form
        self.type("#email", f"tickets{randmail}@gmail.com")
        self.type("#password", "GreatNews@2024")
        self.type("#password-confirmation", "GreatNews@2024")
        self.click('#allow-submit')
        self.click('button.button-secondary')
        self.sleep(3)

        # Log in
        self.type("#email-address", f"tickets{randmail}@gmail.com")
        self.type("#password", "GreatNews@2024")
        self.click('button[type="submit"].bg-secondary-500')

        # Navigate to the apply page
        self.open("https://e-visa.al/apply")
        
        self.sleep(5)

        section_xpath = "//section[header/h2[contains(text(), 'Visa Type “C”')]]"

        # Hover over the identified section to reveal the "Select" option
        self.hover(section_xpath)

        # Optional: Wait briefly to ensure hover effects are applied
        self.sleep(1)

        # Click on the section itself or a specific child if necessary
        self.click(section_xpath)  # Clicks directly on the section

        # Alternatively, if you need to click the "Select" span specifically
        # self.click(f"{section_xpath}//span[contains(text(), 'Select')]")  # Refined XPath for "Select"

        # Verify the click action by checking for any expected behavior change
        # Example: Verifying if "Selected" appears
        # self.assert_text("Selected", f"{section_xpath}//span[contains(text(), 'Selected')]")

        

        header_xpath = "//header[span[contains(text(), 'Visa for tourism (C)')]]"

        self.hover(header_xpath)

        self.sleep(1)

        self.click(header_xpath)  # Clicks directly on the header

        self.click("button.mt-4.block.button.button-secondary.w-full.md\\:w-auto.md\\:mx-auto.lg\\:mx-0.p-8.md\\:px-24.py-2")

        self.type("#email-address", f"tickets{randmail}@gmail.com")
        self.type("#password", "GreatNews@2024")
        self.click('button[type="submit"].bg-secondary-500')

        self.sleep(3)

         # Click on the input field using its class or aria attributes
        self.click('input[aria-labelledby="vs1__combobox"]')  # Click the search input field

        # Type "Ghana" into the input field to trigger the dropdown
        self.type('input[aria-labelledby="vs1__combobox"]', 'Ghana')
        self.sleep(1)  # Wait briefly for the dropdown options to appear

        # Use XPath to select "Ghana" from the dropdown list
        self.click("//ul[@id='vs1__listbox']//li[contains(text(), 'Ghana')]")

        # Optional: Verify if "Ghana" was selected correctly
        self.assert_text("Ghana", 'div#vs1__combobox .vs__selected-options span.vs__selected')

         # Pause to observe the selection action

        self.click('input[aria-labelledby="vs2__combobox"]')  # Click the second search input field

        # Type "Cairo" into the input field to trigger the dropdown
        self.type('input[aria-labelledby="vs2__combobox"]', 'Cairo')
        self.sleep(1)  # Wait briefly for the dropdown options to appear

        # Use XPath to select "Cairo" from the dropdown list
        self.click("//ul[@id='vs2__listbox']//li[contains(text(), 'Cairo')]")

        # Optional: Verify if "Cairo" was selected correctly
        self.assert_text("Cairo", 'div#vs2__combobox .vs__selected-options span.vs__selected')

         # Pause to observe the selection action

        self.type("//label[contains(text(), '1.3 Family name(s) *')]/following-sibling::input", 'Doe')

        self.type("//label[contains(text(), '1.5 First names(given names) *')]/following-sibling::input", 'John')


        self.click('input[type="text"].block.w-full.px-3.py-2.text-black')

        self.wait_for_element_visible("input[type='text'].block.w-full.px-3.py-2.text-black")
        self.click("input[type='text'].block.w-full.px-3.py-2.text-black")

        # Click the arrow to navigate back through the years until 1991 is visible
        while not self.is_element_visible("//button[@aria-label='1991']"):
            # Click the back arrow button
            self.click('button[aria-label="Prev Year"]')

        # Click on the year 1991 once it is visible
        self.wait_for_element_visible("//button[@aria-label='1991']")
        self.click("//button[@aria-label='1991']")

        self.wait_for_element_visible("//button[@aria-label='August, 1991']")
        self.click("//button[@aria-label='August, 1991']")

        self.wait_for_element_visible("//button[@aria-label='27 August 1991']")
        self.click("//button[@aria-label='27 August 1991']")

        # Click on the input field using its class or aria attributes
        self.click('input[aria-labelledby="vs3__combobox"]')  # Click the search input field

        # Type "Ghana" into the input field to trigger the dropdown
        self.type('input[aria-labelledby="vs3__combobox"]', 'Ghana')
        self.sleep(1)  # Wait briefly for the dropdown options to appear

        # Use XPath to select "Ghana" from the dropdown list
        self.click("//ul[@id='vs3__listbox']//li[contains(text(), 'Ghana')]")

         # Pause to observe the selection action


        # Click on the input field using its class or aria attributes
        self.click('input[aria-labelledby="vs4__combobox"]')  # Click the search input field

        # Type "Ghana" into the input field to trigger the dropdown
        self.type('input[aria-labelledby="vs4__combobox"]', 'Ghana')
        self.sleep(1)  # Wait briefly for the dropdown options to appear

        # Use XPath to select "Ghana" from the dropdown list
        self.click("//ul[@id='vs4__listbox']//li[contains(text(), 'Ghana')]")

         # Pause to observe the selection action

        # Click on the input field using its class or aria attributes
        self.click('input[aria-labelledby="vs5__combobox"]')  # Click the search input field

        # Type "Ghana" into the input field to trigger the dropdown
        self.type('input[aria-labelledby="vs5__combobox"]', 'Male')
        self.sleep(1)  # Wait briefly for the dropdown options to appear

        # Use XPath to select "Ghana" from the dropdown list
        self.click("//ul[@id='vs5__listbox']//li[contains(text(), 'Male')]")

         # Pause to observe the selection action

        # Click on the input field using its class or aria attributes
        self.click('input[aria-labelledby="vs6__combobox"]')  # Click the search input field

        # Type "Ghana" into the input field to trigger the dropdown
        self.type('input[aria-labelledby="vs6__combobox"]', 'Single')
        self.sleep(1)  # Wait briefly for the dropdown options to appear

        # Use XPath to select "Ghana" from the dropdown list
        self.click("//ul[@id='vs6__listbox']//li[contains(text(), 'Single')]")

         # Pause to observe the selection action

        # Click on the input field using its class or aria attributes
        self.click('input[aria-labelledby="vs7__combobox"]')  # Click the search input field

        # Type "Ghana" into the input field to trigger the dropdown
        self.type('input[aria-labelledby="vs7__combobox"]', 'No')
        self.sleep(1)  # Wait briefly for the dropdown options to appear

        # Use XPath to select "Ghana" from the dropdown list
        self.click("//ul[@id='vs7__listbox']//li[contains(text(), 'No')]")

         # Pause to observe the selection action

        self.type("//label[contains(text(), '1.7 Personal ID Number(Passport number if empty) *')]/following-sibling::input", 'G2343234')

        self.type("//label[contains(text(), '1.8 Place and country of birth *')]/following-sibling::input", 'Accra')

        self.type("//label[contains(text(), '1.13 Father`s name *')]/following-sibling::input", 'Fathername')

        self.type("//label[contains(text(), '1.14 Mother`s name')]/following-sibling::input", 'Mothername')

        self.click('button.m-6.md\\:m-0.md\\:ml-auto.py-2.px-8.w-full.md\\:w-auto.button.button-secondary')

        self.sleep(2)

        self.click('input[aria-labelledby="vs8__combobox"]')  # Click the search input field

        # Type "Ghana" into the input field to trigger the dropdown
        self.type('input[aria-labelledby="vs8__combobox"]', 'National passport')
        self.sleep(1)  # Wait briefly for the dropdown options to appear

        # Use XPath to select "Ghana" from the dropdown list
        self.click("//ul[@id='vs8__listbox']//li[contains(text(), 'National passport')]")


        self.type("//label[contains(text(), '1.2 Passport number *')]/following-sibling::input", 'G2623324')


        self.type("//label[contains(text(), '1.3 Authority of issue *')]/following-sibling::input", 'Accra')

        first_input_xpath = "(//input[@type='text' and @readonly='readonly' and contains(@class, 'block w-full px-3 py-2 text-black')])[1]"
        self.click(first_input_xpath)

        # Click the arrow to navigate back through the years until 1991 is visible
        while not self.is_element_visible("//button[@aria-label='2020']"):
            # Click the back arrow button
            self.click('button[aria-label="Prev Year"]')

        # Click on the year 1991 once it is visible
        self.wait_for_element_visible("//button[@aria-label='2020']")
        self.click("//button[@aria-label='2020']")

        self.wait_for_element_visible("//button[@aria-label='August, 2020']")
        self.click("//button[@aria-label='August, 2020']")

        self.wait_for_element_visible("//button[@aria-label='27 August 2020']")
        self.click("//button[@aria-label='27 August 2020']")

        self.type("//label[contains(text(), '1.8 Validity *')]/following-sibling::input", 'Yes')

        first_input_xpath = "(//input[@type='text' and @readonly='readonly' and contains(@class, 'block w-full px-3 py-2 text-black')])[2]"
        self.click(first_input_xpath)

        # Click the arrow to navigate back through the years until 1991 is visible
        while not self.is_element_visible("//button[@aria-label='2030']"):
            # Click the back arrow button
            self.click('button[aria-label="Next Year"]')

        # Click on the year 1991 once it is visible
        self.wait_for_element_visible("//button[@aria-label='2030']")
        self.click("//button[@aria-label='2030']")

        self.wait_for_element_visible("//button[@aria-label='August, 2030']")
        self.click("//button[@aria-label='August, 2030']")

        self.wait_for_element_visible("//button[@aria-label='27 August 2030']")
        self.click("//button[@aria-label='27 August 2030']")

        self.click('button.m-6.md\\:m-0.md\\:ml-auto.py-2.px-8.w-full.md\\:w-auto.button.button-secondary')

        
        # Click on the input field using its class or aria attributes
        self.click('input[aria-labelledby="vs10__combobox"]')  # Click the search input field

        # Type "Ghana" into the input field to trigger the dropdown
        self.type('input[aria-labelledby="vs10__combobox"]', 'Yes')
        self.sleep(1)  # Wait briefly for the dropdown options to appear

        # Use XPath to select "Ghana" from the dropdown list
        self.click("//ul[@id='vs10__listbox']//li[contains(text(), 'Yes')]")
        

        # Type "Ghana" into the input field to trigger the dropdown
        self.type('input[aria-labelledby="vs12__combobox"]', 'Tourism')

        self.click("//ul[@id='vs12__listbox']//li[contains(text(), 'Tourism')]")

        first_input_xpath = "(//input[@type='text' and @readonly='readonly' and contains(@class, 'block w-full px-3 py-2 text-black')])[1]"
        self.click(first_input_xpath)

        self.wait_for_element_visible("//button[@aria-label='December, 2024']")
        self.click("//button[@aria-label='December, 2024']")

        self.wait_for_element_visible("//button[@aria-label='11 December 2024']")
        self.click("//button[@aria-label='11 December 2024']")

        self.sleep(3)

        first_input_xpath = "(//input[@type='text' and @readonly='readonly' and contains(@class, 'block w-full px-3 py-2 text-black')])[2]"
        self.click(first_input_xpath)


        self.wait_for_element_visible("//button[@aria-label='December, 2024']")
        self.click("//button[@aria-label='December, 2024']")

        self.wait_for_element_visible("//button[@aria-label='27 December 2024']")
        self.click("//button[@aria-label='27 December 2024']")

        self.type("//label[contains(text(), '1.8 Duration of stay(days) *')]/following-sibling::input", '15')

        self.type("//label[contains(text(), '1.9 Means of transport *')]/following-sibling::input", 'Air')

        self.type('input[aria-labelledby="vs14__combobox"]', 'Tirana Airport')
        
        self.click("//ul[@id='vs14__listbox']//li[contains(text(), 'Tirana Airport')]")

        

        self.type("//label[contains(text(), '1.11 Current occupation *')]/following-sibling::input", 'Teacher')

        self.type('input[aria-labelledby="vs15__combobox"]', 'Yes')

        self.click("//ul[@id='vs15__listbox']//li[contains(text(), 'Yes')]")

        self.type("//label[contains(text(), '1.13 Authority of issue *')]/following-sibling::input", 'Ghana')

        self.type("//label[contains(text(), '2.1 Other visas (issued during the past three years) and their period of validity *')]/following-sibling::input", 'None')

        self.type('input[aria-labelledby="vs16__combobox"]', 'None')

        self.click("//ul[@id='vs16__listbox']//li[contains(text(), 'None')]")

        self.click('button.m-6.md\\:m-0.md\\:ml-auto.py-2.px-8.w-full.md\\:w-auto.button.button-secondary')

        self.sleep(3)

        self.click('button.m-6.md\\:m-0.md\\:ml-auto.py-2.px-8.w-full.md\\:w-auto.button.button-secondary')

        self.sleep(3)

        self.type('input[aria-labelledby="vs24__combobox"]', 'Institution/Organization')

        self.click("//ul[@id='vs24__listbox']//li[contains(text(), 'Institution/Organization')]")

        self.type("//label[contains(text(), '1.2 Name (if it is company, institution, organization) *')]/following-sibling::input", 'Ghana')

        self.type("//label[contains(text(), '1.3 Name *')]/following-sibling::input", 'Ghana')

        self.type("//label[contains(text(), '1.4 Surname *')]/following-sibling::input", 'Ghana')

        self.type("//label[contains(text(), '1.7 Telephone and fax *')]/following-sibling::input", '+355878654534')

        self.type("//label[contains(text(), '1.8 E-mail address *')]/following-sibling::input", 'info@hana.com')

        self.type("//label[contains(text(), '1.9 Full address *')]/following-sibling::input", 'Ghana')

        self.type("//label[contains(text(), '1.10 Personal number of host *')]/following-sibling::input", '+355878654534')

        self.type("//label[contains(text(), '1.12 Please specify who and how *')]/following-sibling::input", 'Ghana')

        self.type('input[aria-labelledby="vs26__combobox"]', 'Myself')

        self.click("//ul[@id='vs26__listbox']//li[contains(text(), 'Myself')]")

        self.type('input[aria-labelledby="vs27__combobox"]', 'Credit Card')

        self.click("//ul[@id='vs27__listbox']//li[contains(text(), 'Credit Card')]")

        self.click('button.m-6.md\\:m-0.md\\:ml-auto.py-2.px-8.w-full.md\\:w-auto.button.button-secondary')

        self.type("//label[contains(text(), '1.1 Applicant`s home address *')]/following-sibling::input", '80 West ebd rd Accra')

        self.type("//label[contains(text(), '1.2 Telephone number *')]/following-sibling::input", '+233878654534')

        self.type("//label[contains(text(), '1.3 E-mail address *')]/following-sibling::input", 'tickets21@waaptravels.com')

        self.type("//label[contains(text(), '1.4 Place and date *')]/following-sibling::input", 'Accra, 07/09/2024')

        self.click('button.m-6.md\\:m-0.md\\:ml-auto.py-2.px-8.w-full.md\\:w-auto.button.button-secondary')

        
        # Set the relative path to the file and construct the full path
        employment = "students/59/payslip.pdf"  # Relative path to the file
        file_path = os.path.abspath(employment)  # Construct the absolute path from the relative path

        first_file_input_xpath = "(//input[@type='file' and @accept='application/pdf'])[1]"
        self.choose_file(first_file_input_xpath, file_path)

        photosize = "students/59/photo.png"  # Relative path to the file
        file_path = os.path.abspath(photosize)  # Construct the absolute path from the relative path

        first_file_input_xpath = "(//input[@type='file' and @accept='image/jpeg, image/jpeg, image/png'])"
        self.choose_file(first_file_input_xpath, file_path)

        self.sleep(5)

        self.click('button.bg-green-500.text-white.font-bold.uppercase.px-6.py-3.rounded.shadow')



        booking = "students/59/payslip.pdf"  # Relative path to the file
        file_path = os.path.abspath(booking)  # Construct the absolute path from the relative path

        first_file_input_xpath = "(//input[@type='file' and @accept='application/pdf'])[3]"
        self.choose_file(first_file_input_xpath, file_path)

        statement = "students/59/payslip.pdf"  # Relative path to the file
        file_path = os.path.abspath(statement)  # Construct the absolute path from the relative path

        first_file_input_xpath = "(//input[@type='file' and @accept='application/pdf'])[4]"
        self.choose_file(first_file_input_xpath, file_path)


        ticket = "students/59/payslip.pdf"  # Relative path to the file
        file_path = os.path.abspath(ticket)  # Construct the absolute path from the relative path

        first_file_input_xpath = "(//input[@type='file' and @accept='application/pdf'])[5]"
        self.choose_file(first_file_input_xpath, file_path)

        file_path = os.path.abspath(statement)  # Construct the absolute path from the relative path

        first_file_input_xpath = "(//input[@type='file' and @accept='application/pdf'])[7]"
        self.choose_file(first_file_input_xpath, file_path)

        passport = "students/59/payslip.pdf"  # Relative path to the file
        file_path = os.path.abspath(passport)  # Construct the absolute path from the relative path

        first_file_input_xpath = "(//input[@type='file' and @accept='application/pdf'])[8]"
        self.choose_file(first_file_input_xpath, file_path)

        self.sleep(3)

        self.click("//button[contains(., 'Finalize')]")

        
        self.sleep(5000)

        self.click('button.m-6.md\\:m-0.md\\:ml-auto.py-2.px-8.w-full.md\\:w-auto.button.button-secondary')



BaseCase.main(__name__, __file__)
