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

		