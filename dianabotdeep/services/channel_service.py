from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.channel import Channel

engine = create_engine(Config.DATABASE_URL)
Session = sessionmaker(bind=engine)

class ChannelService:
    @staticmethod
    def add_channel(channel_id: str, title: str, admin_id: int, username: str = None):
        session = Session()
        channel = Channel(
            channel_id=channel_id,
            title=title,
            username=username,
            admin_id=admin_id
        )
        session.add(channel)
        session.commit()
        session.close()
    
    @staticmethod
    def get_user_channels(admin_id: int):
        session = Session()
        channels = session.query(Channel).filter_by(admin_id=admin_id, is_active=True).all()
        session.close()
        return channels