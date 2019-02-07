import smtplib, ssl
from easygui import passwordbox

port = 465  # For SSL
password = passwordbox("Type your password and press enter: ")
#password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("gptest483@gmail.com", password)
    # TODO: Send email here
