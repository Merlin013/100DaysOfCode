import smtplib

# creating an SMTP object to connect to the email providers SMTP servers
my_email = "youremail@gmail.com"
password = "123456abcde()"
with smtplib.SMTP("smtp-mail.outlook.com") as connection:

    # .starttls() method once enabled will encrypt our connection
    connection.starttls()

    # .login() method is to provide the user name and password to login
    connection.login(user=my_email, password=password)
    # to include a subject line, add the word subject in the msg= parameter. To add the body of the email add 2 \n's
    connection.sendmail(from_addr=my_email,
                        to_addrs="newaddress@gmail.com",
                        msg="Subject:Hello There\n\nThis is the body of the email.")
