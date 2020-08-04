"""Telegram module bot."""

from requests import Session

from .utils import TelegramEndpoints, TelegramMessageParseMode


class TelegramBot:
    """Telegram Bot Class."""

    def __init__(self, bot_token: str, proxies: dict = {}):
        """Initialize Telegram Bot."""
        self.bot_token = bot_token
        self._set_base_url()
        self._set_session(proxies=proxies)
        self._try_connection()

    def _set_base_url(self):
        """Generate base URL using bot token."""
        self.base_url = f'https://api.telegram.org/bot{self.bot_token}/'

    def _set_session(self, proxies: dict = {}):
        """Set requests session."""
        self.session = Session()
        self.session.proxies = proxies

    def _try_connection(self):
        """Try connection to Telegram."""
        req = self.session.get(self._get_endpoint(TelegramEndpoints.GET_ME))
        if req.status_code != 200:
            raise ConnectionError(req.json())

    def _get_endpoint(self, endpoint):
        return f'{self.base_url}{endpoint}'

    def send_message(
        self,
        message: str,
        chat_id: str,
        parse_mode: TelegramMessageParseMode = TelegramMessageParseMode.UNSET,
        disable_web_page_preview: bool = False,
        disable_notification: bool = False
    ):
        """Send a message from bot."""
        url = self._get_endpoint(TelegramEndpoints.SEND_MESSAGE)
        payload = {
            'text': message,
            'chat_id': chat_id,
            'parse_mode': parse_mode,
            'disable_web_page_preview': disable_web_page_preview,
            'disable_notification': disable_notification
        }
        return self.session.get(url=url, params=payload)
