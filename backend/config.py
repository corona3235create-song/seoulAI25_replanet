import os

# AWS RDS Database Configuration
DB_HOST = os.getenv("DB_HOST", "your-rds-endpoint.rds.amazonaws.com")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_USER = os.getenv("DB_USER", "your-db-user")
DB_PASS = os.getenv("DB_PASS", "your-db-password")
DB_NAME = os.getenv("DB_NAME", "your-db-name")

# JWT Configuration
SECRET_KEY = os.getenv("SECRET_KEY", "your-jwt-secret-key")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
