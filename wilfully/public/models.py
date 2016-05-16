import datetime as dt
import enum

from wilfully.database import Column, Model, SurrogatePK, db, reference_col, relationship
from wilfully.extensions import bcrypt

class FuneralBodyOptions(enum.Enum):
	cremated = 'cremated'
	buried = 'buried'
	other = 'other'

class FuneralProfile(SurrogatePK, Model):
    """A role for a user."""
	__tablename__ = 'funeral'
	user_id = reference_col('users', nullable=True)
    user = relationship('User', backref='funeral')
    ceremony = Column(db.String(30), nullable=True)
    body = Column('value', db.Enum(FuneralBodyOptions))
    payment = Column(db.String(30), nullable=True)


