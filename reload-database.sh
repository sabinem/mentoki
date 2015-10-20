#!/bin/bash

set -e

TEST_USER=sabinemaennel
TEST_PASSWORD=Island2015
TEST_HOST=localhost
TEST_DATABASE=mentoki_25_9

SQLFILE=live.sql

# delete all tables in test database
echo "SELECT 'DROP TABLE IF EXISTS \"' || tablename || '\" CASCADE;' FROM pg_tables WHERE schemaname='public';" | \
	PGPASSWORD=$TEST_PASSWORD psql -U $TEST_USER -h $TEST_HOST $TEST_DATABASE -t |
	PGPASSWORD=$TEST_PASSWORD psql -U $TEST_USER -h $TEST_HOST $TEST_DATABASE

# restore dump to test database
PGPASSWORD=$TEST_PASSWORD psql -U $TEST_USER -h $TEST_HOST $TEST_DATABASE < $SQLFILE
