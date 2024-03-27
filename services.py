import database as _db,model as _models,schema as _schemas
import sqlalchemy.orm as _orm
import passlib.hash as _hash
import jwt as _jwt
import fastapi as _fastapi
import fastapi.security as _security

JWT_SECRET = "atulyarahasya"
oauth2schema = _security.OAuth2PasswordBearer(tokenUrl="/api/token")

def create_database():
    return _db.Base.metadata.create_all(bind = _db.engine)

def get_db():
    db = _db.sessionlocal()
    try:
        yield db
    finally:
        db.close()

async def get_user_by_email(email:str,db: _orm.session):
    return db.query(_models.User).filter(_models.User.email == email).first()

async def create_user(user: _schemas.UserCreate, db: _orm.session):
    user_obj = _models.User(
        email=user.email, hashed_password=_hash.bcrypt.hash(user.hashed_password)
    )
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj

async def authenticate_user(email:str,password:str,db:_orm.session):
    user = await get_user_by_email(email=email,db=db)
    if not user:
        return False
    if not _hash.bcrypt.verify(password,user.hashed_password):
        return False
    return user

async def create_token(user:_models.User):
    user_obj = _schemas.User.from_orm(user)

    token = _jwt.encode(user_obj.dict(),JWT_SECRET)

    return dict(access_token= token,token_type="bearer")



async def get_current_user(db:_orm.session = _fastapi.Depends(get_db),token:str = _fastapi.Depends(oauth2schema)):
    try:
        payload = _jwt.decode(token,JWT_SECRET,algorithms = ["HS256"])
        user = db.query(_models.User).get(payload["id"])
    except:
        raise _fastapi.HTTPException(status_code=401,detail="Invalid Email or Password")
    return _schemas.User.from_orm(user) 