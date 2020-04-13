from neo4j import GraphDatabase, basic_auth
import json


class Neo4J_API:

    def __init__(self):
        self.app = None
        self.driver = None
        self.session = None


    # initialize driver connection to Neo4J
    def init_connection(self, app):
        self.app = app
        self.driver = self.connect('bolt://localhost:7687', 'kristi', 'bui')
        self.session = self.driver.session()


    # connect to database using credentials
    def connect(self, uri, user, password):
        driver = GraphDatabase.driver(uri, auth=(user, password), encrypted=False)
        return driver


    # query user information
    def get_users(self, id=''):
        if id == '':
            query = "MATCH (n:Person) RETURN n.feet_height, n.weight, n.gender, n.user_id, n.inches_height"
        else:
            query = "MATCH (n:Person) WHERE n.user_id = '" + str(id) + "' " \
                    "RETURN n.feet_height, n.weight, n.gender, n.user_id, n.inches_height"

        return self.session.run(query)


    # wrapper for getting user data & converting to usable json format
    def get_users_json(self, id=''):

        res = self.get_users(id)

        json = []

        for record in res:
            json.append({'feet_height': record['n.feet_height'],
                        'gender': record['n.gender'],
                        'user_id': record['n.user_id'],
                        'inches_height': record['n.inches_height'],
                        'weight': record['n.weight']})

        return json


    # recommendation #1: based on users with similar tastes at same restaurant
    def recommend_dish_based_on_similar_users(self, id):

        query = "MATCH (p1:Person {user_id: '" + str(id) + "'})<-[:ordered_by]-(p1_top_order:Orders)" \
                "-[:ordered_item]->(p1_top_food:Food)-[:menu_item]->(r:Restaurant) WITH p1, p1_top_food," \
                " p1_top_order, r ORDER BY toInteger(p1_top_order.order_count) DESC LIMIT 1 MATCH " \
                "(p1_top_food)<-[:ordered_item]-(p2_top_order:Orders) WHERE NOT (p2_top_order = " \
                "p1_top_order) WITH p1, p1_top_food, p1_top_order, p2_top_order, r ORDER BY " \
                "toInteger(p2_top_order.order_count) DESC LIMIT 1 MATCH (p2_top_order)-" \
                "[:ordered_by]->(p2:Person)<-[:ordered_by]-(p2_recommended_order:Orders)-" \
                "[:ordered_item]->(p2_recommended_dish:Food) WHERE NOT (p2_recommended_order"\
                " = p2_top_order) AND (p2_recommended_dish.restaurant_id = r.restaurant_id) " \
                "RETURN p1_top_food, r, p2_recommended_dish ORDER BY toInteger(p2_recommended_order.order_count) DESC LIMIT 1"

        return self.session.run(query)


    # recommendation #2: dishes of similar category at same restaurant
    def recommend_dish_similar_users_category(self, id):
        query = "MATCH (p1:Person {user_id: '" + str(id) + "'})<-[:ordered_by]-(p1_top_order:Orders)-[:ordered_item]\
                ->(p1_top_food:Food)-[:menu_item]->(r:Restaurant) WITH p1, p1_top_food, p1_top_order, r \
                ORDER BY toInteger(p1_top_order.order_count) DESC LIMIT 1\
                MATCH (p1_top_food)<-[:ordered_item]-(p2_top_order:Orders)\
                WHERE NOT (p2_top_order = p1_top_order) WITH p1, p1_top_food, p1_top_order, p2_top_order, r \
                ORDER BY toInteger(p2_top_order.order_count) DESC LIMIT 1\
                MATCH (p2_top_order)-[:ordered_by]->(p2:Person)<-[:ordered_by]-(p2_recommended_order:Orders)\
                -[:ordered_item]->(p2_recommended_dish:Food) WHERE NOT (p2_recommended_order = p2_top_order) \
                AND (p2_recommended_dish.restaurant_id = r.restaurant_id) AND \
                (p2_recommended_dish.category = p1_top_food.category) RETURN p1_top_food, r, p2_recommended_dish \
                ORDER BY toInteger(p2_recommended_order.order_count) DESC LIMIT 1"

        return self.session.run(query)


    # recommendation #3: dishes that your friends like at same restaurant
    def recommend_dish_friends(self, id):

        query = ""

        return self.session.run(query)


    # wrapper for recommendation queries
    def get_recommendation(self, id, rec_type):

        # query for specific rec
        if rec_type == 1:
            res = self.recommend_dish_based_on_similar_users(id)
        elif rec_type == 2:
            res = self.recommend_dish_similar_users_category(id)
        elif rec_type == 3:
            res = self.recommend_dish_friends(id)

        # Only one line in result
        for line in res:
            favorite_dish = line['p1_top_food']
            restaurant = line['r']
            recommended_dish = line['p2_recommended_dish']

        json = []

        try:

            json.append({'item': favorite_dish['item'],
                        'subsection': favorite_dish['subsection'],
                        'menu_id': favorite_dish['menu_id'],
                        'price': favorite_dish['price'],
                        'restaurant_id': favorite_dish['restaurant_id']})
            json.append({'cuisines': restaurant['cuisine'],
                        'city': restaurant['city'],
                        'street': restaurant['street'],
                        'restaurant_id': restaurant['restaurant_id'],
                        'restaurant_name': restaurant['restaurant_name']})
            son.append({'item': recommended_dish['item'],
                        'subsection': recommended_dish['subsection'],
                        'menu_id': recommended_dish['menu_id'],
                        'price': recommended_dish['price'],
                        'restaurant_id': recommended_dish['restaurant_id']})

        except UnboundLocalError:

            # No value for this (no recommended dish!)
            json.append({'item': 'none'})

        return json


#for debugging purposes
# def main():
#
#     db = Neo4J_API()
#     db.init_connection('debugging')
#
#     print(db.get_recommendation_2(3))
#
#
# main()
