from nornir import InitNornir
from dotenv import load_dotenv
from pprint import pprint


load_dotenv()

nr = InitNornir(
    config_file="config/netbox_config.yaml",
)
# in order to really understand a nornir inventory item, you should play around with it. A LOT.
pprint(nr.inventory.hosts)
pprint(nr.inventory.hosts)
print(dir(nr.inventory.hosts["router10"]))
pprint(nr.inventory.hosts["router10"].data)

