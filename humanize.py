import subprocess, json, time

def doit(content):
    # Define the curl command as a list of arguments, using the content variable
    curl_command = [
        "curl",
        "--location",
        "https://humanize.undetectable.ai/submit",
        "--header",
        "apikey: lWXvhMcjGL6GDfZdWeCAAXOZO3VMe0XT",
        "--header",
        "Content-Type: application/json",
        "--data",
        json.dumps({
            "content": content,
            "readability": "High School",
            "purpose": "General Writing",
            "strength": "More Human"
        })
    ]

    time.sleep(5)
    
    # Execute the curl command using subprocess
    try:
        result = subprocess.run(curl_command, capture_output=True, text=True, check=True)
        response_json = json.loads(result.stdout)  # Parse the JSON response
        document_id = response_json.get("id")  # Retrieve the document ID
        
        # Check if document ID is retrieved correctly
        if not document_id:
            print("Failed to retrieve document ID:", response_json)
            return

        print("Document ID:", document_id)

    except subprocess.CalledProcessError as e:
        print("An error occurred during the first request:", e.stderr)  # Print the error if the command fails
        return
    except json.JSONDecodeError:
        print("Failed to decode JSON response from the first request.")
        return

    time.sleep(5)

    # Define the second curl command to retrieve the document using the document_id
    curl_command2 = [
        "curl",
        "--location",
        "https://humanize.undetectable.ai/document",
        "--header",
        "apikey: lWXvhMcjGL6GDfZdWeCAAXOZO3VMe0XT",
        "--header",
        "Content-Type: application/json",
        "--data",
        json.dumps({"id": document_id})
    ]

    # Execute the second curl command using subprocess
    try:
        result = subprocess.run(curl_command2, capture_output=True, text=True, check=True)
        response_json = json.loads(result.stdout)  # Parse the JSON response
        
        # Print full response for debugging
        print("Full Response from the second request:", response_json)

        # Check for 'output' in the response
        output = response_json.get("output")
        if output is None:
            print("The 'output' key is missing in the response:", response_json)
        else:
            print("Response:", output)

    except subprocess.CalledProcessError as e:
        print("An error occurred during the second request:", e.stderr)  # Print the error if the command fails
    except json.JSONDecodeError:
        print("Failed to decode JSON response from the second request.")
