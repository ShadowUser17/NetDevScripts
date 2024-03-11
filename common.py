import os
import logging


def get_logger() -> logging.Logger:
    log_level = logging.DEBUG if os.environ.get("DEBUG_MODE", "") else logging.INFO
    logging.basicConfig(
        format=r'%(levelname)s [%(asctime)s]: "%(message)s"',
        datefmt=r'%Y-%m-%d %H:%M:%S', level=log_level
    )
    return logging.getLogger()


class RouterOS:
    @classmethod
    def parse_as_value(self, output: str) -> dict:
        '''
        "key=val;..." -> ["key=val", ...] -> {key: val, ...}
        '''
        return dict(map(lambda item: item.split("="), output.split(";")))
