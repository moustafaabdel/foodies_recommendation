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


LOAD CSV FROM 'file:///random_food_orders.csv' AS line
CREATE (:Orders { order_id: line[0], user_id: line[1], menu_id: line[2], order_count: line[3]})

MATCH (o:Orders)
MATCH (n:Person) where o.user_id = n.user_id
MERGE (o)-[:ordered_by]->(n)

MATCH (o:Orders)-[r:ordered_by]->(n:Person) where n.user_id = '1'
RETURN o, r, n

MATCH (o:Orders)
MATCH (f:Food) where o.menu_id = f.food_id
MERGE (o)-[r:ordered_item]->(f)


// -------- Viewing Data Cyphers --------

MATCH (n:Person)-[r:friends_with]->(friend:Person) where n.user_id = '1'
RETURN n, r, friend

MATCH (n:Restaurant)<-[r:menu_item]-(f:Food) where n.restaurant_id = '1001'
RETURN n, r, f

MATCH (f:Food)-[r:menu_item]->(n:Restaurant) where f.restaurant_id = '1001'
RETURN f, r, n

MATCH (o:Orders)-[r:ordered_item]->(f:Food) where o.order_id = '1'
RETURN o, r, f

// -------- Recommendation Algorithms --------

// Recommendation #1 : Basic recommendation of top 5 food orders that my friends like
MATCH (p:Person {user_id: '1'})-[:friends_with]->(friend:Person)<-[:ordered_by]-(o:Orders)-[:ordered_item]->(f:Food)
RETURN p, friend, o, f
ORDER BY toInteger(o.order_count) DESC
LIMIT 5


// Recommendation #2: Recommend another dish at the same restaurant that's been ordered the top amount of times
// and is not the original dish
MATCH (p:Person {user_id: '1'})<-[:ordered_by]-(o:Orders)-[:ordered_item]->(top_order:Food)
WITH p, top_order
ORDER BY toInteger(top_order.order_count) DESC LIMIT 1
MATCH (top_order)-[:menu_item]->(r:Restaurant)<-[:menu_item]-(restaurant_top_food:Food)<-[:ordered_item]-(restaurant_top_order:Orders)
WHERE NOT (top_order = restaurant_top_food)
RETURN p, top_order, r, restaurant_top_food
ORDER BY toInteger(restaurant_top_order.order_count) DESC LIMIT 1


// Recommendation #3: Recommend another dish at the same restaurant of the same category
// that's been ordered the top amount of times
MATCH (p:Person {user_id: '1'})<-[:ordered_by]-(o:Orders)-[:ordered_item]->(top_order:Food)
WITH p, top_order
ORDER BY toInteger(top_order.order_count) DESC LIMIT 1
MATCH (top_order)-[:menu_item]->(r:Restaurant)<-[:menu_item]-(restaurant_top_food:Food)<-[:ordered_item]-(restaurant_top_order:Orders)
WHERE NOT (top_order = restaurant_top_food) AND (restaurant_top_food.category = top_order.category)
RETURN p, top_order, r, restaurant_top_food
ORDER BY toInteger(restaurant_top_order.order_count) DESC LIMIT 1


// Recommendation #4: Recommend a dish based on what people who also like your favorite dish also order
MATCH (p1:Person {user_id: '1'})<-[:ordered_by]-(p1_top_order:Orders)-[:ordered_item]->(p1_top_food:Food)
WITH p1, p1_top_food, p1_top_order
ORDER BY toInteger(p1_top_order.order_count) DESC LIMIT 1
MATCH (p1_top_food)<-[:ordered_item]-(p2_top_order:Orders)
WHERE NOT (p2_top_order = p1_top_order)
WITH p1, p1_top_order, p2_top_order
ORDER BY toInteger(p2_top_order.order_count) DESC LIMIT 1
MATCH (p2_top_order)-[:ordered_by]->(p2:Person)<-[:ordered_by]-(p2_recommended_order:Orders)-[:ordered_item]->(p2_recommended_dish:Food)
WHERE NOT (p2_recommended_order = p2_top_order)
RETURN p1, p2, p2_recommended_dish
ORDER BY toInteger(p2_recommended_order.order_count) DESC LIMIT 1


// Recommendation #5: Recommend a dish at the same restaurant
// based on what people who also like your favorite dish also order
// NOTE: this one assumes that there is someone who has multiple orders at the same restaurant
MATCH (p1:Person {user_id: '1'})<-[:ordered_by]-(p1_top_order:Orders)-[:ordered_item]->(p1_top_food:Food)-[:menu_item]->(r:Restaurant)
WITH p1, p1_top_food, p1_top_order, r
ORDER BY toInteger(p1_top_order.order_count) DESC LIMIT 1
MATCH (p1_top_food)<-[:ordered_item]-(p2_top_order:Orders)
WHERE NOT (p2_top_order = p1_top_order)
WITH p1, p1_top_order, p2_top_order, r
ORDER BY toInteger(p2_top_order.order_count) DESC LIMIT 1
MATCH (p2_top_order)-[:ordered_by]->(p2:Person)<-[:ordered_by]-(p2_recommended_order:Orders)-[:ordered_item]->(p2_recommended_dish:Food)
WHERE NOT (p2_recommended_order = p2_top_order) AND (p2_recommended_dish.restaurant_id = r.restaurant_id)
RETURN p1, p2, p2_recommended_dish
ORDER BY toInteger(p2_recommended_order.order_count) DESC LIMIT 1
