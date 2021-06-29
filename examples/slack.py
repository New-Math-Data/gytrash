import gytrash
import logging

log = logging.getLogger("slack_example")

gytrash.setup_logging(
    log,
    log_level=10,
    log_from_botocore=False,
    log_to_slack=True,
    slack_log_channel="<LOG NAME>",
    slack_log_level=20,
    slack_bot_token="<TOKEN>",
)

log.info("Test info message")
log.debug("Test debug message")

log.info(
    "Test info message", extra={"notify_slack": True}
)  # send this log message to slack

