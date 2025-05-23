from nornir import InitNornir


from dotenv import load_dotenv

from nornir_utils.plugins.functions import print_result
from nornir.core.task import Task, Result
from nornir_napalm.plugins.tasks import napalm_get
from pprint import pprint


load_dotenv()


nr = InitNornir(
    config_file="config/netbox_config.yaml",
)

print(nr.inventory.hosts)


def gather_device_facts(task: Task):
    task.run(
        name="Gather Basic Facts",
        task=napalm_get,
        getters=["get_facts", "get_interfaces_ip"],
    )
    return Result(host=task.host, result=f"Facts gathered from {task.host}")


def gather_netbox_facts(task: Task):
    pprint(task.host.data)


def multiple_tasks(task: Task):
    task.run(gather_device_facts)
    task.run(gather_netbox_facts)


test_results = nr.run(name="running multiple tasks", task=multiple_tasks)

print(test_results)
print_result(test_results)
