from fastapi import APIRouter
from models.todos import Todo
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()


# GET request method
@router.get("/")
def get_todos():
    todos = collection_name.find()
    return list_serial(todos)


# POST request method
@router.post("/")
async def post_todos(todo: Todo):
    collection_name.insert_one(dict(todo))
    return {
        **todo.dict()
    }


# PUT request method
@router.put("/{id}")
async def put_todos(id: str, todo: Todo):
    collection_name.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(todo)})
    return {
        **todo.dict(),
        "id": id
    }
