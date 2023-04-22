import logging

from fastapi import FastAPI

from routes import company, photo, status, specialty, education, user

logging.basicConfig(level=logging.INFO,
                    format="%(levelname)s:  %(asctime)s  %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")

app = FastAPI()
app.include_router(company.router)
app.include_router(photo.router)
app.include_router(status.router)
app.include_router(specialty.router)
app.include_router(education.router)
app.include_router(user.router)


@app.get("/")
async def root():
    logging.info("Root application start")
