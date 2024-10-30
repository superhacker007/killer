import imaplib
import email
from email.header import decode_header
from email.utils import parseaddr
from datetime import datetime
import os

def fetch_emails(mail, download_folder="attachments"):
    """Fetch emails and extract their attachments if available."""
    mail.select("INBOX")  # Select the inbox folder

    # Search for all emails (you can use 'UNSEEN' for unread emails)
    status, messages = mail.uid('search', None, 'ALL')

    if status != "OK":
        print("Failed to fetch emails!")
        return []

    email_uids = messages[0].split()
    print(f"Total emails found: {len(email_uids)}")

    emails = []  # List to store email data

    # Create the download folder if it doesn't exist
    os.makedirs(download_folder, exist_ok=True)

    for i, uid in enumerate(email_uids):
        print(f"Fetching email {i + 1} / {len(email_uids)} with UID: {uid.decode()}")

        # Fetch the email by UID
        status, msg_data = mail.uid('fetch', uid, '(RFC822)')

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

        # Store email data in a dictionary
        email_data = {
            "uid": uid.decode(),
            "from": email_address,
            "name": name,
            "subject": subject,
            "body": body,
            "attachments": attachments,  # List of attachment filenames
            "date": date_obj.strftime('%Y-%m-%d %H:%M:%S') if date_obj else "N/A",
        }

        emails.append(email_data)
        print(f"Email {i + 1} added: {email_data}")

    print(f"Total emails fetched: {len(emails)}")
    return emails

def parse_email_body(msg):
    """Extract the body of the email, handling both plain text and HTML."""
    body = ""
    if msg.is_multipart():
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

            if content_type == "text/plain":
                body += part_body  # Append plain text body
            elif content_type == "text/html":
                body += f"\n\n[HTML Content]\n\n{part_body}"  # Mark HTML content
    else:
        try:
            body = msg.get_payload(decode=True).decode()
        except Exception as e:
            print(f"Failed to decode email body: {e}")
            body = "[Failed to decode body]"

    return body.strip()

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
    mail = connect_to_email("linda@workgh.com", "GreatNews@2024")

    if mail:
        try:
            emails = fetch_emails(mail)
        finally:
            mail.logout()  # Ensure the connection is closed
        return emails

    return []

# Example usage
if __name__ == "__main__":
    emails = get_mails()
    for email_data in emails:
        print(email_data)
