from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

# In-memory database for demonstration
tasks_db: List[Dict] = []
task_id_counter = 0

class Task(BaseModel):
    title: str
    description: str = None
    completed: bool = False

@app.post("/tasks/", status_code=201)
async def create_task(task: Task):
    global task_id_counter
    task_id_counter += 1
    new_task = task.dict()
    new_task["id"] = task_id_counter
    tasks_db.append(new_task)
    return new_task

@app.get("/tasks/", response_model=List[Task])
async def get_tasks():
    return tasks_db

@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    for task in tasks_db:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks_db):
        if task["id"] == task_id:
            tasks_db[i].update(updated_task.dict(exclude_unset=True))
            return tasks_db[i]
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", status_code=204)
async def delete_task(task_id: int):
    global tasks_db
    initial_len = len(tasks_db)
    tasks_db = [task for task in tasks_db if task["id"] != task_id]
    if len(tasks_db) == initial_len:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}
