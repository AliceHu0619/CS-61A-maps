from abstractions import *
from data import ALL_RESTAURANT, CATEGORIES, USER_FILES, load_user_file
from ucb import main, trace, interact
from utils import distance, mean, zip, enumerate, sample
from visualize import draw_map


def find_closest(loction, centroids):

	>>>find_closest([3.0, 4.0],[[0.0, 0.0],[2.0,3.0],[4.0, 3.0],[5.0,5.0]])

	return min(centroids, key = lambda x : distance(loction,x))


def group_by_first(pairs):

	>>> example = [[1,2].[3,2],[2,4],[1,3],[3,1],[1,2]]
	>>> group_by_first(example)

	keys = []

	for key, _ in pairs:
		if key not in keys:
			keys.append(key)
	return [[y for x, y in paris if x == key] for key in keys]



def group_by_centroid(restaurants, centroids):
	pairs = [[find_closest(restaurants_location(r), centroids),r] for r in restaurants]
	return group_by_first(pairs)


def find_centroid(cluster):
	latitudes, longitudes = [], []
	for c in cluster:
		loc = restaurants_location(c)
		latitudes.append(loc[0])
		longitudes.append(loc[1])
	return [mean(latitudes), mean(longitudes)]


def k_means(restaurants, k, max_updates = 100):
	assert len(restaurants) >= k, 'Not enough restaurants to cluster'
	old_centroids, n = [], 0

	centroids = [restaurants_location(r) for r in sample(restaurants, k)]

	while old_centroids != centroids and n < max_updates:

		old_centroids = centroids
		pairs = group_by_centroid(restaurants, centroids)
		centroids = [find_centroid(l) for l in pairs]
		n += 1
	return centroids



def find_predictor(user, restaurants, feature_fn):
	reviews_by_user = {review_restaurant_name(review): review_rating(review) for review in user_reviews(user).values()}

	xs = [feature_fn(r) for r in restaurants]
	ys = [reviews_by_user[restaurant_name(r)] for r in restaurants] 

	x_mean = mean(xs)
	sxx = sum([(x - x_mean) ** 2 for x in xs])

	y_mean = mean(ys)
	syy = sum([(y - y_mean) ** 2 for y in ys])
	sxy = sum([(x - x_mean)*(y - y_mean) for x, y in zip(xs, ys)])

	b = sxy / sxx
	a = y_mean - b * x_mean
	r_squared = sxy * sxy / (sxx * syy)




	def predictor(restaurant):
		return b * feature_fn(restaurant) + a

	return predictor, r_squared





def best_predictor(user, restaurants, feature_fns):

	dt = {}
	for feature_fn in feature_fns:
		predictor, r_squared = find_predictor(user, reviewed, feature_fn)
		dt[predictor] = r_squared

	return max(dt, key = lambda x :dt[x])





















