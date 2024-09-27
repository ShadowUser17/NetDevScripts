import os
import config
import logging


def get_logger() -> logging.Logger:
    log_level = logging.DEBUG if os.environ.get("DEBUG_MODE", "") else logging.INFO
    logging.basicConfig(
        format=r'%(levelname)s [%(asctime)s]: "%(message)s"',
        datefmt=r'%Y-%m-%d %H:%M:%S', level=log_level
    )
    return logging.getLogger()


def get_config(hosts: str = "vm_hosts") -> list:
    return getattr(config, os.environ.get("HOSTS", hosts))


class RouterOS:
    @classmethod
    def parse_as_value(self, output: str) -> dict:
        '''
        "key=val;..." -> ["key=val", ...] -> {key: val, ...}
        '''
        return dict(map(lambda item: item.split("="), output.split(";")))

    @classmethod
    def parse_as_table(self, output: str) -> list:
        lines = filter(lambda item: not item.startswith("#"), output.splitlines())
        lines = filter(lambda item: not item.startswith("Columns"), lines)
        return list(map(lambda item: tuple(item.split()), lines))
