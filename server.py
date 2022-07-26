import time

from fastapi import FastAPI, Request, Query, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from data.states import STATES


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def base_page(request: Request) -> Response:
    return templates.TemplateResponse(
        "base.html",
        {
            "request": request,
        },
    )


@app.get("/demo", response_class=HTMLResponse)
def demo_page(request: Request) -> Response:
    return templates.TemplateResponse(
        "demo.html",
        {
            "request": request,
        },
    )


@app.get("/state-list-results", response_class=HTMLResponse)
def state_list_results(
    request: Request,
    search: str = Query(""),
    search_type: str = Query("Contain", alias="search-type"),
) -> Response:
    states = STATES

    if search:
        if search_type == "Contain":
            states = [state for state in states if search.upper() in state.upper()]

        elif search_type == "Start":
            states = [state for state in states if state.upper().startswith(search.upper())]

        elif search_type == "End":
            states = [state for state in states if state.upper().endswith(search.upper())]

    return templates.TemplateResponse(
        "state-list-results.html",
        {
            "request": request,
            "states": states,
        },
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
