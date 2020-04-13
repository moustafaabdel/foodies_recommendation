// -------- Loading Data Cyphers --------

LOAD CSV FROM 'file:///random_food_users.csv' AS line
CREATE (:Person { user_id: line[0], gender: line[1], feet_height: toInteger(line[2]), inches_height: toInteger(line[3]), weight: toInteger(line[4])})

LOAD CSV FROM 'file:///friendships.csv' AS line
MATCH (p1:Person) where p1.user_id = line[0]
MATCH (p2:Person) where p2.user_id = line[1]
MERGE (p2)-[:friends_with]->(p1)

LOAD CSV WITH HEADERS FROM 'file:///restaurants.csv' AS line
CREATE (:Restaurant {restaurant_id: line.restaurant_id, restaurant_name: line.restaurant_name, price_range: line.price_range, street: line.street, city: line.city, cuisines: line.cuisines})

LOAD CSV WITH HEADERS FROM 'file:///foods.csv' AS line
CREATE (:Food {menu_id: line.menu_id, restaurant_id: line.restaurant_id, item: line.menu_item_name, subsection: line.subsection, price: line.price})

MATCH (f:Food)
MATCH (r:Restaurant) where r.restaurant_id = f.restaurant_id
MERGE (f)-[:menu_item]->(r)


LOAD CSV FROM 'file:///random_food_orders.csv' AS line
CREATE (:Orders { order_id: line[0], user_id: line[1], menu_id: line[2], order_count: line[3]})

MATCH (o:Orders)
MATCH (n:Person) where o.user_id = n.user_id
MERGE (o)-[:ordered_by]->(n)

MATCH (o:Orders)
MATCH (f:Food) where o.menu_id = f.menu_id
MERGE (o)-[:ordered_item]->(f)

LOAD CSV FROM 'file:///categories.csv' AS line
CREATE (:Categories {restaurant_id: line[0], category: line[1]})

MATCH (c:Categories)
MATCH (r:Restaurant) where r.restaurant_id = c.restaurant_id
MERGE (c)-[:category]->(r)


// -------- Viewing Sample Data Cyphers --------

MATCH (n:Person)-[r:friends_with]->(friend:Person) where n.user_id = '1'
RETURN n, r, friend

MATCH (n:Restaurant)<-[r:menu_item]-(f:Food) where n.restaurant_id = '586'
RETURN n, r, f

MATCH (f:Food)-[r:menu_item]->(n:Restaurant) where f.restaurant_id = '586'
RETURN f, r, n

MATCH (o:Orders)-[r:ordered_item]->(f:Food) where o.order_id = '1'
RETURN o, r, f
