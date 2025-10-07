from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Modelo de tarefa
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

# Lista de tarefas em memória
fake_db: List[Task] = []

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return fake_db

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    fake_db.append(task)
    return task

# Implemente os endpoints de atualização e remoção conforme solicitado no README
