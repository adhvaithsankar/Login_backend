import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

DB_URI = "postgresql://invoice_mfz9_user:UOt6wMB1s35yqZs4KjI0tBUvzMdMqNm8@dpg-cnulse0cmk4c73ffdjig-a.oregon-postgres.render.com/invoice_mfz9"

engine = _sql.create_engine(DB_URI)

sessionlocal = _orm.sessionmaker(autocommit = False, autoflush = False , bind = engine)

Base = _declarative.declarative_base()



