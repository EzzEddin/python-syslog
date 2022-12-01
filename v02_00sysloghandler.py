import logging
from logging.handlers import SysLogHandler


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = SysLogHandler(
    facility=SysLogHandler.LOG_DAEMON,
    address='/dev/log'
    )
logger.addHandler(handler)
logger.debug('Sending a log message through SysLogHandler!')
