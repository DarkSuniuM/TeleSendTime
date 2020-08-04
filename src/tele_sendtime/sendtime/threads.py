"""SendTime Module Threading."""

from threading import Event, Thread


class AutomationThread(Thread):
    """Automation Thread Class."""

    def __init__(self, target, args):
        """Initialize Authomation Thread."""
        self._stop_event = Event()
        self._sleep_period = args[0]['interval']
        Thread.__init__(self, target=target, args=args)

    def run(self):
        """Run thread."""
        while not self._stop_event.isSet():
            self._target(*self._args)
            self._stop_event.wait(self._sleep_period)

    def join(self, timeout=None):
        """Stop the thread and wait for it to end."""
        self._stop_event.set()
        Thread.join(self, timeout)
