from fastapi import FastAPI

def create_start_app_handler(app: FastAPI):
    async def start_app() -> None:
        # connect db, init cache, etc.
        pass
    return start_app

def create_stop_app_handler(app: FastAPI):
    async def stop_app() -> None:
        # close db, cleanup
        pass
    return stop_app
