import os
from datetime import datetime
from pprint import pprint
from time import sleep

import routeros_api

ROUTER_IP = os.environ["ROUTER_IP"]
USER = os.environ["MIKROTIK_USER"]
PASS = os.environ["MIKROTIK_PASSWORD"]
BACKUP_FILE = "backupify-" + datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".rsc"

connection = routeros_api.RouterOsApiPool(
    ROUTER_IP, username=USER, password=PASS, plaintext_login=True
)
api = connection.get_api()

# print status info
pprint(api.get_resource("/system/routerboard").get())

# print backup
pprint(api.get_resource("/").call("export", {"file": "backupify.rsc"}))

# get the human readable backup
file = api.get_resource("/file").call(
    "read", {"file": "backupify.rsc", "chunk-size": "32768"}
)

with open(f"output/{BACKUP_FILE}", "w") as f:
    f.write(file[0]["data"])

# create binary backup
# this cannot be downloaded without enabling ftp
# so its just a backup to be kept
# this overwrites the previous backup, which isn't ideal
pprint(api.get_resource("/system/backup").call("save", {"name": "backupify.backup"}))

