# utils/logger.py

from loguru import logger
import sys
import os

# Create logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configure logger
logger.remove()  # Remove the default logger
logger.add(sys.stdout, level="INFO", format="<green>{time}</green> <level>{message}</level>")
logger.add("logs/multi_agent_system.log", rotation="1 MB", retention="10 days", level="DEBUG", format="{time} {level} {message}")
