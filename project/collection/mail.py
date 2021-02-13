# coding: utf8
import smtplib
import poplib
import imaplib,email
from email.mime.text import MIMEText
from email.header import Header
import getpass
import random,re
from bs4 import BeautifulSoup

class Emailmodule:
    # 此函数通过使用smtplib实现发送邮件
    def send_smtp(self):
        # 用于发送邮件的邮箱。修改成自己的邮箱
        sender_email_address = "your_email@qq.com"
        # 用于发送邮件的邮箱的密码。修改成自己的邮箱的密码
        sender_email_password = "your_email_password"
        # 用于发送邮件的邮箱的smtp服务器，也可以直接是IP地址
        # 修改成自己邮箱的sntp服务器地址；qq邮箱不需要修改此值
        smtp_server_host = "smtp.qq.com"
        # 修改成自己邮箱的sntp服务器监听的端口；qq邮箱不需要修改此值
        smtp_server_port = 465
        # 要发往的邮箱
        receiver_email = "your_dest_email@qq.com"
        # 要发送的邮件主题
        message_subject = "Python smtp测试邮件"
        # 要发送的邮件内容
        message_context = "这是一封通过Python smtp发送的测试邮件..."

        # 邮件对象，用于构建邮件
        # 如果要发送html，请将plain改为html
        message = MIMEText(message_context, 'plain', 'utf-8')
        # 设置发件人（声称的）
        message["From"] = Header(sender_email_address, "utf-8")
        # 设置收件人（声称的）
        message["To"] = Header(receiver_email, "utf-8")
        # 设置邮件主题
        message["Subject"] = Header(message_subject,"utf-8")

        # 连接smtp服务器。如果没有使用SSL，将SMTP_SSL()改成SMTP()即可其他都不需要做改动
        email_client = smtplib.SMTP_SSL(smtp_server_host, smtp_server_port)
        try:
            # 验证邮箱及密码是否正确
            email_client.login(sender_email_address, sender_email_password)
            print("smtp----login success, now will send an email to {receiver_email}")
        except:
            print("smtp----sorry, username or password not correct or another problem occur")
        else:
            # 发送邮件
            email_client.sendmail(sender_email_address, receiver_email, message.as_string())
            print(f"smtp----send email to {receiver_email} finish")
        finally:
            # 关闭连接
            email_client.close()

    # 此函数通过使用poplib实现接收邮件
    def receive_pop3(self):
        # 要进行邮件接收的邮箱。改成自己的邮箱
        email_address = "your_email@qq.com"
        # 要进行邮件接收的邮箱的密码。改成自己的邮箱的密码
        email_password = "your_email_password"
        # 邮箱对应的pop服务器，也可以直接是IP地址
        # 改成自己邮箱的pop服务器；qq邮箱不需要修改此值
        pop_server_host = "pop.qq.com"
        # 邮箱对应的pop服务器的监听端口。改成自己邮箱的pop服务器的端口；qq邮箱不需要修改此值
        pop_server_port = 995

        try:
            # 连接pop服务器。如果没有使用SSL，将POP3_SSL()改成POP3()即可其他都不需要做改动
            email_server = poplib.POP3_SSL(host=pop_server_host, port=pop_server_port, timeout=10)
            print("pop3----connect server success, now will check username")
        except:
            print("pop3----sorry the given email server address connect time out")
            exit(1)
        try:
            # 验证邮箱是否存在
            email_server.user(email_address)
            print("pop3----username exist, now will check password")
        except:
            print("pop3----sorry the given email address seem do not exist")
            exit(1)
        try:
            # 验证邮箱密码是否正确
            email_server.pass_(email_password)
            print("pop3----password correct,now will list email")
        except:
            print("pop3----sorry the given username seem do not correct")
            exit(1)

        # 邮箱中其收到的邮件的数量
        email_count = len(email_server.list()[1])
        # 通过retr(index)读取第index封邮件的内容；这里读取最后一封，也即最新收到的那一封邮件
        resp, lines, octets = email_server.retr(email_count)
        # lines是邮件内容，列表形式使用join拼成一个byte变量
        email_content = b'\r\n'.join(lines)
        # 再将邮件内容由byte转成str类型
        email_content = email_content.decode()
        print(email_content)

        # 关闭连接
        email_server.close()

    # 此函数通过使用imaplib实现接收邮件
    def receive_imap4(self,user,passwd,serveraddr,port):
        # 邮箱
        self.email_address = user
        # 密码
        self.email_password = passwd
        # imap服务器
        self.imap_server_host = serveraddr
        # 监听端口
        self.imap_server_port = port

        #连接服务器
        try:
            # SSL方式连接服务器
            email_server = imaplib.IMAP4_SSL(host=self.imap_server_host, port=self.imap_server_port)
            print('正在连接服务器...')
        except:
            print('服务器连接失败!')
            exit(1)
        try:
            # 验证
            email_server.login(self.email_address,self.email_password)
            print("系统正在登录中...")
        except:
            print('用户名密码错误！')
            exit(1)

        email_server.select()

        # 收件箱邮件数量
        email_count = len(email_server.search(None, 'ALL')[1][0].split())

        # 读取最新收到的那一封邮件
        typ, email_content = email_server.fetch(f'{email_count}'.encode(), '(RFC822)')

        # 下载邮件
        message = email.message_from_string(email_content[0][1].decode())

        # 获取邮件主题,解码
        try:
            subject = email.header.decode_header(message.get('Subject'))[0][0].decode('GB18030')
        except:
            try:
                subject = email.header.decode_header(message.get('Subject'))[0][0].decode()
            except:
                subject = email.header.decode_header(message.get('Subject'))[0][0]

        # 邮件解码
        for par in message.walk():
            annex = par.get_param('name')
            #contain annex!
            if annex:
                named = email.header.Header(annex)
                namedf = email.header.decode_header(named)
                annex_name = namedf[0][0]
                annex_name = str(annex_name).replace('?','1')[3:11] + str(random.randint(0,100)+random.randint(1,99))
                annex_db = par.get_payload(decode=True)
                print('annex_name=',type(annex_name),annex_name)
                try:
                    with open(annex_name+'.jpg','wb') as f:
                        f.write(annex_db)
                except:
                    with open(annex_name + str(random.randint(0,90)), 'wb') as f:
                        f.write(annex_db)

            #No have annex
            else:
                if not par.is_multipart():
                    try:
                        result = par.get_payload(decode=True).decode('utf-8')
                        result_8 = BeautifulSoup(result, 'html.parser')
                        result = result_8.get_text()
                        #print(message)
                        print('utf-8')
                    except:
                        result = par.get_payload(decode=True).decode('gbk')
                        result_8 = BeautifulSoup(result, 'html.parser')
                        result = result_8.get_text()
                        print('gbk')
        return result
        # 关闭服务
        # email_server.close()
        # 注销账户
        # email_server.logout()
