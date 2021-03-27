import smtplib


def send_email(subject, body):
    gmail_user = 'an unprotected email address'
    gmail_password = 'The password'

    sent_from = gmail_user
    to = 'your sms number here'
    text_subject = subject
    #print(text_subject)
    text_body = subject + body
    #print(text_body)

    email_text = ("From: %s\r\n" % sent_from
                  + "To: %s\r\n" % to
                  + "Subject: %s\r\n" % subject
                  + "\r\n"
                  + body)

    print(email_text)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')
