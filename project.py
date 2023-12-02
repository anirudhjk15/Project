from fastapi import FastAPI, File, UploadFile, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from databases import Database
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table

# SQLite Database Configuration
DATABASE_URL = "sqlite:///./test.db"
database = Database(DATABASE_URL)
metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, index=True),
    Column("age", Integer),
)

# FastAPI Configuration
app = FastAPI()

# Jinja2 Templates Configuration
templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
async def startup_db():
    engine = create_engine(DATABASE_URL)
    metadata.create_all(bind=engine)
    await database.connect()


@app.on_event("shutdown")
async def shutdown_db():
    await database.disconnect()


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/uploadfile/")
async def create_upload_file(

        file: UploadFile = File(...),
        name_column: int = Form(...),
        age_column: int = Form(...),
):
    content = await file.read()
    content = content.decode("utf-8").splitlines()

    # Assume the first row contains headers
    headers = content[0].split(",")

    name_index = name_column - 1
    age_index = age_column - 1

    # Validate selected columns
    if name_index >= len(headers) or age_index >= len(headers):
        return {"detail": "Invalid column selection"}

    # Extract data and save to the database
    for row in content[1:]:
        row_data = row.split(",")
        name = row_data[name_index]
        age = int(row_data[age_index])
        await database.execute(users_table.insert().values(name=name, age=age))

    return {"detail": "File uploaded and data saved to the database"}
