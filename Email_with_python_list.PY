import smtplib   #LIBRARY FOR SENDING THE MAIL OVER THE INTERNET FOR A VALID EMAIL ADDRESS
from email.mime.multipart import MIMEMultipart #FOR MAKING DIFFERENT PARTS IN THE SCRIPT AND CONNECTING ALL THE PARTS IN THE END
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
# list of email_id to send the mail
list = ["dishadwivedi233@gmail.com"]
for demon in list:
        shubh = smtplib.SMTP('smtp.gmail.com', 587)
        shubh.starttls()
        shubh.login("shubhdwivedimi@gmail.com", "shubhdisha22")
        gmail_gui = MIMEMultipart()
        # storing the senders email address
        gmail_gui['From'] = "SHUBHKANT DWIVEDI"
        # storing the receivers email address
        gmail_gui['To'] =  demon
        # storing the subject
        gmail_gui['Subject'] = "FIFA FOR LIFE"
        # string to store the body of the mail
        body = "I WOULD LIKE TO DRAW ALL OF YOUR ATTENTION TO THE FIFA EVENT GOING TO HAPPEN IN AMITY AMICHROMA SO I WOULD LIKE ALL OF YOU TO REGISTER FOR THE EVENT,YOU CAN USE THE ATTACHED POSTER FOR FUTURE DETAILS"
        # attach the body with the msg instance
        gmail_gui.attach(MIMEText(body, 'plain'))
        # open the file to be sent
        filename = "pp.jpg"
        attachment = open("E:\AMITIAN\pp.jpg", "rb")
        #   instance of MIMEBase and named as p
        connect = MIMEBase('application', 'octet-stream')
        # To change the payload into encoded form
        connect.set_payload((attachment).read())
        # encode into base64
        encoders.encode_base64(connect)
        connect.add_header('Content-Disposition', "attchment; filename= %s" % filename)
        # attach the instance 'p' to instance 'msg'
        gmail_gui.attach(connect)
        # Converts the Multipart msg into a string
        alpha= gmail_gui.as_string()
        shubh.sendmail("shubhdwivedimigmail.com",demon,alpha)
        print("the mail has been sent")
        shubh.quit()
