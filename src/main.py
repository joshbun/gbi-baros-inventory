from fastapi import FastAPI, Depends
from .controllers import health, user

app = FastAPI()

@app.get("/", include_in_schema=False)
async def root():
    return {"message": "Welcome to FastAPI!"}

app.include_router(health.router, tags=["health"])
app.include_router(user.router, tags=["user"], prefix="/v1/users")
