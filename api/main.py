from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import select, Session
from dotenv import load_dotenv
import os

# load .env
load_dotenv(override=True)

from api.database import get_session
from api.models import mTableCell, mHierarchy, mHierarchyNode

app = FastAPI(title="DPM Lookup Service", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

# DPM_DB_URL = os.getenv("DPM_DB_URL")
# API_HOST  = os.getenv("API_HOST", "127.0.0.1")
# API_PORT  = int(os.getenv("API_PORT", 8000))

# lookup with in-memory caching

@app.get("/cell/{business_code}", tags=["Lookup"])
def get_dps_by_business_code(
    business_code: str,
    session: Session = Depends(get_session)
):
    """
    Return the DPS value for a given BusinessCode.
    """
    statement = select(mTableCell).where(mTableCell.BusinessCode == business_code)
    result = session.exec(statement).first()
    if not result:
        raise HTTPException(
            status_code=404,
            detail=f"No table cell found for BusinessCode '{business_code}'"
        )
    return {
        "BusinessCode": result.BusinessCode,
        "DPS": result.DPS,
        "CellID": result.CellID,
        "TableID": result.TableID
    }