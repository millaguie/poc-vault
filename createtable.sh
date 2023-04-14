#!/bin/sh

psql -c "CREATE TABLE test (id serial PRIMARY KEY, num integer);" -d testdb
