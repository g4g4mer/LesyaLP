from .utils import edit_message, adder, prefix
from vkbottle.user import Message, Blueprint
from vkbottle.rule import FromMe

user = Blueprint(
	name='prefix_bp'
)

@user.on.message_handler(FromMe(), text=[prefix + 'новый преф <new_prefix>'])
async def set_prefix(message: Message, new_prefix):
	await adder(js_name='config.json', method='prefix', value=new_prefix + ' ', intent=5)
	await edit_message(message, f'Префикс успешно изменён на {new_prefix}')