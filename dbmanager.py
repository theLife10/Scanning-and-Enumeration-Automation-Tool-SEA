from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement, BatchStatement


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
    result = session.execute(batch)
    # Close connection
    closeConnection(session)


def deleteQuery(statement, variable):
    session = connect()
    batch = BatchStatement()
    batch.add(statement, variable)
    keyspace = "USE tutorialspoint;"
    session.execute(keyspace)
    # Execute
    result = session.execute(batch)
    # Close connection
    closeConnection(session)

def closeConnection(session):
    session.shutdown()