import os

# project base path
PROJ_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# default log file path
LOG_PATH_DEFAULT = os.path.join(os.path.join(os.path.join(PROJ_DIR, 'app'), 'log'), 'app.log')


SUCCESS_MSG = "success"
ERROR_MSG = "error"