# main.py

from content_generation import generate_newsletter_content
from email_sender import send_newsletter
from users import load_users

def main():
    # Generate newsletter content
    newsletter_content = generate_newsletter_content()

    # Load users from file
    users = load_users()

    # Send newsletter via email
    subject = "Your Weekly Newsletter"
    send_newsletter(subject, newsletter_content, users)

if __name__ == "__main__":
    main()