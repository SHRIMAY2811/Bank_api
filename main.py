from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models, schemas
from database import engine, get_db

# Initialize DB tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bank Information Service")

@app.get("/banks", response_model=List[schemas.BankBase])
def read_banks(db: Session = Depends(get_db)):
    """Fetch the list of all banks."""
    return db.query(models.Bank).all()

@app.get("/branches/{ifsc}", response_model=schemas.BranchBase)
def read_branch_details(ifsc: str, db: Session = Depends(get_db)):
    """Fetch details for a specific branch by IFSC."""
    branch = db.query(models.Branch).filter(models.Branch.ifsc == ifsc.upper()).first()
    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")
    return branch