from vkbottle.rule import FromMe
from vkbottle.user import Message, Blueprint
from .utils import edit_message, adder, read, prefix
from vkbottle import TaskManager
import asyncio



user = Blueprint(
	name='autobonus_bp'
)

r = TaskManager()

async def bonus(message: Message, kd, bonus_text):
	get_bonus = await read('Settings', bonus_text)
	while get_bonus == True:
		get_bonus = await read('Settings', bonus_text)
		r_id = message.peer_id
		await user.api.messages.send(peer_id=r_id, message=f'{bonus_text}', random_id=0)
		await asyncio.sleep(kd)
		
@user.on.message_handler(FromMe(), text=[prefix + '+автобонус <bonus_text> <kd>'])
async def autobonus(message: Message, bonus_text, kd):
	await adder(js_name='Settings.json', method=bonus_text, value=True, intent=5)
	await edit_message(message, 'Автобонус успешно включён!')
	r.run_task(bonus(message, int(kd), bonus_text))
	
@user.on.message_handler(FromMe(), text=[prefix + '-автобонус <bonus_text>'])
async def autobonuses_off(message: Message, bonus_text):
	await adder(js_name='Settings.json', method=bonus_text, value=False, intent=5)
	await edit_message(message, 'Автобонус успешно отключён')
