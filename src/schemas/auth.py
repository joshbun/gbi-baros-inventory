from fastapi import HTTPException, status, Depends, Header
from ..config import API_KEY

def authenticate(api_key: str = Header(..., alias="X-API-KEY")):
    # Ambil kunci dari konfigurasi
    correct_api_key = API_KEY
    
    # Validasi API key
    if api_key != correct_api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )
