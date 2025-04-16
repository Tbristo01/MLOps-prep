import logging
import os
from datetime import datetime

# Create log filename with correct timestamp format
LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"

# Create logs directory
log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok=True)

# Define log file path
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='%(asctime)s - %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")