
from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field

app = FastAPI()
# this is not the best option ToDo = {}
# this is not a good option too In_Progress = {}
# same as this Done = {}
# Creating the Database
#Always use just one Master dictionary for your dictionary
Tasks = {} # To store the tasks details
allowed_columns = ['ToDo', 'In_Progress', 'Done'] # a list of fixed stages
Id = 0

#Creating the Data Model
class TaskCreate(BaseModel):
    title: str
    priorities: int=Field(le = 3)
    description: str | None = None


@app.post('/tasks')
async def create_task(task:TaskCreate):
    global Id
    Id = Id + 1
    details = task.model_dump()
    details.update({'id': Id,'column':'ToDo'})
    Tasks[Id]= details 
    return JSONResponse(status_code = 200, content={'message': 'Success', 'details': details})

@app.get('/tasks')
async def get_task(priority:int | None = None):
    filtered_task = []
    for task in Tasks.values():
        if task['priorities'] == priority:
            filtered_task.append(task)
        elif priority is None:
            filtered_task.append(Tasks)

    return (filtered_task)
    
@app.get('/tasks/{column_name}')
async def spec_task(column_name:str):
    if column_name not in allowed_columns:
        raise HTTPException(status_code=400, detail= 'Not in the list')
    # Collect tasks that belong to this column
    matching_tasks = []

    for task in Tasks.values():
        # We compare the string from the task to the string from the URL
        if task['column'] == column_name:
            matching_tasks.append(task)

    # Return the collection
    return {'status': 'success', 'data':matching_tasks}


class Column_Move(BaseModel):
    column_name:str

@app.patch('/tasks/{task_id}/move')
async def update_tasks(task_id:int, movement: Column_Move):
    # check if the task exists
    if task_id not in Tasks:
        raise HTTPException(status_code= 404, detail = 'Tasks not Found')
    
    # is the destination column valid?
    new_col = movement.column_name #Grab the string from pydantic model
    if new_col not in allowed_columns:
        raise HTTPException(status_code=400, detail = 'Invalid Column')
    
    # Move it!
    Tasks[task_id]['column'] = new_col
    return {'status': 'success', 'data': Tasks[task_id]}
    

@app.delete('/tasks/completed')
def del_task():
    # bring all IDs where columns are 'Done'
    ids_to_delete = []

    for task_id , task_data in Tasks.items():
        if task_data['column'] == 'Done':
            ids_to_delete.append(task_id)

    # delate those specific IDs from the master dictionary
    for task_id in ids_to_delete:
        del Tasks[task_id]

    return {'status': 'success', 'message':f"Deleted {len(ids_to_delete)} tasks"}