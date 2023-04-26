#!/usr/bin/env python3

import os
import datetime
import reports
import emails

dttoday = datetime.datetime.today().strftime("%B %d, %Y")
dateTitle = "Processed Update on " + dttoday
path = "descriptions/"
names = []
weight = []
summary = ""
for txtfile in os.listdir(path):
    with open(os.path.join(path, txtfile)) as fopen:
        for count, line in enumerate(fopen.readlines()):
            if count == 0:
                summary += "name: " + line.strip() + "<br/>"
            elif count == 1:
                summary += "weight: " + line.strip() + "<br/><br/>"

if __name__ == "__main__":
    reports.generate_report("/tmp/processed.pdf", dateTitle, summary)

    sender = "automation@example.com"
    receiver = "student-01-af7207aee4c7@example.com".format(os.environ.get("USER"))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send_email(message)

