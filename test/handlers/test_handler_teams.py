import logging
import os
import json
import requests
from unittest.mock import patch
import pytest
from gytrash.handlers.teams import TeamsHandler

class TestTeamsHandler:
    @patch("requests.post")
    def test_emit(self, mock_post):
        handler = TeamsHandler(url="test_url", level=logging.INFO)
        record = logging.LogRecord(
            name="test_logger",
            level=logging.INFO,
            pathname="test_path",
            lineno=10,
            msg="test_message",
            args=None,
            exc_info=None,
        )
        handler.emit(record)
        mock_post.assert_called_once_with(
            url="test_url",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"text": "test_message"}),
        )

    @patch("os.environ", {"TEAMS_CHANNEL_URL": "test_url"})
    @patch("requests.post")
    def test_emit_with_env_variable(self, mock_post):
        handler = TeamsHandler(url=None, level=logging.INFO)
        record = logging.LogRecord(
            name="test_logger",
            level=logging.INFO,
            pathname="test_path",
            lineno=10,
            msg="test_message",
            args=None,
            exc_info=None,
        )
        handler.emit(record)
        mock_post.assert_called_once_with(
            url="test_url",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"text": "test_message"}),
        )

    def test_format_with_default_formatter(self):
        handler = TeamsHandler(url="test_url", level=logging.INFO)
        record = logging.LogRecord(
            name="test_logger",
            level=logging.INFO,
            pathname="test_path",
            lineno=10,
            msg="test_message",
            args=None,
            exc_info=None,
        )
        formatted = handler.format(record)
        assert formatted == json.dumps({"text": "test_message"})

    def test_format_with_custom_formatter(self):
        class CustomFormatter:
            def format(self, record):
                return f"Custom: {record.msg}"

        handler = TeamsHandler(url="test_url", level=logging.INFO)
        handler.formatter = CustomFormatter()
        record = logging.LogRecord(
            name="test_logger",
            level=logging.INFO,
            pathname="test_path",
            lineno=10,
            msg="test_message",
            args=None,
            exc_info=None,
        )
        formatted = handler.format(record)
        print(formatted)
        assert formatted == '{"text": "Custom: test_message"}'