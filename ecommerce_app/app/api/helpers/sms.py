from typing import Annotated, List
from twilio.rest import Client

from app.conf.settings import settings
from app.conf.mail import mail_conf

class SMS:
    def __init__(self, ):
        self._twilio_client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        
    async def send_sms(self, body:str, to:str):
        message = self._twilio_client.messages.create(
                        to=to,
                        from_=settings.TWILIO_PHONE_NUMBER,
                        body=body
                    )
        return message.sid
    