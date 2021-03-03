import smtplib   #LIBRARY FOR SENDING THE MAIL OVER THE INTERNET FOR A VALID EMAIL ADDRESS
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
list = ["RECIVERS MAIL ID , , , ...."]
for demon in list:
        shubh = smtplib.SMTP('smtp.gmail.com', 587)
        shubh.starttls()
        shubh.login("SENDERS_EMAIL", "SENDER_PASSWORD")
        gmail_gui = MIMEMultipart()
        gmail_gui['From'] = "NAME OF SENDING PARTY"
        # storing the receivers email address and will help you to show the receivers mail in TO of the gui part
        gmail_gui['To'] =  demon   
        gmail_gui['Subject'] = "MAIL SUBJECT"
        body = "BODY FOR THE MAIL"
        # attach the body with the msg instance
        gmail_gui.attach(MIMEText(body, 'plain'))
        # open the file to be sent
        filename = "NAME OF ATTCHMENT FILE WITH EXTENSION"
        attachment = open("PATH FOR THE FILE", "rb")
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
        shubh.sendmail("SENDERS MAIL",demon,alpha)
        print("the mail has been sent")
        shubh.quit()
