import gytrash
import logging

log = logging.getLogger("slack_example")

gytrash.setup_logging(log, log_level=10)

log.info("Test info message")
log.debug("Test debug message")
