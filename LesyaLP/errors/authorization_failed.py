from vkbottle.user import Blueprint
from vkbottle import VKError
from ..commands.utils import adder

user = Blueprint(name="authorization_bp")

@user.error_handler.error_handler(5)
async def token_handler(error: VKError):
	token = ""
	await adder(js_name='config.json', method='token', value=token, intent=5)
	quit()