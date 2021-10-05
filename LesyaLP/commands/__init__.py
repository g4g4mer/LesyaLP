from . import autobonus, ping, autowars, prefixes, set_captcha_key

commands_bp = (
	ping.user,
	autobonus.user,
	set_captcha_key.user,
	autowars.user,
	prefixes.user
)