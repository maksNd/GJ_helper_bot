import logging


def get_and_set_logger():
    logger = logging.getLogger('basic')
    logger.setLevel(logging.DEBUG)

    formatter_1 = logging.Formatter("%(asctime)s : %(message)s", "%d.%m.%y %H:%M")

    file_handler = logging.FileHandler('log.log', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter_1)

    logger.addHandler(file_handler)

def new_log(logger, user, user_input):
    logger.info(f'{user} - get reply for {user_input}')
