from vkbottle.rule import FromMe, PrivateMessage
from vkbottle.user import Blueprint, Message
from .utils import edit_message
import re

user = Blueprint(
	name='case_bp'
)

case = False

@user.on.message_handler(FromMe(), text='.лб +автокейсы <int> <int1>')
async def case_on(message: Message, int, int1):
	global case
	case = True
	await edit_message(message, 'Автооткрытие кейсов успешно включено')
	
@user.on.message_handler(FromMe(), text='.лб -автокейсы')
async def case_off(message: Message):
	global case
	case = False
	await edit_message(message, 'Автооткрытие кейсов успешно отключено')
	
@user.on.message_handler(PrivateMessage())
async def case_handler(message: Message):
	if case == True:
		a = re.search('Вам выпало', message.text)
		if a != None:
			await message(f'Кейс о {int} {int1}')