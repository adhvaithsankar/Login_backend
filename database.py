import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

DB_URI = "postgresql://aws_invoice_user:oFsKPV03cSTIvRFwmkEiiJhnc99dNhxp@dpg-cnu1hgda73kc73f5966g-a.singapore-postgres.render.com/aws_invoice"

engine = _sql.create_engine(DB_URI)

sessionlocal = _orm.sessionmaker(autocommit = False, autoflush = False , bind = engine)

Base = _declarative.declarative_base()



