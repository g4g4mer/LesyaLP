from . import captcha, authorization_failed

error_bp = (
	captcha.user,
	authorization_failed.user
)