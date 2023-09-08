from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Item

router = APIRouter()

def get_item(id: int, db: Session):
    item = db.query(Item).filter(Item.id == id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/input/{my_target_field}", response_model=Item)
def create_item(my_target_field: str, item: Item, db: Session = Depends(SessionLocal)):
    if my_target_field not in ["field_1", "author", "description"]:
        raise HTTPException(status_code=400, detail="Invalid target field")

   
    if hasattr(item, my_target_field) and isinstance(getattr(item, my_target_field), str):
        setattr(item, my_target_field, getattr(item, my_target_field).upper())
    else:
        raise HTTPException(status_code=400, detail=f"{my_target_field} no es un campo de texto válido")

    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.get("/get_data/{id}", response_model=Item)
def read_item(id: int, db: Session = Depends(SessionLocal)):
    return get_item(id, db)
