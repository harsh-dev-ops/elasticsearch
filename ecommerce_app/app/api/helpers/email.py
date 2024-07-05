from typing import Annotated, List
from fastapi_mail import FastMail, MessageSchema, MessageType

from app.conf.mail import mail_conf
from ..schema import EmailSchema
    
class Email:
    def __init__(self, ):
        pass
    
    async def send_email(self, data: EmailSchema):
        try:
            message = MessageSchema(
                subject=data.subject,
                recipients=data.email,
                template_body=data.body,
                subtype=MessageType.html,
                )

            fm = FastMail(mail_conf)
            await fm.send_message(message, template_name="otp.html")
            
        except Exception as e:
            print(f"{e}")
    