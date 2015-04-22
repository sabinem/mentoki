#!/bin/bash

set -e

LIVE_USER=sabinemaennel
LIVE_PASSWORD=Island2015
LIVE_HOST=localhost
LIVE_DATABASE=netteachers_master

DEV_USER=sabinemaennel
DEV_PASSWORD=Island2015
DEV_HOST=localhost
DEV_DATABASE=netteachers_dev

SQLFILE=master.sql

# dump live database
PGPASSWORD=$LIVE_PASSWORD pg_dump -U $LIVE_USER -h $LIVE_HOST $LIVE_DATABASE \
	--schema public > $SQLFILE

# delete all tables in test database
echo "SELECT 'DROP TABLE IF EXISTS \"' || tablename || '\" CASCADE;' FROM pg_tables WHERE schemaname='public';" | \
	PGPASSWORD=$DEV_PASSWORD psql -U $DEV_USER -h $DEV_HOST $DEV_DATABASE -t |
	PGPASSWORD=$DEV_PASSWORD psql -U $DEV_USER -h $DEV_HOST $DEV_DATABASE

# restore dump to test database
PGPASSWORD=$DEV_PASSWORD psql -U $DEV_USER -h $DEV_HOST $DEV_DATABASE < $SQLFILE