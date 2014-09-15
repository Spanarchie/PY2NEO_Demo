__author__ = 'colinmoore-hill'

from py2neo import cypher

session = cypher.Session("http://localhost:7474")
tx = session.create_transaction()

# send three statements to for execution but leave the transaction open
tx.append("MERGE (a:Person {name:'Alice'}) "
          "RETURN a")
tx.append("MERGE (b:Person {name:'Bob'}) "
          "RETURN b")
tx.append("MATCH (a:Person), (b:Person) "
          "WHERE a.name = 'Alice' AND b.name = 'Bob' "
          "CREATE UNIQUE (a)-[ab:KNOWS]->(b) "
          "RETURN ab")
tx.execute()

# send another three statements and commit the transaction
tx.append("MERGE (c:Person {name:'Carol'}) "
          "RETURN c")
tx.append("MERGE (d:Person {name:'Dave'}) "
          "RETURN d")
tx.append("MATCH (c:Person), (d:Person) "
          "WHERE c.name = 'Carol' AND d.name = 'Dave' "
          "CREATE UNIQUE (c)-[cd:KNOWS]->(d) "
          "RETURN cd")
tx.commit()