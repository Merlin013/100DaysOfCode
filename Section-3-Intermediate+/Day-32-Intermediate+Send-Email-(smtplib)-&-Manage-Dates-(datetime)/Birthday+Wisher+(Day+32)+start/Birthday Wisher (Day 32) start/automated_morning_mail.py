import smtplib
import datetime as dt
import random

MY_EMAIL = "youremail@gmail.com"
MY_PASSWORD = "123456abcde()"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0: # 0 indicates its checking for monday
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIl, msg=f"Subject:Monday Motivation\n\n{quote}")





# import smtplib
#
# # creating an SMTP object to connect to the email providers SMTP servers
# my_email = "youremail@gmail.com"
# password = "123456abcde()"
# with smtplib.SMTP("smtp-mail.outlook.com") as connection:
#
#     # .starttls() method once enabled will encrypt our connection
#     connection.starttls()
#
#     # .login() method is to provide the user name and password to login
#     connection.login(user=my_email, password=password)
#     # to include a subject line, add the word subject in the msg= parameter. To add the body of the email add 2 \n's
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="newaddress@gmail.com",
#                         msg="Subject:Hello There\n\nThis is the body of the email.")

# import datetime as dt
#
# # the now() method gets the current date and time
# now = dt.datetime.now()
# print(now)