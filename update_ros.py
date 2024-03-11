import os
import sys
import common
import logging

from config import config
from netmiko import ConnectHandler


try:
    log_level = logging.DEBUG if os.environ.get("DEBUG_MODE", "") else logging.INFO
    logging.basicConfig(
        format=r'%(levelname)s [%(asctime)s]: "%(message)s"',
        datefmt=r'%Y-%m-%d %H:%M:%S', level=log_level
    )

    with ConnectHandler(**config) as client:
        res = client.send_command(":put [/system/package/update/check-for-updates as-value]")
        logging.debug(res)

        data = common.RouterOS.parse_as_value(res)
        if data["installed-version"] != data["latest-version"]:
            res = client.send_command(":put [/system/package/update/install as-value]")
            logging.debug(res)

        else:
            logging.info("Status: {}".format(data["status"]))

except Exception:
    logging.exception(__name__)
    sys.exit(1)
