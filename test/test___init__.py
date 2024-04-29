import logging
import pytest
from gytrash import setup_logging
import logging
from gytrash import setup_logging

def test_setup_logging():
    # Create a root logger
    log = logging.getLogger()
    
    # Call the setup_logging function with different combinations of arguments
    setup_logging(log)
    assert log.level == 10
    assert len(log.handlers) == 1
    
    setup_logging(log, log_level=20, log_to_slack=True, slack_log_channel="test_channel", slack_bot_token="test_token")
    assert log.level == 20
    assert len(log.handlers) == 2
    
    setup_logging(log, log_level=30, log_to_teams=True, teams_url="test_url")
    assert log.level == 30
    assert len(log.handlers) == 3
    
    setup_logging(log, log_level=40, log_from_botocore=True)
    assert log.level == 40
    assert len(log.handlers) == 4

    # Add more test cases for other combinations of arguments

    # Add assertions to validate the behavior of the function

    # Add more test cases as neededimport logging

def test_setup_logging():
    # Create a root logger
    log = logging.getLogger()
    
    # Call the setup_logging function
    setup_logging(
        log,
        log_level=logging.DEBUG,
        log_from_botocore=True,
        log_to_slack=True,
        slack_log_channel="my_slack_channel",
        slack_log_level=logging.INFO,
        slack_bot_token="my_slack_bot_token",
        log_to_teams=True,
        teams_url="my_teams_url",
        teams_log_level=logging.INFO,
        teams_nonblocking=True,
        teams_card_formatter=True
    )
    
    # Assert that the log level is set correctly
    assert log.getEffectiveLevel() == logging.DEBUG
    
    # Assert that the Botocore logger is tapped
    # assert logging.getLogger("botocore").handlers
    
    # Assert that the SlackHandler is added and configured correctly
    # assert any(isinstance(handler, logging.handlers.SlackHandler) for handler in log.handlers)
    # assert log.handlers[0].channel == "my_slack_channel"
    # assert log.handlers[0].token == "my_slack_bot_token"
    # assert log.handlers[0].level == logging.INFO
    
    # # Assert that the TeamsHandler or TeamsQueueHandler is added and configured correctly
    # assert any(isinstance(handler, logging.handlers.TeamsHandler) or isinstance(handler, logging.handlers.TeamsQueueHandler) for handler in log.handlers)
    # assert log.handlers[1].url == "my_teams_url"
    # assert log.handlers[1].level == logging.INFO
    
    # Assert that the Office365CardFormatter is set if teams_card_formatter is True
    # if isinstance(log.handlers[1], logging.handlers.TeamsHandler):
    #     assert isinstance(log.handlers[1].formatter, logging.handlers.Office365CardFormatter)
    #     assert log.handlers[1].formatter.facts == ["name", "levelname", "lineno"]
