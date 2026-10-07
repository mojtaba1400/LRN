from fastapi import FastAPI , Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import engine, Base, SessionLocal
from models import Todo
from database import get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()

class TodoCreate(BaseModel):
    title: str
    description: str | None = None
    priority: int

@app.post("/todos")
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db)
):

    new_todo = Todo(
        title=todo.title,
        description=todo.description,
        priority=todo.priority
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo

@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return todos

@app.get("/todos/{todo_id}")
def get_todo(
    todo_id: int,
    db: Session = Depends(get_db)
):

    todo = db.query(Todo).filter(
        Todo.id == todo_id
    ).first()

    return todo

@app.delete("/todos/{todo_id}")
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db)
):

    todo = db.query(Todo).filter(
        Todo.id == todo_id
    ).first()

    if not todo:
        return {"message": "Todo not found"}

    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted"}