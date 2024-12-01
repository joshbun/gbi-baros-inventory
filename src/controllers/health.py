from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/health")
async def health():
    return JSONResponse(
        content={"status": "ok"},
        status_code=200,
    )

@router.get("/ping")
async def ping():
    return JSONResponse(
        content={"status": "pong"},
        status_code=200,
    )

@router.get("/test")
async def test(params:int = 10):
    return JSONResponse(
        content={"status": "ok", "params" : params},
        status_code=200,
    )