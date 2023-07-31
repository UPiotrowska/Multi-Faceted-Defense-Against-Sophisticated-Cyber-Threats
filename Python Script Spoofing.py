import smtplib
from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from_addr = 'pthompson@thebootcampspot.com'
to_addr = 'tatianapavlovichovna@gmail.com'

msg = MIMEMultipart()
msg['From'] = formataddr(('Paige Thompson', 'pthompson@thebootcampspot.com'))
msg['Reply-To'] = 'pthompson@thebootcampspot.com'
msg['To'] = to_addr
msg['Subject'] = 'CompTIA+ voucher'

# Using HTML formatting for the email body to set the text color to black
body = '''
<html>
<body style="color: black;">
<p>👋 Hello,</p>

<p>We are roughly two weeks out from the bootcamp's completion.</p>

<p>Please take a look at the data I have below on your student status. If anything is incorrect, please let me know ASAP so that I can make adjustments or have the conversation to find a solution. You will find updates below:</p>

<p><strong>📚 Student Status:</strong></p>
<p>Homework Requirement Met? ✅ On track!</p>
<p>Project Requirement Met? ❌ On track!</p>
<p>Attendance Requirement Met? ✅ On track!</p>

<p><strong>🎓 In order to graduate with a certificate you must:</strong></p>
<ul>
<li>Not exceed 4 absences</li>
<li>Not exceed 2 missing/incomplete/zero-pointed assignments</li>
<li>Complete ALL projects</li>
<li>Be up-to-date on your financial obligation</li>
</ul>

<p><strong>⚠️ ⬆️ All of the above requirements must be met by the last day of class. ⬆️ ⚠️</strong></p>

<p>In order to redeem your CompTIA+ voucher, you must successfully complete the bootcamp, and meet requirements mentioned above. To access your voucher, please visit the bootcamp link provided and follow the given instructions:</p>
<p><a href="http://thebootcampspot.com/">http://thebootcampspot.com/</a></p>

<p>If you have any questions/concerns about your class stats, please email me ASAP or schedule a meeting on my Calendly. I am happy to meet with you to figure out a plan to help get you caught up. I will see you in class at some point in the next week. See you soon!</p>

<p>Best,<br>
Paige Thompson SSM</p>
</body>
</html>
'''

msg.attach(MIMEText(body, 'html'))

smtp_server = smtplib.SMTP('smtp-relay.brevo.com', 587)
smtp_server.ehlo()
smtp_server.starttls()
smtp_server.login('', '') 
smtp_server.sendmail(from_addr, to_addr, msg.as_string())
smtp_server.quit()
