import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import passlib.hash as _hxh
import database as _db

class User(_db.Base):
    __tablename__ = "user"
    id = _sql.Column(_sql.Integer,primary_key= True, nullable= False,index = True)
    email = _sql.Column(_sql.String,index = True,unique = True,nullable = False)
    hashed_password = _sql.Column(_sql.String)

    invoice = _orm.relationship("Invoice",back_populates="employee")

    user_details = _orm.relationship("UserDetails",back_populates="user")

    def verify_password(self,password):
        return _hxh.bcrypt.verify(password,self.hashed_password)
    



class UserDetails(_db.Base):
    __tablename__ = "user_details"
    id = _sql.Column(_sql.Integer,primary_key=True,nullable=False,index = True)
    user_id = _sql.Column(_sql.Integer,_sql.ForeignKey("user.id"))
    user_name = _sql.Column(_sql.String,nullable = False)
    user_ph_no = _sql.Column(_sql.Integer,index = True)

    user = _orm.relationship("User",back_populates="user_details")




    
    

class Invoice(_db.Base):
    __tablename__ = "invoice"
    id = _sql.Column(_sql.Integer,primary_key=True,nullable=False,index = True)
    employee_id = _sql.Column(_sql.Integer,_sql.ForeignKey("user.id"))
    Invoice_no = _sql.Column(_sql.String,nullable = False)
    Bill_date = _sql.Column(_sql.Date,nullable=False)
    status = _sql.Column(_sql.String,nullable=False)
    employee = _orm.relationship("User",back_populates="invoice")

    


