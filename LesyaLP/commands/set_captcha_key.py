from .utils import edit_message, adder, prefix
from vkbottle.rule import FromMe
from vkbottle.user import Blueprint, Message

user = Blueprint(name="set_captcha_key_bp")

@user.on.message_handler(FromMe(), text=[prefix + "+капча <captcha_key>"])
async def set_key(message: Message, captcha_key):
	await adder(js_name='config.json', method='captcha_key', value=captcha_key, intent=5)
	text = "Вы успешно изменили ключ рукапчи"
	await edit_message(message, text)