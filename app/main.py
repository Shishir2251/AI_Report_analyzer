from fastapi import FastAPI
from routes import report
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="AI Report Analyzer")
app.include_router(report.router, prefix="/report")
