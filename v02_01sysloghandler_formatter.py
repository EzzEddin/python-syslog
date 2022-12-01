import logging
from logging.handlers import SysLogHandler


def main():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = SysLogHandler(
        facility=SysLogHandler.LOG_DAEMON,
        address='/dev/log'
        )

    formatter = logging.Formatter(
        fmt="%(asctime)s - %(filename)s:%(funcName)s:%(lineno)d %(levelname)s - '%(message)s'",
        datefmt="%Y-%m-%d %H:%M:%S"
        )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.debug('Sending a log message through SysLogHandler_v1!')

if __name__ == '__main__':
    main()
