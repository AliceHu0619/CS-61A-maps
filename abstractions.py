import re
from utils import mean


def make_review(restaurant_name, rating):
	return [restaurant_name, rating]


def make_restaurant_name(review):
	return review[0]



def review_rating(review):
	return review[1]


def make_user(name, reviews):
	return [name, {review_restaurant_name(r): r for r in reviews}]


def user_name(user):
	return user[0]


def user_review(user):
	return user[1]



def user_review_restaurant(user, restaurant):
	name = list(user_review(user))

	return [r for r in restaurant if restaurant_name(r) in names]


def user_rating(user, restaurant_name):
	reviewed_by_user = user_review(user)
	user_review = reviewed_by_user[restaurant_name]
	return review_rating(user_review)



def make_restaurant(name, location, categories, price, reviews):
	return [name, location, categories, price, reviews]


def restaurant_name(restaurant):
	return restaurant[0]



def restaurant_location(restaurant):
	return restaurant[1]


def restaurant_categories(restaurant):
	return restaurant[2]


def restaurant_price(restaurant):
	return restaurant[3]


def restaurant_ratings(restaurant):
	return [review_rating(r) for r in restaurant[4]]












