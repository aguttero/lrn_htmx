from typing import Annotated
from fastapi import FastAPI, status, Form

# from pydantic import BaseModel

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from .html_content import dummy_page, make_ul, HTMX_KNOWLEDGE, goals_page

# Jinja Setup for session 18
from fastapi import Request
from fastapi.templating import Jinja2Templates


app = FastAPI()

# Jinja Setup for session 18
templates = Jinja2Templates(directory="templates")

# Jinja sample get response
@app.get("/poljinja", response_class =HTMLResponse)
async def pol_jinja(request: Request):
    my_list = ["Apple", "Banana", "Cherry"]
    my_empty_list = []

    # return templates.TemplateResponse(name = "pol.html",request= {"request": request, "items": my_list})
    return templates.TemplateResponse(name = "pol.html",request= request, context={"sample_list":my_list})


# HTML JS SETUP_
# Mount the static directory to the "/static" URL path
app.mount("/static", StaticFiles(directory="static"), name="static")
# app.mount("/public", StaticFiles(directory="public"), name="public")

@app.get("/healthy")
async def healty():
    return {"message": "Hello World! This is Panorámix"}

# Lesson 18 - Resources 07 + Jinja
@app.get("/goals", response_class=HTMLResponse)
async def goals(request: Request):
    return templates.TemplateResponse(name="goals.html", request=request)

# @app.get("/goals", response_class=HTMLResponse)
# async def goals():
#     return HTMLResponse(content=goals_page(), status_code=200)

goal_list = []
@app.post("/goalform", response_class=HTMLResponse)
async def capture_goal_item (goal: Annotated[str, Form()], request: Request):
    print (f"input_goal = {goal}")
    goal_list.append(goal)
    # goal_list.append(goal)
    print (f"goal_list = {goal_list}")
    print(f"--- NUEVA PETICIÓN ---")
    print(f"Método HTTP: {request.method}")     # GET, POST, etc.
    print(f"URL completa: {request.url}")       # http://127.0.0
    print(f"Path: {request.url.path}")  # /
    print(f"Client: {request.client}")
    print(f"IP del Cliente: {request.client.host}")
    # print(f"Auth: {request.auth}")
    print(f"Cookies: {request.cookies}")
    # return HTMLResponse(content=f"{goal_list}")
    return templates.TemplateResponse(name="goals.html",context={"goal_list":goal_list}, request=request)

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
