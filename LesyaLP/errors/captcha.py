from python_rucaptcha import ImageCaptcha
from vkbottle.exceptions import VKError
from vkbottle.framework.blueprint.user import Blueprint
from ..commands.utils import captcha_key


user = Blueprint(name="captcha_bp")

@user.error_handler.captcha_handler
async def captcha(error: VKError):
	if captcha_key == "":
		return
	
	answer = ImageCaptcha.ImageCaptcha(rucaptcha_key=captcha_key).captcha_handler(captcha_link=error.raw_error['captcha_img'])
	
	if not answer['error']:
		return answer['captchaSolve']