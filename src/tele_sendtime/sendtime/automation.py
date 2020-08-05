"""TeleSendTime Module Automation."""


import string
import time

from ..telegram import TelegramBot
from ..telegram.utils import TelegramMessageParseMode

from .threads import AutomationThread


class Automation:
    """Automation Class."""

    def __init__(self, bot_token: str, proxies: dict = {}):
        """Initialize Automation Object."""
        self.bot = TelegramBot(bot_token=bot_token, proxies=proxies)
        self.jobs = []
        self._threads = []

    def add_job(
        self,
        function,
        chat_id: str,
        template: str = '',
        render_type: TelegramMessageParseMode = TelegramMessageParseMode.UNSET,
        disable_web_page_preview: bool = False,
        disable_notification: bool = False,
        interval: int = 300
    ):
        """Add a job to automation."""
        self.jobs.append({
            'template': template,
            'chat_id': chat_id,
            'render_type': render_type,
            'interval': interval,
            'disable_web_page_preview': disable_web_page_preview,
            'disable_notification': disable_notification,
            'function': function,
        })

    def job(
        self,
        chat_id: str,
        template: str = '',
        render_type: TelegramMessageParseMode = TelegramMessageParseMode.UNSET,
        disable_web_page_preview: bool = False,
        disable_notification: bool = False,
        interval: int = 300,
    ):
        """Run the checking function and send messages."""
        def _add_job(function):
            self.add_job(
                function=function,
                template=template,
                chat_id=chat_id,
                render_type=render_type,
                disable_notification=disable_notification,
                disable_web_page_preview=disable_web_page_preview,
                interval=interval
            )
        return _add_job

    def _initialize_threads(self):
        for job in self.jobs:
            self._threads.append(
                AutomationThread(target=self._run_thread, args=[job]))

    def _start_threads(self):
        for thread in self._threads:
            thread.start()

    def _stop_threads(self):
        for thread in self._threads:
            thread.join()

    def _send_messages(self, job, messages):
        for message in messages:
            self._send_message(job, message)

    def _send_message(self, job, message):
        if isinstance(message, dict):
            message_template = string.Template(job['template'])
            message = message_template.substitute(message)
        self.bot.send_message(
            message=message,
            chat_id=job['chat_id'],
            parse_mode=job['render_type'],
            disable_web_page_preview=job['disable_web_page_preview'],
            disable_notification=job['disable_notification'])

    def _are_threads_alive(self):
        return any([thread.is_alive() for thread in self._threads])

    def _run_thread(self, job):
        messages = job['function']()
        self._send_messages(job, messages)

    def run(self):
        """Run automation."""
        self._initialize_threads()
        self._start_threads()
        try:
            while self._are_threads_alive():
                time.sleep(30)
        except KeyboardInterrupt:
            self._stop_threads()
