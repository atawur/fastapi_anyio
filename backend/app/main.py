from typing import Union
import uvicorn


from fastapi import FastAPI,Depends

from config.config import settings
from anyio import sleep,create_task_group,run
from task import TaskManager,OpsTask
import anyio

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# async def sometask(num):
#     print('Task', num, 'running')
#     await sleep(30)
#     print('Task', num, 'finished')

# def test(num,ext):
#     print(num,ext,"hi")

# async def anothertask(num):
#     #print('Task2', num, 'running')
#     #test(**num)
#     await sleep(3)
#     print('Task2', num, 'finished')

@app.get("/async_task")
async def create_async_task(task_manager:TaskManager= Depends(TaskManager)):
    await task_manager.start_task(OpsTask,task_name="my_task:001")
    

# @app.get("/anothertask")
# async def create_async_task(task_manager:TaskManager= Depends(TaskManager)):
#     await task_manager.start_task(TestTask,task_name="atik-task")
#     print('All tasks finished!f taks 1')

# async def async_task(task_group):
#     async with task_group as tg:
#         for i in range(5):
#             await tg.spawn(print_number, i)

# async def print_number(number):
#     await anyio.sleep(1)
#     print(f"Number: {number}")

# @app.get("/anyio")
# async def root():
#     async with anyio.create_task_group() as tg:
#         await tg.spawn(async_task, tg)
#     return {"message": "Tasks completed"}

if __name__ == "__main__":
    print("server is running")
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=settings.SERVICE_PORT)