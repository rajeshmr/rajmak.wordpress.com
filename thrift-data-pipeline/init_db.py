import os
import sqlite3
import pipeline_config


db_is_new = not os.path.exists(pipeline_config.DB_LOCATION)
with sqlite3.connect(pipeline_config.DB_LOCATION) as conn:
    if db_is_new:
        print "creating schema"
        with open(pipeline_config.DB_SCHEMA, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)
    print "Database initialized"


