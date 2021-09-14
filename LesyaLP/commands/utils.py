from vkbottle.user import Message
import json

with open('config.json', encoding='utf-8') as f:
	jj = json.load(f)
	prefix = jj["prefix"]

async def edit_message(
        message: Message,
        text: str = '',
        **kwargs
) -> int:
    """Простой редач сообщений
    Какие параметры пихать -- https://vk.com/dev/messages.edit
    :return: После успешного выполнения возвращает 1.
    """
    kwargs.setdefault('message_id', message.id)
    kwargs.setdefault('message', text)
    kwargs.setdefault('peer_id', message.peer_id)
    kwargs.setdefault('keep_forward_messages', True)
    kwargs.setdefault('keep_snippets', True)
    kwargs.setdefault('dont_parse_links', False)

    return await message.api.messages.edit(
        **kwargs
    )
    
async def adder(js_name, method: str, value, intent: int):
	with open(js_name, 'r', encoding='utf-8') as d:
		data = json.load(d)
	data[method] = value
	with open(js_name, 'w', encoding='utf-8') as d:
		d.write(json.dumps(data, indent=intent, ensure_ascii=False))



async def read(js_name, method):
	with open(js_name + '.json', 'r', encoding='utf-8') as g:
		xz = json.load(g)
		xz1 = xz[method]
	return xz1