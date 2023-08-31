from anyio import sleep,create_task_group,run
from typing import Callable, Coroutine,Any

class AsyncTask:
    def __init__(self) -> None:
        pass


    async def create_async_task(self,func:Callable[[],Coroutine[Any,Any,None]]=None,**kwargs):
        print("start async task--------------------")
        async with create_task_group() as tg:
            tg.start_soon(func, kwargs)
            return 



