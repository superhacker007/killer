import requests

# API endpoint for fetching student details
API_URL = "https://waap.replit.app/studentsapi"

def get_new_students():
    # Send GET request to fetch all student details
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        all_students = response.json()
        print("Fetched all student details.")

        # Filter students where status is 'new'
        new_students = [student for student in all_students if student.get('student_status') == 'new']
        
        if new_students:
            print(f"Found {len(new_students)} student(s) with status 'new'.")
            # Process each student with 'new' status
            for student in new_students:
                perform_task(student)
                update_student_status(student['id'], 'new')
        else:
            print("No students with status 'new' found.")
    else:
        print(f"Failed to fetch data. Status Code: {response.status_code}")

def perform_task(student_data):
    # Example task: printing student's full name
    full_name = f"{student_data['firstname']} {student_data['lastname']}"
    print(f"Processing student: {full_name}")
    
    # You can perform other tasks here based on your business logic
    # For now, we assume the task has been completed

def update_student_status(student_id, new_status):
    # API endpoint for updating student status
    update_url = f"{API_URL}/update/{student_id}"
    
    # Data to be updated
    update_data = {
        "student_status": new_status
    }
    
    # Send PATCH request to update the student status
    response = requests.patch(update_url, json=update_data)
    
    if response.status_code == 200:
        print(f"Successfully updated student status to '{new_status}' for student ID {student_id}")
    else:
        print(f"Failed to update status for student ID {student_id}. Status Code: {response.status_code}")

# Run the script
if __name__ == "__main__":
    get_new_students()
