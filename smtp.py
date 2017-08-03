# -*-coding=utf-8-*-

#from email.mime.text import MIMEText
#msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
#
#from_addr = raw_input('From:')
#password = raw_input('Password:')
#smtp_server = raw_input('SMTP server:')
#to_addr = raw_input('To:')
#
#import smtplib
#server = smtplib.SMTP(smtp_server, 25)
#server.set_debuglevel(1)
#server.login(from_addr, password)
#server.sendmail(from_addr, [to_addr], msg.as_string())
#server.quit()

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr(( \
		Header(name, 'utf-8').encode(), \
		addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = raw_input('From:')
password = raw_input('Password:')
to_addr = raw_input('To:')
smtp_server = raw_input('SMTP server:')

msg = MIMEMultipart()#('alternative')
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['to'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候......', 'utf-8').encode()

msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
#msg.attach(MIMEText('<html><body><h1>send with file...</h1></body></html>', 'html', 'utf-8'))
with open('/home/hao/mygit/learnpy/11.jpg', 'rb') as f:
	mime = MIMEBase('image', 'png', filename='11.jpg')
	mime.add_header('Content-Disposition', 'attachmennt', filename='11.jpg')
	mime.add_header('Content-ID', '<0>')
	mime.add_header('X-Attachment-Id', '0')
	mime.set_payload(f.read())
	encoders.encode_base64(mime)
	msg.attach(mime)

with open('/home/hao/mygit/learnpy/22.jpg', 'rb') as f:
	mime1 = MIMEBase('image', 'png', filename='22.jpg')
	mime1.add_header('Content-Disposition', 'attachment', filename='22.jpg')
	mime1.add_header('Content-ID', '<0>')
	mime1.add_header('X-Attachment-Id', '0')
	mime1.set_payload(f.read())
	encoders.encode_base64(mime1)
	msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
		'<p><img src="cid:0"></p>' +
		'</body></html>', 'html', 'utf-8'))

#smtp_server = 'smtp.gmail.com'
smtp_port = 25#587
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
