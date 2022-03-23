from ninja import Router
from app.authorization import GlobalAuth, get_tokens_for_user
account_controller = Router(tags=['auth'])

