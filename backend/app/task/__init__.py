from .task_manager import TaskManager
from .ops_task import OpsTask

def get_task_manager()->TaskManager:

    return TaskManager


def get_ops_task()->OpsTask:

    return OpsTask