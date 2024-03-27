import datetime as _dt

import pydantic as _pydantic

class _UserBase(_pydantic.BaseModel):
    email: str

class UserCreate(_UserBase):
    hashed_password: str

    class Config:
        orm_mode = True
        from_attributes = True

class User(_UserBase):
    id: int
    class Config:
        orm_mode = True
        from_attributes = True

class Invoice(_pydantic.BaseModel):
    invoice_no: str
    bill_date: _dt.date
    status:str

class InvoiceCreate(Invoice):
    pass

class Invoice(Invoice):
    id: int
    employee_id: int

    class Config:
        orm_mode = True
        from_attributes = True
