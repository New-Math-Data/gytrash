.. _Examples:


******************
Examples
******************

Simple logging setup
====================

   examples/simple.py
 
.. literalinclude:: ../examples/simple.py


Slack logging setup
====================
To use gytrash to ship logging messages to slack, first setup a slack app using this `walkthrough <https://github.com/slackapi/python-slack-sdk/blob/main/tutorial/01-creating-the-slack-app.md>`_

Once you have generated the bot token, save it as an environment variable.
Set Slack Environment Variables
-------------------------------

``export SLACK_BOT_TOKEN="<BOT TOKEN>"``

   examples/slack.py
 
Finally setup gytrash using the extended parameters.

.. literalinclude:: ../examples/slack.py