import sys
import common

from config import config
from netmiko import ConnectHandler


logger = common.get_logger()
try:
    with ConnectHandler(**config) as client:
        res = client.send_command(":put [/system/package/update/check-for-updates as-value]")
        logger.debug(res)

        data = common.RouterOS.parse_as_value(res)
        if data["installed-version"] != data["latest-version"]:
            res = client.send_command(":put [/system/package/update/install as-value]")
            logger.debug(res)

        else:
            logger.info("Status: {}".format(data["status"]))

except Exception:
    logger.exception(__name__)
    sys.exit(1)
