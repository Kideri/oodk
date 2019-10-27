from dialog_bot_sdk.bot import DialogBot
import grpc

token = '56b606b2217d28d75960fd0a41a75ac448882fd5'
endpoint = 'hackathon-mob.transmit.im'
bot = DialogBot.get_secure_bot(
    endpoint,
    grpc.ssl_channel_credentials(),
    token,
    verbose=True
)

DBHOST = 'localhost'
BDPORT = 27017
DBNAME = 'bot1'
