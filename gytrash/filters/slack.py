import logging


class SlackLogFilter(logging.Filter):
    """
    Logging filter to decide when logging to Slack is requested, using
    the `extra` kwargs:
        `logger.info("...", extra={'notify_slack': True})`
    """

    def filter(self, record):
        return getattr(record, "notify_slack", False)

