# app/main.py
from fastapi import FastAPI
from app.api.v1 import auth, users, role

app = FastAPI(title="EMS API")

# include routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
# app.include_router(role.router, prefix="/api/v1/roles", tags=["roles"])

@app.get("/")
def root():
    return {"msg": "Welcome to EMS API"}


