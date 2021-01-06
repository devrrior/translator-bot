import logging

logger = logging

logger.basicConfig(level=logging.DEBUG,
                   format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                   datefmt='%I:%M:%S',
                   handlers=[
                       logging.StreamHandler()
                   ])