from logging import (
    StreamHandler,
    CRITICAL,
    ERROR,
    WARNING,
    INFO,
    FATAL,
    DEBUG,
    NOTSET,
    Formatter,
)

import logging
import os
import traceback

from slack_sdk.web import WebClient

ERROR_COLOR = "danger"  # color name is built in to Slack API
WARNING_COLOR = "warning"  # color name is built in to Slack API
INFO_COLOR = "#439FE0"

COLORS = {
    CRITICAL: ERROR_COLOR,
    FATAL: ERROR_COLOR,
    ERROR: ERROR_COLOR,
    WARNING: WARNING_COLOR,
    INFO: INFO_COLOR,
    DEBUG: INFO_COLOR,
    NOTSET: INFO_COLOR,
}


class SlackHandler(StreamHandler):
    def __init__(
        self, channel: str, slack_bot_token: str = None, username: str = "Gytrash"
    ):
        StreamHandler.__init__(self)
        # Initialize a Web API client
        if slack_bot_token:
            self.slack_web_client = WebClient(token=slack_bot_token)
        else:
            self.slack_web_client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
        self.channel = channel
        self.username = username

    def build_trace(self, record, fallback):
        trace = {"fallback": fallback, "color": COLORS.get(self.level, INFO_COLOR)}

        if record.exc_info:
            trace["text"] = "\n".join(traceback.format_exception(*record.exc_info))

        return trace

    def _send_log(self, message: str):
        self.slack_web_client.chat_postMessage(**message)

    def emit(self, message: str):
        assert isinstance(message, logging.LogRecord)

        slack_message = self.format(message)

        # List of LogRecord attributes expected when reading the
        # documentation of the logging module:
        expected_attributes = (
            "args,asctime,created,exc_info,filename,funcName,levelname,"
            "levelno,lineno,module,msecs,message,msg,name,pathname,"
            "process,processName,relativeCreated,stack_info,thread,threadName"
        )
        for ea in expected_attributes.split(","):
            if not hasattr(message, ea):
                print("UNEXPECTED: LogRecord does not have the '{}' field!".format(ea))

        slack_message["channel"] = self.channel
        slack_message["username"] = self.username

        self._send_log(slack_message)
