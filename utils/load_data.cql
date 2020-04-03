// data directory path
'/Users/kristibui/Desktop/Spring20/Large Scale Storage and Retrieval/foodies/utils/random_food_users.csv'

// Delete All Nodes
MATCH (n)
DETACH DELETE n

// Show All Nodes
MATCH (n) RETURN (n)

// -------- Loading Data Cyphers --------

LOAD CSV FROM 'file:///random_food_users.csv' AS line
CREATE (:Person { user_id: line[0], gender: line[1], feet_height: toInteger(line[2]), inches_height: toInteger(line[3]), weight: toInteger(line[4])})

LOAD CSV FROM 'file:///friendships.csv' AS line
MATCH (p1:Person) where p1.user_id = line[0]
MATCH (p2:Person) where p2.user_id = line[1]
MERGE (p2)-[:friends_with]->(p1)

LOAD CSV WITH HEADERS FROM 'file:///restaurants.csv' AS line
CREATE (:Restaurant {restaurant_id: line.restaurant_id, restaurant_name: line.restaurant_name, price_range: line.price_range, address: line.address, cuisine: line.cuisine})

LOAD CSV WITH HEADERS FROM 'file:///foods.csv' AS line
CREATE (:Food {restaurant_id: line.restaurant_id, item: line.item, category: line.category, item_price: line.item_price})

MATCH (f:Food)
MATCH (r:Restaurant) where r.restaurant_id = f.restaurant_id
MERGE (f)-[:menu_item]->(p)


// -------- Viewing Data Cyphers --------

MATCH (n:Person)-[r:friends_with]->(friend:Person) where n.user_id = '1'
RETURN n, r, friend

MATCH (n:Restaurant)<-[r:menu_item]-(f:Food) where n.restaurant_id = '1001'
RETURN n, r, f

MATCH (f:Food)-[r:menu_item]->(n:Restaurant) where f.restaurant_id = '1001'
RETURN f, r, n
