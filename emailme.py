import requests

def create_email(emailname, forward_to, forward_to_second):
    # Configuration
    cpanel_user = 'worktzjw'
    cpanel_password = 'mnZIn2PuQrkk'
    cpanel_domain = 'workgh.com'
    email_domain = 'workgh.com'
    email_user = emailname
    email_password = 'GreatNews@2024'
    email_quota = 102  # Quota in MB

    # cPanel API endpoint
    cpanel_url = f'https://{cpanel_domain}:2083/json-api/cpanel'

    # API token or basic authentication
    auth = (cpanel_user, cpanel_password)

    # Create the email account
    params_create_email = {
        'cpanel_jsonapi_user': cpanel_user,
        'cpanel_jsonapi_apiversion': '2',
        'cpanel_jsonapi_module': 'Email',
        'cpanel_jsonapi_func': 'addpop',
        'domain': email_domain,
        'email': email_user,
        'password': email_password,
        'quota': email_quota,
    }

    response_create_email = requests.get(cpanel_url, params=params_create_email, auth=auth, verify=False)

    if response_create_email.status_code == 200:
        print("Email account created successfully.")
        
        # Create primary email forwarding
        create_forwarding(cpanel_url, auth, email_user, email_domain, forward_to)
        
        # Create secondary email forwarding
        create_forwarding(cpanel_url, auth, email_user, email_domain, forward_to_second)

    else:
        print("Failed to create email account.")
        print(response_create_email.text)

def create_forwarding(cpanel_url, auth, email_user, email_domain, forward_to):
    """Helper function to create email forwarding."""
    params_create_forwarding = {
        'cpanel_jsonapi_user': auth[0],
        'cpanel_jsonapi_apiversion': '2',
        'cpanel_jsonapi_module': 'Email',
        'cpanel_jsonapi_func': 'addforward',
        'domain': email_domain,
        'email': f'{email_user}@{email_domain}',
        'fwdopt': 'fwd',
        'fwdemail': forward_to,
    }

    response_create_forwarding = requests.get(cpanel_url, params=params_create_forwarding, auth=auth, verify=False)

    if response_create_forwarding.status_code == 200:
        print(f"Email forwarding to {forward_to} created successfully.")
    else:
        print(f"Failed to create email forwarding to {forward_to}.")
        print(response_create_forwarding.text)