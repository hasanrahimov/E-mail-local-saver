import os
import imaplib
import email
from email.header import decode_header
from email.utils import parsedate_to_datetime

def clean(text):
    # Clean the text for creating a valid folder/file name
    return "".join(c if c.isalnum() or c in [' ', '.', '_'] else '_' for c in text)

imap_url = 'imap.gmail.com' # Imap server url

my_email = input("Enter your email login: ")
password_key = input("Enter your email password: ")

my_mail = imaplib.IMAP4_SSL(imap_url) # Secure IMAP connection
my_mail.login(my_email, password_key) # Login

my_mail.select("INBOX") # Inbox folder

# Create a directory to save emails, if it doesn't exist yet
save_dir = "Saved-E-mails"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

aaa, data = my_mail.search(None, 'ALL') # Search for all emails in the inbox folder

# Iteration for each found email
for num in data[0].split():
    aaa, message_data = my_mail.fetch(num, "(RFC822)") # Fetching email data
    message = email.message_from_bytes(message_data[0][1]) # Parsing data

    sender_email = message.get("From") # Extracting sender's email adress
    sender_folder = os.path.join(save_dir, clean(sender_email)) # Create folder for the sender(also cleaning the adress for valid folder name)

    # Check if there are attachments
    has_attachments = any(part.get_content_maintype() != 'multipart' and part.get('Content-Disposition') is not None for part in message.walk())
    
    # If there are attachments, create a folder based on received date
    if has_attachments:
        date_received = parsedate_to_datetime(message.get("Date"))
        date_str = date_received.strftime("%d%m%Y%H%M%S")
        email_folder = os.path.join(sender_folder, date_str)

        if not os.path.exists(email_folder):
            os.makedirs(email_folder)

        # Save the email content to a file
        email_filepath = os.path.join(email_folder, "email.txt")
        # Opens email folder to write with utf-8 encoding
        with open(email_filepath, "w", encoding="utf-8") as file:
            file.write(f"From: {message.get('From')}\n")
            file.write(f"To: {message.get('To')}\n")
            file.write(f"Date: {message.get('Date')}\n")
            file.write(f"Subject: {message.get('Subject')}\n\n")

            file.write("Content:\n")
            # Iteration through each part of the email
            for part in message.walk(): 
                # If the part is a plain text, then write the text content to the file
                if part.get_content_type() == "text/plain":
                    file.write(part.as_string())

            # Iteration through each part of the message
            for part in message.walk():
                # Check if part is not a multipart type and has a content disposition header, which stands for an attachment indication
                if part.get_content_maintype() != 'multipart' and part.get('Content-Disposition') is not None:
                    filename, encoding = decode_header(part.get_filename())[0] # Decode filename using the decode header function, and take the first item from the result
                    # If the filename is bytes obj, decode it to string using the previously found encoding or utf-8, if encoding was None
                    if isinstance(filename, bytes):
                        filename = filename.decode(encoding or 'utf-8')
                    
                    # Creation of full path, where the attachment will be saved, including filename valid for the file  system
                    attachment_path = os.path.join(email_folder, clean(filename))
                    
                    # Opens the file in binary write and save the attachment
                    with open(attachment_path, "wb") as attachment_file:
                        attachment_file.write(part.get_payload(decode=True))
    else:
        # If there are no attachments, create a txt file directly
        date_received = parsedate_to_datetime(message.get("Date"))
        date_str = date_received.strftime("%d%m%Y%H%M%S")
        email_filepath = os.path.join(sender_folder, f"{date_str}_email.txt")
        
        # Opens email folder to write with utf-8 encoding
        with open(email_filepath, "w", encoding="utf-8") as file:
            file.write(f"From: {message.get('From')}\n")
            file.write(f"To: {message.get('To')}\n")
            file.write(f"Date: {message.get('Date')}\n")
            file.write(f"Subject: {message.get('Subject')}\n\n")

            file.write("Content:\n")
            for part in message.walk():
                if part.get_content_type() == "text/plain":
                    file.write(part.as_string())

my_mail.close()
