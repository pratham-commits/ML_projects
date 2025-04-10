import logging
import os
from datetime import datetime

# we log every execution that occurs so that we are able to 
# keep of very exception and execution happening

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_paths=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(log_paths,exist_ok=True)

LOG_FILE_PATH=os.path.join(log_paths,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="%(asctime)s - %(levelname)s - %(filename)s - Line %(lineno)d - %(message)s",
    level=logging.INFO,
    filemode='a'
)


