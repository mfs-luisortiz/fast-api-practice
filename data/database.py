from sqlalchemy import create_engine, text
import dotenv


engine = create_engine(dotenv.get_key('.env', 'DATABASE_URL'), echo=True)

def get_users():
    users = None
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM usuario"))
        users = result.all()
    return users