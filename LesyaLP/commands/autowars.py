#pylint:disable=E0401
from vkbottle.user import Blueprint, Message
from vkbottle.rule import PrivateMessage, FromMe
import re
from .utils import edit_message, prefix

war = False

user = Blueprint(
	name='wars_bp'
)

@user.on.message_handler(FromMe(), text=[prefix + '+бой', prefix + '+бои'])
async def war_True(message: Message, **kwargs):
	global war
	war = True
	await edit_message(message, 'Автобои включены')

@user.on.message_handler(FromMe(), text=[prefix + '-бой', prefix + '-бои'])
async def war_False(message: Message, **kwargs):
	global war
	war = False
	
	await edit_message(message, 'Автобои отключены')


@user.on.message_handler(PrivateMessage())
async def handler(message: Message):
	if war == True:
		a = re.search('Ваши питомцы проиграли', message.text)
		b = re.search('Ваши питомцы победили!', message.text)
			
		if b != None:
			await message('бой')
		if a != None:
			await message('бой')
	elif war == False:
		pass