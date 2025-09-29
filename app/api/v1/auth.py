from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


from app import models, crud, schemas
from app.schemas import auth as auth_schemas

from app.db.session import get_db

from app.core import security, config

router = APIRouter()

@router.post("/login", response_model=schemas.auth.Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = crud.users.get_by_username(db, username=form_data.username)
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token_expires = timedelta(minutes=config.settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        subject=user.username,
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/logout")
def logout():
    # With JWT, "logout" is usually handled on the client side by deleting the token.
    # If you want server-side invalidation, maintain a blacklist of tokens in DB/Redis.
    return {"msg": "Successfully logged out"}
