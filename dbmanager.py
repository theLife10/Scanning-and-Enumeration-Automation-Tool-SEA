from cassandra.cluster import Cluster
from cassandra.query import BatchStatement


def connect():
    cluster = Cluster(['127.0.0.1'], 9042)
    # Database Credentials
    session = cluster.connect()
    return session

def selectQuery(statement):
    session = connect()
    batch = BatchStatement()
    batch.add(
        statement)
    keyspace = "USE tutorialspoint;"
    session.execute(keyspace)
    # Execute
    result = session.execute(statement)
    # Close connection
    closeConnection(session)
    return result


def insertQuery(statement, variables):
    session = connect()
    batch = BatchStatement()
    batch.add(statement,
        (variables))
    keyspace = "USE tutorialspoint;"
    session.execute(keyspace)
    # Execute
    session.execute(batch)
    # Close connection
    closeConnection(session)

def updateList(table, column, row, name, insert):
    session = connect()
    statement =  f"UPDATE {table} SET {column} = {column} + {insert} where {row} = '{name}';"
    session.execute("USE tutorialspoint;")
    session.execute(statement)
    closeConnection(session)

def deleteQuery(statement, variable):
    session = connect()
    batch = BatchStatement()
    batch.add(statement, variable)
    keyspace = "USE tutorialspoint;"
    session.execute(keyspace)
    # Execute
    session.execute(batch)
    # Close connection
    closeConnection(session)

def closeConnection(session):

    session.shutdown()

