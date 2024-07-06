from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from db import crud, models, schemas
from db.database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users",  response_model=list[schemas.User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    authors = crud.get_users(db, skip=skip, limit=limit)
    if not authors:
        raise HTTPException(status_code=404, detail="Користувачів не знайдено")
    return authors

@app.post("/users/{user_id}", response_model=schemas.User)
async def get_user_by_id(user_id:int, db: Session = Depends(get_db)):
    db_author = crud.get_user_by_id(db, user_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Автор не знайдений")
    return db_author

@app.post("/create_user", response_model=schemas.User)
def add_user(user : schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = crud.get_user_by_username(db = db,username=user.username)
    if new_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Такий користувач вже існує",
        )
    return crud.create_user(db=db, user=user)








  

