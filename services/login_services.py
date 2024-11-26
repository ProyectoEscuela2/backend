from utils.sqlite_utils import read_sql_query
from queries.login_queries import query_read_hash

def read_hash():
    hash = read_sql_query(lambda cur: cur.execute(query_read_hash).fetchone())[0]

    return hash
