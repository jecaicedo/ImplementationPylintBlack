"""
auth.py

This module defines the key the API.
"""

from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader
from database import API_KEY

api_key_header = APIKeyHeader(name="X-API-KEY")


async def get_api_key(api_key: str = Security(api_key_header)):
    """method for get api key"""
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Could not validate API Key")
