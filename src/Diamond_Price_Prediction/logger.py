import logging, os
from datetime import datetime
from pathlib import Path

log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path = os.path.join(Path(os.getcwd()).resolve().parent, "logs")
os.makedirs(log_path, exist_ok=True)

log_file_path = os.path.join(log_path, log_file)

logging.basicConfig(level = logging.INFO,
                    filename = log_file_path, 
                    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s %(message)s"
)


