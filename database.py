# database.py
import os
from dotenv import load_dotenv
import sqlalchemy
from sqlalchemy import create_engine, text

# load .env (for local development)
load_dotenv()

print(sqlalchemy.__version__)

# read connection string from env
db_connection_string = os.getenv("DB_CONNECTION_STRING")
if not db_connection_string:
    raise ValueError(
        "DB_CONNECTION_STRING is not set. Add it to your environment or create a .env file with DB_CONNECTION_STRING="
    )

# create engine (ensure the CA file exists at ssl/ca.pem)
engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {"ca": "ssl/cert.pem"}
    }
)


def load_jobs_from_db():
    """Return list of all jobs as dicts."""
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        # result.mappings() returns mapping-like rows that convert cleanly to dict
        return [dict(r) for r in result.mappings().all()]


def load_job_from_db(id):
    """Return single job dict by id, or None if not found."""
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM jobs WHERE id = :val"), {"val": id}
        )
        row = result.mappings().first()
        if row is None:
            return None
        return dict(row)
