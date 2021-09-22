from _typeshed import Self
import logging

class Log_model:
    logging.basicConfig(filename="v.log", level=logging.debug, format=f'[%(asctime)s] - [%(filename)s]: %(message)s')

    def l_info(message):
        pass

    def l_debug(message):
        logging.debug(message)
        pass

    def l_warning(message):
        pass
    
    def l_critical(message):
        pass

    def l_error(message):
        pass