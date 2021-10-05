from vkbottle.user import User
from .commands import commands_bp
import json
from loguru import logger
import re
from .commands.utils import prefix
from .errors import error_bp

with open("config.json", "r", encoding="utf-8") as tok:
	data = json.load(tok)
	token = data["token"]

logger.catch()
loglevel = logger.level("[LesyaLP]", no=38, color="blue")

		
if len(token) < 85:
	logger.catch()
	loglvl = logger.level("[Tokens]", no=38, color="<green>")
	logger.log("[Tokens]", "\nДля начала работы, введите ваш токен: ")
	token = input("")
	while not (re.sub('[^A-Za-z0-9]', '', token)) == token and len(token) == 85:
		logger.log("[Tokens]", "\nВы ввели неправильный токен, укажите правильный: ")
		token = input("")
	
	data["token"] = token
	with open('config.json', 'w', encoding='utf-8') as token_:
		token_.write(json.dumps(data, indent=4))
		

user = User(data["token"], mobile=True)


text = f"""
                                        ⊶⋞Параметры запуска⋟⊷:
    ✦═══════════════════════════════⋞⋆━━━━━━━━━━━━━━━━━━━━━━⋆⋟═══════════════════════════════✦
            Ваш токен --->                  {data["token"]}
            Ваш префикс:                  {prefix}
    ✦═══════════════════════════════⋞⋆━━━━━━━━━━━━━━━━━━━━━━⋆⋟═══════════════════════════════✦
    """

logger.log("[LesyaLP]", text)
user.set_blueprints(*commands_bp, error_bp)
user.run_polling()
user.set_blueprints(*commands_bp)
user.run_polling()
