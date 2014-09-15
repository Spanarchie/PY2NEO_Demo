__author__ = 'colinmoore-hill'


from py2neo.neo4j import GraphDatabaseService, CypherQuery


# Set up a link to the local graph database.
# When () left blank defaults to http://localhost:7474/db/data/
graph = GraphDatabaseService()


cypher = "create (C :country {name:\"Homeland\" }) return C"

CypherQuery(graph, cypher).execute()



