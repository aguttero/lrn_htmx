from fastapi import FastAPI

# from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from .html_content import dummy_page, make_ul, HTMX_KNOWLEDGE

app = FastAPI()

# Mount the static directory to the "/static" URL path
app.mount("/static", StaticFiles(directory="static"), name="static")
# app.mount("/public", StaticFiles(directory="public"), name="public")

@app.get("/healthy")
async def healty():
    return {"message": "Hello World! This is Panorámix"}


@app.get("/dummy", response_class=HTMLResponse)
async def dummy():
    return HTMLResponse(content=dummy_page(), status_code=200)

@app.get("/info", response_class=HTMLResponse)
async def info():
    # return HTMLResponse(content="Placeholder for the /info request")
    return HTMLResponse(content=make_ul(HTMX_KNOWLEDGE))
