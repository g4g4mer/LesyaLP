import time
from vkbottle.rule import FromMe
from vkbottle.user import Blueprint, Message
from .utils import edit_message, prefix


user = Blueprint(
	name = 'ping_blueprint'
)


async def get_ping(message: Message, answer: str) -> str:
	delta = round(time.time() - message.date, 2)
	
	return f'{answer} LesyaLP\n' \
				f'Ответ через {delta} с'
	

@user.on.message_handler(FromMe(), text=[prefix + 'пинг'])
async def ping(message: Message):
	await edit_message(message, await get_ping(message, 'ПОНГ'))