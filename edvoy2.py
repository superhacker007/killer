import requests
from edvoy import MyTestClass

# Define the API endpoint
API_URL = "https://waap.replit.app/studentsapi"

# Function to update student status (if needed in your workflow)
def update_student_status(student_id, status):
    # This is a placeholder. Implement this function to send a request
    # back to the API to update the student status, if applicable.
    pass

# Fetch student data from the API
response = requests.get(API_URL)

if response.status_code == 200:
    all_students = response.json()
    print("Fetched all student details.")

    # Filter students where status is 'ready'
    new_students = [student for student in all_students if student['student_status'] == 'ready']
    
    if new_students:
        print(f"Found {len(new_students)} student(s) with status 'ready'.")
        
        # Process each student with 'ready' status
        for student in new_students:
            tester = MyTestClass()  # Initialize the test class

            try:
                # Set up the Selenium environment
                tester.setUp()
                
                # Run the form automation using the student data
                tester.do_student(student)

                # Optional: Update the student status to 'applying' or something else
                # update_student_status(student['id'], 'applying')

            finally:
                # Ensure the Selenium browser is closed even if an error occurs
                tester.tearDown()
    else:
        print("No students with status 'ready' found.")
else:
    print(f"Failed to fetch data. Status Code: {response.status_code}")
