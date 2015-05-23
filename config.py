import sys
import logging

logger = logging.getLogger(__name__)


def configure_logging():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s  %(name)12s %(levelname)7s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)
