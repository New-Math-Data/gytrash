import logging
import pytest
from gytrash import setup_logging
from gytrash.formatters.teams import Office365CardFormatter

def test_setup_logging():
    # Create a root logger
    log = logging.getLogger()
    
    # Call the setup_logging function with different combinations of arguments
    setup_logging(log)
    assert log.level == 10
    assert len(log.handlers) == 7
    
    setup_logging(log, log_level=20, log_to_slack=True, slack_log_channel="test_channel", slack_bot_token="test_token")
    assert log.level == 20
    assert len(log.handlers) == 8
    
    setup_logging(log, log_level=30, log_to_teams=True, teams_url="test_url")
    assert log.level == 30
    assert len(log.handlers) == 9
    
    setup_logging(log, log_level=40, log_from_botocore=True)
    assert log.level == 40
    assert len(log.handlers) == 9

# def test_office365_card_formatter():
#     # Create a log record
#     record = logging.LogRecord(
#         name="test_logger",
#         level=logging.INFO,
#         pathname="/path/to/file.py",
#         lineno=10,
#         msg="Test message",
#         args=(),
#         exc_info=None
#     )
    
#     # Create an instance of Office365CardFormatter
#     formatter = Office365CardFormatter(facts=["name", "levelname", "lineno"])
    
#     # Format the log record
#     formatted_message = formatter.format(record)
    
#     # Assert the formatted message
#     assert formatted_message == (
#         '{"@context": "https://schema.org/extensions", '
#         '"@type": "MessageCard", '
#         '"title": "Info in test_logger", '
#         '"summary": "Test message", '
#         '"sections": [{"facts": [{"name": "name", "value": "test_logger"}, '
#         '{"name": "levelname", "value": "INFO"}, '
#         '{"name": "lineno", "value": 10}]}], '
#         '"themeColor": "#008000", '
#         '"text": "Test message"}'
#     )