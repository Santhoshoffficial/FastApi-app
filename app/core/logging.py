from loguru import logger

logger.add("logs/ems.log", rotation="1 week", retention="1 month", level="INFO")
