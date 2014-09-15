__author__ = 'colinmoore-hill'

from py2neo import neo4j

graph_db = neo4j.GraphDatabaseService()
x = graph_db.neo4j_version
print ("Release Version : {} , Major Version : {}, minor version {} ").format(x[0],x[1],x[2])