from .on_callback import OnCallbackQuery
from .on_inline import OnInlineQuery
from .on_message import OnMessage


class Decorators(
    OnMessage,
    OnInlineQuery,
    OnCallbackQuery,
):
    pass
