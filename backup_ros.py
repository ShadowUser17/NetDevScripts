import common
import pathlib

from netmiko import file_transfer
from netmiko import ConnectHandler


logger = common.get_logger()
for host in common.get_config():
    try:
        with ConnectHandler(**host) as client:
            res = client.send_command("/system/backup/save dont-encrypt=yes")
            logger.debug(res)

            res = client.send_command(":put [/file/print where type=backup]")
            logger.debug(res)

            path = pathlib.Path("./backups")
            logger.debug("Create directory: {}".format(path))
            path.mkdir(exist_ok=True)

            for item in common.RouterOS.parse_as_table(res):
                src_path = pathlib.Path(item[1])
                dst_path = path.joinpath(src_path.name)

                if not dst_path.exists():
                    logger.info("Get {} -> {}".format(src_path, dst_path))
                    file_transfer(
                        client, source_file=src_path.name, dest_file=str(dst_path),
                        file_system=src_path.parent.name, direction="get"
                    )

    except Exception:
        logger.exception(__name__)
