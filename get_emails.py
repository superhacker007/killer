import imaplib
import email
from email.header import decode_header
from email.utils import parseaddr
from datetime import datetime
import os
from flask_login import current_user

def fetch_emails(mail, download_folder="attachments"):
    """Fetch emails, extract their attachments, and determine read/unread status."""
    mail.select("INBOX")  # Select the inbox folder

    # Get the total number of emails
    status, all_messages = mail.uid('search', None, 'ALL')
    email_uids = all_messages[0].split()  # List of UIDs
    total_emails = len(email_uids)
    print(f"Total emails found: {total_emails}")

    # Sort UIDs in descending order (latest first)
    email_uids.sort(reverse=True, key=int)  # Convert UIDs to int for sorting

    # Search for unread emails
    status, unread_messages = mail.uid('search', None, 'UNSEEN')
    unread_uids = set(unread_messages[0].split())
    print(f"Unread emails: {len(unread_uids)}")

    emails = []  # List to store email data

    # Create the download folder if it doesn't exist
    os.makedirs(download_folder, exist_ok=True)

    for i, uid in enumerate(email_uids):
        print(f"Fetching email {i + 1} / {total_emails} with UID: {uid.decode()}")

        # Fetch the email by UID
        status, msg_data = mail.uid('fetch', uid, '(RFC822 FLAGS)')

        if status != "OK":
            print(f"Failed to fetch email UID {uid}")
            continue

        # Parse the email
        msg = email.message_from_bytes(msg_data[0][1])

        # Extract subject and decode it
        subject, encoding = decode_header(msg.get("Subject"))[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else "utf-8")

        # Extract sender's name and email address
        from_email = msg.get("From")
        name, email_address = parseaddr(from_email)

        # Extract the date
        date = msg.get("Date")
        date_obj = email.utils.parsedate_to_datetime(date) if date else None

        # Extract the email body
        body = parse_email_body(msg)

        # Extract attachments, if any
        attachments = extract_attachments(msg, download_folder)

        # Check if the email is unread (UID is in the unread_uids set)
        is_unread = uid in unread_uids

        # Store email data in a dictionary
        email_data = {
            "uid": uid.decode(),
            "from": email_address,
            "name": name,
            "subject": subject,
            "body": body,
            "attachments": attachments,  # List of attachment filenames
            "date": date_obj.strftime('%Y-%m-%d %H:%M:%S') if date_obj else "N/A",
            "unread": is_unread  # Boolean indicating if the email is unread
        }

        emails.append(email_data)
        print(f"Email {i + 1} added: {email_data}")

    print(f"Total emails fetched: {len(emails)}")
    return emails

def parse_email_body(msg):
    """Extract the body of the email, prioritizing HTML if available."""
    plain_text = ""
    html_content = ""

    if msg.is_multipart():
        # Iterate through email parts
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))

            # Skip attachments
            if "attachment" in content_disposition:
                continue

            try:
                part_body = part.get_payload(decode=True).decode()
            except Exception as e:
                print(f"Failed to decode part: {e}")
                continue

            # Store plain text and HTML separately
            if content_type == "text/plain":
                plain_text += part_body
            elif content_type == "text/html":
                html_content += part_body

    else:
        # If the email isn't multipart, treat it as a single part email
        try:
            payload = msg.get_payload(decode=True).decode()
            if msg.get_content_type() == "text/html":
                html_content = payload
            else:
                plain_text = payload
        except Exception as e:
            print(f"Failed to decode email body: {e}")
            return "[Failed to decode body]"

    # Return HTML content if available; otherwise, return plain text
    if html_content:
        return html_content.strip()
    elif plain_text:
        return plain_text.strip()
    else:
        return "[No content available]"


def extract_attachments(msg, download_folder):
    """Extract and save attachments from the email."""
    attachments = []  # List to store attachment filenames
    for part in msg.walk():
        content_disposition = str(part.get("Content-Disposition"))
        if "attachment" in content_disposition:
            filename = part.get_filename()
            if filename:
                filename, encoding = decode_header(filename)[0]
                if isinstance(filename, bytes):
                    filename = filename.decode(encoding if encoding else "utf-8")

                filepath = os.path.join(download_folder, filename)
                with open(filepath, "wb") as f:
                    f.write(part.get_payload(decode=True))
                attachments.append(filepath)
                print(f"Saved attachment: {filepath}")

    return attachments

def connect_to_email(username, password, imap_server="workgh.com"):
    """Connect to the email server using IMAP."""
    try:
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(username, password)
        return mail
    except Exception as e:
        print(f"Failed to connect: {e}")
        return None

def get_mails():
    """Connect to the email server, fetch emails, and return them."""
    mail = connect_to_email(current_user.email, "GreatNews@2024")

    if mail:
        try:
            emails = fetch_emails(mail)
        finally:
            mail.logout()  # Ensure the connection is closed
        return emails

    return []
