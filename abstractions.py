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

