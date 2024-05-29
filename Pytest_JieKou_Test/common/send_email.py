from email import encoders
from email.header import Header                   #Header()定义邮件标题
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart    #MIMEMulipart模块构造带附件
from email.mime.text import MIMEText              #MIMRText()定义邮件正文
from Config.config_init import read_config
import smtplib

# 邮件服务器基础设置
def send_email():
        # 1、读取配置文件里的相关邮箱信息
        smtpserver = read_config("email", "smtpserver")
        # 设置登录邮箱的账号和授权密码,以qq邮箱为例
        user = read_config("email", "user")
        # 此处是授权码，不是邮箱密码
        password = read_config("email", "password")
        sender = read_config("email", "sender")
        # 可添加多个收件人的邮箱
        receives = [read_config("email", "receives")]

        # user_manage构造邮件对象
        msg = MIMEMultipart('mixed')
        # # 定义邮件的标题
        subject = read_config("email", "subject")
        # HTML邮件正文，定义成字典
        msg['Subject'] = Header(subject, "utf-8")
        #发件人
        msg['From'] = sender
        # 收件人
        msg['To'] = ','.join(receives)
        # 构造文字内容
        text_plain = MIMEText("最新的接口自动化测试报告，请查收！", 'html', 'utf-8')
        msg.attach(text_plain)

        # 3、邮箱设置时勾选了SSL加密连接，进行防垃圾邮件，SSL协议端口号要使用465
        smtp = smtplib.SMTP_SSL(smtpserver, 465)
        # 向服务器标识用户身份
        smtp.helo(smtpserver)
        # 向服务器返回确认结果
        smtp.ehlo(smtpserver)
        # 登录邮箱的账号和授权密码
        smtp.login(user, password)

        # 4、开始进行邮件的发送，msg表示已定义的字典
        print("开始发送邮件...")
        smtp.sendmail(sender, receives, msg.as_string())
        # 5、停止发送，发送完成
        smtp.quit()
        print("发送邮件完成!")