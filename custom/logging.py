import logging
import sys


class CustomFormatter(logging.Formatter):
    def __init__(self, *args, do_color=False, **kwargs):
        self.do_color = do_color

        super().__init__(*args, **kwargs)

    COLORS_BY_LEVEL = {
        logging.DEBUG: '34',  # Green
        logging.INFO: '26',  # Blue
        logging.WARNING: '220',  # Yellow
        logging.ERROR: '208',  # Orange
        logging.CRITICAL: '124',  # Red
    }

    def color_format(self, start_escape_code, end_escape_code):
        return f'%(asctime)s {start_escape_code}%(levelname)-8s{end_escape_code} %(module)s:%(lineno)s %(funcName)s :: %(message)s'

    def format(self, record: logging.LogRecord) -> str:
        start_escape_code = ''
        end_escape_code = ''

        if self.do_color:
            start_escape_code += (
                '\033[1;38;5;'
                + self.COLORS_BY_LEVEL[record.levelno]
                + 'm'
            )
            end_escape_code = '\033[m'

        formatter = logging.Formatter(
            self.color_format(
                start_escape_code,
                end_escape_code,
            ),
            datefmt='%H:%M:%S',
        )
        return formatter.format(record)


log = logging.getLogger()


# Prints to terminal
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(
    CustomFormatter(do_color=True),
)

log.addHandler(stream_handler)

# This log-level is bounded by whatever is set by the handler.
log.setLevel(logging.INFO)


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    log.critical(
        'Uncaught exception',
        exc_info=(exc_type, exc_value, exc_traceback),
    )


sys.excepthook = handle_exception
