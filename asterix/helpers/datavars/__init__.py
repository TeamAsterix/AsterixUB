from .botconfig import BOTDV, BotConfig
from .otherconfig import OTHERDV, OtherConfig
from .userconfig import USERDV, UserConfig


class DataVars(BotConfig, OtherConfig, UserConfig):
    DVLIST = BOTDV + OTHERDV + USERDV
