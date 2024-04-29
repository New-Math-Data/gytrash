import logging
import pytest
from gytrash import setup_logging
from gytrash.logging_mixin import LoggingMixin
from gytrash.formatters.slack import SlackFormatter

class TestSetupLogging:
    def test_setup_logging(self):
        # Create a root logger
        log = logging.getLogger()
        
        # Call the setup_logging function with different combinations of arguments
        setup_logging(log)
        assert log.level == 10
        assert len(log.handlers) == 5
        
        setup_logging(log, log_level=20, log_to_slack=True, slack_log_channel="test_channel", slack_bot_token="test_token")
        assert log.level == 20
        assert len(log.handlers) == 6
        
        setup_logging(log, log_level=30, log_to_teams=True, teams_url="test_url")
        assert log.level == 30
        assert len(log.handlers) == 7
        
        setup_logging(log, log_level=40, log_from_botocore=True)
        assert log.level == 40
        assert len(log.handlers) == 7

    # Add more test cases for other combinations of arguments

class TestLoggingMixin:
    def test_log_property(self):
        mixin = LoggingMixin()
        logger = mixin.log
        assert isinstance(logger, logging.Logger)
        assert logger.name == "gytrash.logging_mixin.LoggingMixin"

    def test_set_context(self):
        mixin = LoggingMixin()
        logger = logging.getLogger("gytrash.logging_mixin.LoggingMixin")
        mixin.set_context(logger, "test_context")
        for handler in logger.handlers:
            assert hasattr(handler, "set_context")
            assert handler.get_context() == "test_context"

class TestSlackFormatter:
    def test_format(self):
        formatter = SlackFormatter()
        record = logging.LogRecord(
            name="test_logger",
            level=logging.ERROR,
            pathname="/path/to/file.py",
            lineno=10,
            msg="Test error message",
            args=(),
            exc_info=None,
        )
        result = formatter.format(record)
        assert isinstance(result, dict)
        assert "ts" in result
        assert "icon_emoji" in result
        assert "blocks" in result

    # def test_create_log_block(self):
    #     formatter = SlackFormatter()
    #     record = logging.LogRecord(
    #         name="test_logger",
    #         level=logging.ERROR,
    #         pathname="/path/to/file.py",
    #         lineno=10,
    #         msg="Test error message",
    #         args=(),
    #         exc_info=None,
    #     )
    #     result = formatter._create_log_block(record)
    #     assert isinstance(result, list)
    #     assert len(result) == 3
    #     assert all(isinstance(item, dict) for item in result)

    def test_get_log_block(self):
        formatter = SlackFormatter()
        emoji = ":red_circle:"
        text = "Test error message"
        information = "2022-01-01 12:00:00-test_logger[123]-module-ERROR"
        result = formatter._get_log_block(emoji, text, information)
        assert isinstance(result, list)
        assert len(result) == 3
        assert all(isinstance(item, dict) for item in result)