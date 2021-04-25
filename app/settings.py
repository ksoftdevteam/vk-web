import os

WEBAPP_HOST = os.getenv('WEBAPP_HOST')
WEBAPP_PORT = int(os.getenv('WEBAPP_PORT'))
API_V1_STR = os.getenv('API_V1_STR')
POSTGRES_DB = os.environ.get("POSTGRES_DB", 'nyamnyam')
POSTGRES_USER = os.environ.get("POSTGRES_USER", 'postgres')
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", 'nyamnyam')
POSTGRES_CONTAINER_NAME = os.environ.get("POSTGRES_CONTAINER_NAME", "localhost")