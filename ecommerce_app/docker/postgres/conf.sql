ALTER SYSTEM SET wal_level = logical;
ALTER SYSTEM SET max_replication_slots = 2;

ALTER USER postgres WITH SUPERUSER;