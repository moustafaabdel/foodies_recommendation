#!/usr/bin/env python
# coding: utf-8

# In[28]:


from neo4j import GraphDatabase, basic_auth

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "vidhi"))






# In[29]:


session=driver.session()


# In[38]:


q1 = "MATCH (o:Orders)-[r:ordered_by]->(n:Person) where n.user_id = '1' RETURN o, r, n"

print(session.run(q1))


# In[39]:


Top5FriendsLike = "MATCH (p:Person {user_id: '1'})-[:friends_with]-> (friend:Person)<-[:ordered_by]-(o:Orders)-[:ordered_item]->(f:Food) RETURN p, friend, o, f ORDER BY toInteger(o.order_count) DESC LIMIT 5"

print(session.run(Top5FriendsLike))


# In[10]:





# In[ ]:





# In[16]:





# In[ ]:
