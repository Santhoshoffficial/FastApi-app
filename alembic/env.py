
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from app.db.base import Base  # ✅ our Base with models imported
from app.core.config import settings

# This is the Alembic Config object, which provides access to the values within alembic.ini
config = context.config

# Interpret the config file for Python logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata  # ✅ Alembic will now see all models
