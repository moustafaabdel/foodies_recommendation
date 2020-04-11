

/ -------- Recommendation Algorithms --------

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


// Recommendation #6: Recommend a dish of the same category at the same restaurant
MATCH (p1:Person {user_id: '1'})<-[:ordered_by]-(p1_top_order:Orders)-[:ordered_item]->(p1_top_food:Food)-[:menu_item]->(r:Restaurant)
WITH p1, p1_top_food, p1_top_order, r
ORDER BY toInteger(p1_top_order.order_count) DESC LIMIT 1
MATCH (p1_top_food)<-[:ordered_item]-(p2_top_order:Orders)
WHERE NOT (p2_top_order = p1_top_order)
WITH p1, p1_top_food, p1_top_order, p2_top_order, r
ORDER BY toInteger(p2_top_order.order_count) DESC LIMIT 1
MATCH (p2_top_order)-[:ordered_by]->(p2:Person)<-[:ordered_by]-(p2_recommended_order:Orders)-[:ordered_item]->(p2_recommended_dish:Food)
WHERE NOT (p2_recommended_order = p2_top_order) AND (p2_recommended_dish.restaurant_id = r.restaurant_id) AND (p2_recommended_dish.category = p1_top_food.category)
RETURN p1, p2, p2_recommended_dish
ORDER BY toInteger(p2_recommended_order.order_count) DESC LIMIT 1


