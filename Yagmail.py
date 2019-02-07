import yagmail
from easygui import passwordbox

username="gptest483@gmail.com"
password = passwordbox("Type your password and press enter: ")
yagmail.register(username, password)

receiver = "matterisfull@gmail.com"
body = "Hello there from Yagmail"
filename = "resume.pdf"

yag = yagmail.SMTP("gptest483@gmail.com")

yag.send(
    to=receiver,
    subject="Yagmail test with attachment",
    contents=body,
    attachments=filename,
)