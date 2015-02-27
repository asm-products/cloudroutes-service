import sys
import yaml

import rethinkdb as r
from rethinkdb.errors import RqlDriverError, RqlRuntimeError
import socket


def set_auth(conn):
    try:
        r.db('rethinkdb').table('cluster_config').update(
            {'auth_key': config['rethink_authkey']}).run(conn)
    except (RqlDriverError, RqlRuntimeError, socket.error) as e:
        print("RethinkDB Error: %s") % e.message

# Open Config File and Parse Config Data
configfile = sys.argv[1]
cfh = open(configfile, "r")
config = yaml.safe_load(cfh)
cfh.close()

# Establish Connection
host = config['rethink_host']
port = config['rethink_port']

try:
    conn = r.connect(host, port).repl()
except (RqlDriverError, RqlRuntimeError, socket.error) as e:
    print("RethinkDB Error on Connection: %s") % e.message
    sys.exit(1)


set_auth(conn)

cursor = r.db('rethinkdb').table('cluster_config').run(conn)
for data in cursor:
    print data

conn.close()

print "Authentication set!"
