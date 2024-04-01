from fastapi import FastAPI
from routers import movie
from routers import user
from routers import login
from typing import Union

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(movie.router_movies)
app.include_router(user.router_users)
app.include_router(login.router_login)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=5000, reload=True, host="0.0.0.0")