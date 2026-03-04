CREATE USER backend_user WITH PASSWORD 'backend_password';

CREATE DATABASE backend OWNER backend_user;

GRANT ALL PRIVILEGES ON DATABASE backend TO backend_user;

\c backend

GRANT ALL PRIVILEGES ON SCHEMA public TO backend_user;
