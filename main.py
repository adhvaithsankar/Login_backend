import fastapi as _fastapi
import fastapi.security as _security
import sqlalchemy.orm as _orm
import services as _services,schema as _schema
from fastapi.middleware.cors import CORSMiddleware
app = _fastapi.FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)



@app.post("/api/users")
async def create_user(user:_schema.UserCreate,db:_orm.session = _fastapi.Depends(_services.get_db)):
    db_user = await _services.get_user_by_email(user.email,db)
    if db_user:
        raise _fastapi.HTTPException(status_code=400,detail="Email already registered")
    user = await _services.create_user(user,db)
    return await _services.create_token(user)
    
@app.post("/api/token")
async def generate_token(form_data:_security.OAuth2PasswordRequestForm = _fastapi.Depends(),db:_orm.session = _fastapi.Depends(_services.get_db)):
         user = await _services.authenticate_user(form_data.username,form_data.password,db) 
         if not user:
               raise _fastapi.HTTPException(status_code = 401,detail = "Invalid Credentials") 
         return await _services.create_token(user)  

@app.get("/api/users/me",response_model=_schema.User)
async def get_user(user:_schema.User = _fastapi.Depends(_services.get_current_user)):
    return user

@app.get("/api")
async def root():
    return {"message": "Awesome Leads Manager"}

