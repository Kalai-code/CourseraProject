#!/usr/bin/env python3
import shutil
import psutil
import emails
import socket


def triggeremail(subjectline):
    sender = "automation@example.com"
    receiver = "student-01-af7207aee4c7@example.com"
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_email(sender, receiver, subjectline, body, "")
    emails.send_email(message)


# Check CPU usage and trigger email if the usage is more than 80%
cpu_percent = psutil.cpu_percent(1)
if cpu_percent > 80:
    subject = "Error - CPU usage is over 80%"
    triggeremail(subject)

#Available disk space is lower than 20%
diskusage = psutil.disk_usage("/")
du_percent = diskusage.free / diskusage.total * 100
if du_percent < 20:
    subject = "Error - Available disk space is less than 20%"
    triggeremail(subject)


#available memory is less than 500MB
mem = psutil.virtual_memory()
compValue = 500 * 1024 * 1024 #500 MB
if mem.available < compValue:
    subject = "Error - Available memory is less than 500MB"
    triggeremail(subject)


#hostname "localhost" cannot be resolved to "127.0.0.1"
hostname = socket.gethostname("localhost")
if hostname != "127.0.0.1":
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    triggeremail(subject)