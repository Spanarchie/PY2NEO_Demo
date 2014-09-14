__author__ = 'colin moore-hill'
from py2neo import neo4j

graph_db = neo4j.GraphDatabaseService()

query = neo4j.CypherQuery(graph_db, "CREATE (a {name:{name_a}})-[ab:KNOWS]->(b {name:{name_b}}) RETURN a, b, ab")
a, b, ab = query.execute(name_a="Alice", name_b="Bob").data[0]
