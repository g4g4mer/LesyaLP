#pylint:disable=E0401
from vkbottle.user import Blueprint, Message
from vkbottle.rule import PrivateMessage, FromMe
import re
from .utils import edit_message, prefix
from random import randint
from asyncio import sleep

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
		t = randint(18, 120)
		a = re.search('Ваши питомцы проиграли', message.text)
		b = re.search('Ваши питомцы победили!', message.text)
			
		if b != None:
			sleep(t)
			await user.api.messages.send(random_id=0, peer_id=message.peer_id, message='бой')
		if a != None:
			sleep(t)
			await user.api.messages.send(random_id=0, peer_id=message.peer_id, message='бой')
	elif war == False:
		pass
