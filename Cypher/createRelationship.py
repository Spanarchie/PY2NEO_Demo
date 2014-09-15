__author__ = 'colin moore-hill'

from py2neo.neo4j import GraphDatabaseService, CypherQuery

# Set up a link to the local graph database.
# When () left blank defaults to http://localhost:7474/db/data/
graph = GraphDatabaseService()

cypher = "CREATE (a :person {name:\"Eric Idle\"})-[ab:KNOWS]->(b :person {name:\"John Cleese\"}) RETURN a, b, ab"

CypherQuery(graph, cypher).execute()