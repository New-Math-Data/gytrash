import logging


class LoggingMixin:
    """ Convenience super-class to have a logger configured with the class name
    """

    def __init__(self, context=None):
        self._set_context(context)

    @property
    def log(self) -> logging.Logger:
        """ A logger object.
        Returns:
            Logger
        """
        self._log = logging.getLogger(
            self.__class__.__module__ + "." + self.__class__.__name__
        )
        # self.log.setup_logging(log_level=10)
        return self._log

    def _set_context(self, context):
        if context is not None:
            self.set_context(self.log, context)

    @staticmethod
    def set_context(logger, value):
        """ Walks the tree of loggers and tries to set the context for each handler.
        
        Args:
            logger: logger to traverse
            value: value to set
        """
        _logger = logger
        while _logger:
            for handler in _logger.handlers:
                try:
                    handler.set_context(value)
                except AttributeError:
                    # Not all handlers need to have context passed in so we ignore
                    # the error when handlers do not have set_context defined.
                    pass
            if _logger.propagate is True:
                _logger = _logger.parent
            else:
                _logger = None

