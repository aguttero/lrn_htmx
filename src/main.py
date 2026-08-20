from typing import Annotated
from fastapi import FastAPI, status, Form

# from pydantic import BaseModel
# from fastapi import Request

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from .html_content import dummy_page, make_ul, HTMX_KNOWLEDGE, goals_page

app = FastAPI()

# Mount the static directory to the "/static" URL path
app.mount("/static", StaticFiles(directory="static"), name="static")
# app.mount("/public", StaticFiles(directory="public"), name="public")

@app.get("/healthy")
async def healty():
    return {"message": "Hello World! This is Panorámix"}

# Lesson 18 - Resources 07
@app.get("/goals", response_class=HTMLResponse)
async def goals():
    return HTMLResponse(content=goals_page(), status_code=200)

goal_list = []
@app.get("/addgoalitem", response_class=HTMLResponse)
async def add_goal_item (goal: Annotated[str, Form()]):
    print (f"input_goal = {goal}")

# First lesson
@app.get("/dummy", response_class=HTMLResponse)
async def dummy():
    return HTMLResponse(content=dummy_page(), status_code=200)

@app.get("/info", response_class=HTMLResponse)
async def info():
    # return HTMLResponse(content="Placeholder for the /info request")
    return HTMLResponse(content=make_ul(HTMX_KNOWLEDGE))

@app.post("/formin", response_class=HTMLResponse)
async def post_note(note: Annotated[str, Form()]):
    print (f"notepost = {note}")
    print (f"type={type(note)}")

    new_list = [note]
    print(f"new_list={new_list}")
    output_list = new_list + HTMX_KNOWLEDGE
    # print (output_list)
    # return {"note_content": f"contenido={note}"}
    return HTMLResponse(content=make_ul(output_list))
