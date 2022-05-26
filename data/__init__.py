import collections
import os 


from abstaction import *
import data.jsonl

DATA_DIRECTORY = 'data'
USER_DIRECTORY = 'users'


def load_data(user_dataset, review_dataset, restaurant_dataset):
	with open(os.path.join(DATA_DIRECTORY, user_dataset)) as f:
		user_data = jsonl.load(f)
	with open(os.path.join(DATA_DIRECTORY, review_dataset)) as f:
		review_dataset = jsonl.load(f)
	with open(os.path.join(DATA_DIRECTORY, restaurant_dataset)) as f:
		restaurant_data = jsonl.load(f)



	userid_to_user = {}
	for user in user_data:
		name = user['name']
		_user_id = user['user_id']
		user = make_user(name, [])


		userid_to_user[_user_id] = user



	busid_to_restaurant = {}
	for restaurant in restaurant_data:
		name = restaurant['name']
		location = float(restaurant['latitude']), float(restaurant['longitude'])
		categories = restaurant['categories']
		price = restaurant['price']

		if price is not None:
			price  = int(price)

		num_reviews = int(restaurant['review_count'])
		restaurant = make_restaurant(name,location, categories,price, [])
		busid_to_restaurant[_business_id] = restaurant


	review = []
	busid_to_restaurant = collections.defaultdict(list)
	userid_to_user = collections.defaultdict(list)
	for review in review_data:
		_user_id = review['user_id']
		_business_id = review['business_id']

		restaurant = restaurant_name(busid_to_restaurant[_business_id])
		rating = float(review['stars'])

		review = make_review(restaurant, rating)
		











