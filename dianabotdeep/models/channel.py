from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Channel(Base):
    __tablename__ = 'channels'
    
    id = Column(Integer, primary_key=True)
    channel_id = Column(String(100), unique=True)
    title = Column(String(255))
    username = Column(String(100), nullable=True)
    is_active = Column(Boolean, default=True)
    admin_id = Column(Integer)
    
    def __repr__(self):
        return f"<Channel {self.title} ({self.channel_id})>"