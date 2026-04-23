# Script to Parse Logs: Read server or application logs, extract errors, and send an alert.

import re
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# Step 1: Parse logs to extract errors
def parse_logs(file_path):
    errors = []
    error_pattern = r"(ERROR|CRITICAL|EXCEPTION)"  # Regex to match error lines
    with open(file_path, 'r') as file:
        for line in file:
            if re.search(error_pattern, line):
                errors.append(line.strip())
    return errors