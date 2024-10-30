from seleniumbase import BaseCase
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pytest
import json, os, requests
import undetected_chromedriver as uc


class MyTestClass(BaseCase):
    def setUp(self):
        # Call SeleniumBase's setUp() to initialize required variables
        super().setUp()

        options = Options()
        # Use undetected-chromedriver for Chrome
        options = uc.ChromeOptions()
        options.add_argument("user-data-dir=/Users/Augustine/chrome_profiles/edvoy")  # Path to your Chrome profile
        
        # Use undetected-chromedriver
        self.driver = uc.Chrome(options=options)

    # @pytest.fixture(autouse=True)

    def do_student(self, student):
        # Use student_id directly
        
        print(f"Running tests with Student ID: {student['firstname']}")
        self.open("https://partners.edvoy.com/student")
        self.sleep(10)  # Wait for page to load completely

        # Click the 'Create Student' button
        self.click('button:contains("Create Student")')
        print(student['firstname'])
        self.sleep(5) 

        # Fill in the form using the student details from JSON
        self.wait_for_element_visible('input[placeholder="Example: John"]', timeout=30)
        self.type('input[placeholder="Example: John"]', student['firstname'])  # First name
        self.type('input[placeholder="Example: Doe"]', student['lastname'])    # Last name
        self.type('input[placeholder="Johndoe@example.com"]', student['email2all']) # Email
        self.type('input[placeholder="Enter a number"]', student['phonen'])   # Phone number
        
        # Select gender based on student.sex
        # Step 1: Click to open the dropdown
        self.click('span:contains("Please Select")')  # Click to open the dropdown
        
        # Step 2: Click the appropriate gender option based on the value
        if student['sex'] == "m":
            self.click('li:contains("Male")')  # Adjust the selector to match the "Male" option
        else:
            self.click('li:contains("Female")')  # Adjust the selector to match the "Female" option
        
        # Continue filling the form
        self.sleep(5)  # Shorter pause

         # Interact with the custom date picker to select "27th August 1991"
        # Step 1: Click on the date input to open the date picker
        self.click('div.relative.w-full.h-10.bg-white')  # Clicking the main div with specific classes

        # Step 2: Click on the year to open the dropdown of years
        self.click('span.ml-1.cursor-pointer.font-medium.text-sm.text-gray-800')  # Clicks the displayed year (e.g., "2011")

        myyear = student['myyear']
        mymonth = student['mymonth']
        myday = student['myday']

        # Step 3: Scroll and click on the specified year from the dropdown list of years
        self.scroll_to(f'li:contains("{myyear}")')  # Scrolls to the specified year
        self.click(f'li:contains("{myyear}")')  # Clicks on the specified year

         # Step 1: Click on the current month (e.g., "September") to open the dropdown list of months
        self.click('span.cursor-pointer.font-medium.text-sm.text-gray-800')  # Clicks the current month

        # Step 2: Select "December" from the dropdown list
        self.click(f'li:contains("{mymonth}")') 

        # Select the specified day
        self.click(f'button[type="button"] div.cursor-pointer:contains("{myday}")')  # Click on the specified day

        self.sleep(5)

        self.wait_for_element_visible('(//span[contains(text(), "Please Select")])[2]', timeout=10)
        self.scroll_to('(//span[contains(text(), "Please Select")])[2]')
        self.click('(//span[contains(text(), "Please Select")])[2]') 


        # Step 2: Type "English" into the search box
        self.wait_for_element_visible('input[placeholder="Type to Search for more..."]', timeout=10)
        self.type('input[placeholder="Type to Search for more..."]', 'English')  # Types "English" into the input box

        # Step 3: Wait for and select "English" from the dropdown
        self.wait_for_element_visible('div.text-gray-600.hover\\:bg-gray-50.hover\\:text-gray-800.relative.py-2.px-4.flex.items-center.capitalize.text-sm:contains("English")', timeout=10)
        self.click('div.text-gray-600.hover\\:bg-gray-50.hover\\:text-gray-800.relative.py-2.px-4.flex.items-center.capitalize.text-sm:contains("English")')  # Clicks on "English" from the dropdown
        
        self.wait_for_element_visible('(//span[contains(text(), "Please Select")])[3]', timeout=10)
        self.scroll_to('(//span[contains(text(), "Please Select")])[3]')
        self.click('(//span[contains(text(), "Please Select")])[3]') 


        # Step 2: Type "English" into the search box
        self.wait_for_element_visible('input[placeholder="Type to Search for more..."]', timeout=10)
        self.type('input[placeholder="Type to Search for more..."]', 'English')  # Types "English" into the input box

       # Wait for the checkbox near the label "English" to be visible and click it
        self.wait_for_element_visible('//label[span[text()="English"]]/preceding-sibling::input[@type="checkbox"]', timeout=10)
        self.scroll_to('//label[span[text()="English"]]/preceding-sibling::input[@type="checkbox"]')
        self.click('//label[span[text()="English"]]/preceding-sibling::input[@type="checkbox"]')  # Click the checkbox near "English"
        

        # Wait for the fourth "Please Select" button to be visible
        self.wait_for_element_visible('(//button[contains(@class, "autocomplete-popper-btn") and .//span[contains(text(), "Please Select")]])[4]', timeout=10)

        # Scroll the element into view using JavaScript
        self.execute_script('arguments[0].scrollIntoView(true);', self.find_element('(//button[contains(@class, "autocomplete-popper-btn") and .//span[contains(text(), "Please Select")]])[4]'))

        # Click the element using JavaScript to bypass the interception
        self.execute_script('arguments[0].click();', self.find_element('(//button[contains(@class, "autocomplete-popper-btn") and .//span[contains(text(), "Please Select")]])[4]'))

        
        # Click the button containing "Please Select"



        # Step 2: Type "Ghana" into the search box
        self.wait_for_element_visible('input[placeholder="Type to Search for more..."]', timeout=10)
        self.type('input[placeholder="Type to Search for more..."]', 'Ghana')  # Types "Ghana" into the input box

        # Step 3: Wait for and select "Ghana" from the dropdown
        self.wait_for_element_visible('div.text-gray-600.hover\\:bg-gray-50.hover\\:text-gray-800.relative.py-2.px-4.flex.items-center.capitalize.text-sm:contains("Ghana")', timeout=10)
        self.click('div.text-gray-600.hover\\:bg-gray-50.hover\\:text-gray-800.relative.py-2.px-4.flex.items-center.capitalize.text-sm:contains("Ghana")')  # Clicks on "Ghana" from the dropdown
        
        

        # Wait for the fourth "Please Select" button to be visible
        self.wait_for_element_visible('(//button[contains(@class, "autocomplete-popper-btn") and .//span[contains(text(), "Please Select")]])[5]', timeout=10)

        # Scroll the element into view using JavaScript
        self.execute_script('arguments[0].scrollIntoView(true);', self.find_element('(//button[contains(@class, "autocomplete-popper-btn") and .//span[contains(text(), "Please Select")]])[5]'))

        # Click the element using JavaScript to bypass the interception
        self.execute_script('arguments[0].click();', self.find_element('(//button[contains(@class, "autocomplete-popper-btn") and .//span[contains(text(), "Please Select")]])[5]'))

        
        # Click the button containing "Please Select"
        # Step 2: Type "Ghana" into the search box
        self.wait_for_element_visible('input[placeholder="Type to Search for more..."]', timeout=10)
        self.type('input[placeholder="Type to Search for more..."]', 'Ghana')  # Types "Ghana" into the input box

        # Step 3: Wait for and select "Ghana" from the dropdown
        self.wait_for_element_visible('div.text-gray-600.hover\\:bg-gray-50.hover\\:text-gray-800.relative.py-2.px-4.flex.items-center.capitalize.text-sm:contains("Ghana")', timeout=10)
        self.click('div.text-gray-600.hover\\:bg-gray-50.hover\\:text-gray-800.relative.py-2.px-4.flex.items-center.capitalize.text-sm:contains("Ghana")')  # Clicks on "Ghana" from the dropdown
        



        # Wait for the fourth "Please Select" button to be visible
        self.wait_for_element_visible('(//button[contains(@class, "autocomplete-popper-btn") and .//span[contains(text(), "Please Select")]])[6]', timeout=10)

        # Scroll the element into view using JavaScript
        self.execute_script('arguments[0].scrollIntoView(true);', self.find_element('(//button[contains(@class, "autocomplete-popper-btn") and .//span[contains(text(), "Please Select")]])[6]'))

        # Click the element using JavaScript to bypass the interception
        self.execute_script('arguments[0].click();', self.find_element('(//button[contains(@class, "autocomplete-popper-btn") and .//span[contains(text(), "Please Select")]])[6]'))


        # Step 2: Type "Ghana" into the search box
        self.wait_for_element_visible('input[placeholder="Type to Search for more..."]', timeout=10)
        self.type('input[placeholder="Type to Search for more..."]', 'Accra')  # Types "Ghana" into the input box

        # Step 3: Wait for and select "Ghana" from the dropdown
        self.wait_for_element_visible('div.text-gray-600.hover\\:bg-gray-50.hover\\:text-gray-800.relative.py-2.px-4.flex.items-center.capitalize.text-sm:contains("Accra Greater Accra Ghana")', timeout=10)
        self.click('div.text-gray-600.hover\\:bg-gray-50.hover\\:text-gray-800.relative.py-2.px-4.flex.items-center.capitalize.text-sm:contains("Accra Greater Accra Ghana")')  # Clicks on "Ghana" from the dropdown
        
        
        
        
        
        # Wait for the fourth "Please Select" button to be visible
        self.wait_for_element_visible('(//button[contains(@class, "autocomplete-popper-btn") and .//span[contains(text(), "Please Select")]])[7]', timeout=10)

        # Scroll the element into view using JavaScript
        self.execute_script('arguments[0].scrollIntoView(true);', self.find_element('(//button[contains(@class, "autocomplete-popper-btn") and .//span[contains(text(), "Please Select")]])[7]'))

        # Click the element using JavaScript to bypass the interception
        self.execute_script('arguments[0].click();', self.find_element('(//button[contains(@class, "autocomplete-popper-btn") and .//span[contains(text(), "Please Select")]])[7]'))


        # Step 3: Wait for and select "Ghana" from the dropdown
        self.wait_for_element_visible('div.text-gray-600.hover\\:bg-gray-50.hover\\:text-gray-800.relative.py-2.px-4.flex.items-center.capitalize.text-sm:contains("Has Passport")', timeout=10)
        self.click('div.text-gray-600.hover\\:bg-gray-50.hover\\:text-gray-800.relative.py-2.px-4.flex.items-center.capitalize.text-sm:contains("Has Passport")')  # Clicks on "Ghana" from the dropdown
        
        self.sleep(5)
        # Click the 'Create Student' button
        self.click('button:contains("Create Student")')



        self.open("https://partners.edvoy.com/student")

        self.sleep(10)

        # Wait for the input field to be visible and type into it
        self.wait_for_element_visible('input[placeholder="Search Student by Name,Email"]', timeout=10)
        self.scroll_to('input[placeholder="Search Student by Name,Email"]')
        self.type('input[placeholder="Search Student by Name,Email"]', student['firstname'] + ' ' + student['lastname'])  # Replace '{{current_user.username}}' with the search query

        # Combine firstname and lastname for the dynamic text
        full_name = student['firstname'] + " " + student['lastname']

        # Use CSS Selector with the combined name
        self.wait_for_element_visible(f'div.cursor-pointer.capitalize:contains("{full_name}")', timeout=10)
        self.scroll_to(f'div.cursor-pointer.capitalize:contains("{full_name}")')
        self.click(f'div.cursor-pointer.capitalize:contains("{full_name}")')  # Click the div


        # Use XPath to target the div containing the text "Study Preferences"
        self.wait_for_element_visible('//div[contains(@class, "flex") and contains(text(), "Study Preferences")]', timeout=10)
        self.scroll_to('//div[contains(@class, "flex") and contains(text(), "Study Preferences")]')
        self.click('//div[contains(@class, "flex") and contains(text(), "Study Preferences")]')  # Click the div

        self.sleep(5)

        # Wait for the first instance of the "United Kingdom" button to be visible and click it
        self.wait_for_element_visible('(//button[contains(@class, "app-button") and contains(@class, "app-button--white") and contains(@class, "app-button--xs") and contains(@class, "app-button--rounded") and contains(@class, "m-1")])[2]', timeout=10)
        self.scroll_to('(//button[contains(@class, "app-button") and contains(@class, "app-button--white") and contains(@class, "app-button--xs") and contains(@class, "app-button--rounded") and contains(@class, "m-1")])[2]')
        self.click('(//button[contains(@class, "app-button") and contains(@class, "app-button--white") and contains(@class, "app-button--xs") and contains(@class, "app-button--rounded") and contains(@class, "m-1")])[2]')  # Click the first button


        # Wait for the first instance of the "United Kingdom" button to be visible and click it
        self.wait_for_element_visible('(//button[contains(@class, "app-button") and contains(@class, "app-button--white") and contains(@class, "app-button--xs") and contains(@class, "app-button--rounded") and contains(@class, "m-1")])[14]', timeout=10)
        self.scroll_to('(//button[contains(@class, "app-button") and contains(@class, "app-button--white") and contains(@class, "app-button--xs") and contains(@class, "app-button--rounded") and contains(@class, "m-1")])[14]')
        self.click('(//button[contains(@class, "app-button") and contains(@class, "app-button--white") and contains(@class, "app-button--xs") and contains(@class, "app-button--rounded") and contains(@class, "m-1")])[14]')  # Click the first button


        self.wait_for_element_visible('(//button[contains(@class, "app-button") and contains(@class, "app-button--white") and contains(@class, "app-button--xs") and contains(@class, "app-button--rounded") and contains(@class, "m-1")])[21]', timeout=10)
        self.scroll_to('(//button[contains(@class, "app-button") and contains(@class, "app-button--white") and contains(@class, "app-button--xs") and contains(@class, "app-button--rounded") and contains(@class, "m-1")])[21]')
        self.click('(//button[contains(@class, "app-button") and contains(@class, "app-button--white") and contains(@class, "app-button--xs") and contains(@class, "app-button--rounded") and contains(@class, "m-1")])[21]')  # Click the first button


        self.wait_for_element_visible('(//button[contains(@class, "app-button") and contains(@class, "app-button--white") and contains(@class, "app-button--xs") and contains(@class, "app-button--rounded") and contains(@class, "m-1")])[25]', timeout=10)
        self.scroll_to('(//button[contains(@class, "app-button") and contains(@class, "app-button--white") and contains(@class, "app-button--xs") and contains(@class, "app-button--rounded") and contains(@class, "m-1")])[25]')
        self.click('(//button[contains(@class, "app-button") and contains(@class, "app-button--white") and contains(@class, "app-button--xs") and contains(@class, "app-button--rounded") and contains(@class, "m-1")])[25]')  # Click the first button

        self.sleep(5)

        self.wait_for_element_visible('(//span[contains(text(), "Please Select")])[1]', timeout=10)
        self.scroll_to('(//span[contains(text(), "Please Select")])[1]')
        self.click('(//span[contains(text(), "Please Select")])[1]') 

        # Step 2: Type the value from student['tostudy'] into the search box
        self.wait_for_element_visible('input[placeholder="Type to Search for more..."]', timeout=10)
        self.type('input[placeholder="Type to Search for more..."]', student['tostudy'])  # Types the desired value into the input box

        # Step 1: Wait for the checkbox associated with the label that has the text from student["tostudy"]
        self.wait_for_element_visible(f'//label[span[text()="{student["tostudy"]}"]]/preceding-sibling::input[@type="checkbox"]', timeout=10)

        # Step 2: Scroll to the checkbox element
        self.scroll_to(f'//label[span[text()="{student["tostudy"]}"]]/preceding-sibling::input[@type="checkbox"]')

        # Step 3: Click the checkbox
        self.click(f'//label[span[text()="{student["tostudy"]}"]]/preceding-sibling::input[@type="checkbox"]')


        # Wait for the "Save" button to be visible
        self.wait_for_element_visible('button[type="submit"].app-button.app-button--primary.app-button--md', timeout=10)

        # Scroll to the "Save" button to ensure it's in view
        self.scroll_to('button[type="submit"].app-button.app-button--primary.app-button--md')

        # Click the "Save" button
        self.click('button[type="submit"].app-button.app-button--primary.app-button--md')




    def tearDown(self):
        # Call SeleniumBase's tearDown() for cleanup
        super().tearDown()
