# app/api/v1/auth.py
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Set

from app.crud import users as crud_users
from app.schemas.auth import Token
from app.db.session import get_db
from app.core import security, config

router = APIRouter()

# In-memory token blacklist (use Redis/DB for production)
blacklisted_tokens: Set[str] = set()


@router.post("/login", response_model=Token, summary="User login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
):
    """
    Authenticate user and return a JWT access token.
    """
    user = await crud_users.authenticate(db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = security.create_access_token(
        subject=user.email,
        expires_delta=timedelta(minutes=config.settings.ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/logout", summary="User logout (JWT invalidation)")
async def logout(token: str = Depends(security.oauth2_scheme)):
    """
    Logout the current user by blacklisting the JWT token.
    """
    blacklisted_tokens.add(token)
    return {"msg": "Successfully logged out"}


# Dependency to verify token for protected routes
async def verify_token(token: str = Depends(security.oauth2_scheme)):
    if token in blacklisted_tokens:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has been revoked")
    return token
