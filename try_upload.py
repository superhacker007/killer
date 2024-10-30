import os
from seleniumbase import BaseCase

class FileUploadButtonTests(BaseCase):
    def test_file_upload_button(self):
        # Open the URL with the file upload button
        self.open("https://seleniumbase.io/w3schools/file_upload")
        
        # Click the "Run" button to interact with the iframe containing the file input
        self.click("button#runbtn")
        self.switch_to_frame("iframeResult")

        # Set the relative path to the file and construct the full path
        my_file = "students/59/payslip.pdf"  # Relative path to the file
        file_path = os.path.abspath(my_file)  # Construct the absolute path from the relative path

        # Ensure the file exists at the specified path
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        # Print the file path for verification
        print(f"Uploading file from: {file_path}")

        # Verify the file input is empty before uploading
        self.assert_attribute("#myFile", "value", "")

        # Use choose_file() to upload the file
        self.choose_file('input[type="file"]', file_path)

        self.sleep(3)  # Pause to observe the upload action

BaseCase.main(__name__, __file__)
