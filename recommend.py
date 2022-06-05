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




def rate_all(user, restaurants, feature_fn):
	predictor = best_predictor(user, ALL_RESTAURANT, feature_fns)
	reviewed = user_reviews_restaurant(user, restaurants)

	return {restaurant_name(r): user_rating(user, restaurant_name(r)) if r in reviewed else predictor(r) for r in restaurant}



def search(query, restaurants):

	return [r for r in restaurants if query in restaurant_categories(r)]



def feature_set():
    """Return a sequence of feature functions."""
    return [lambda r: mean(restaurant_ratings(r)),
            restaurant_price,
            lambda r: len(restaurant_ratings(r)),
            lambda r: restaurant_location(r)[0],
            lambda r: restaurant_location(r)[1]]


@main
def main(*args):
    import argparse
    parser = argparse.ArgumentParser(
        description='Run Recommendations',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('-u', '--user', type=str, choices=USER_FILES,
                        default='test_user',
                        metavar='USER',
                        help='user file, e.g.\n' +
                        '{{{}}}'.format(','.join(sample(USER_FILES, 3))))
    parser.add_argument('-k', '--k', type=int, help='for k-means')
    parser.add_argument('-q', '--query', choices=CATEGORIES,
                        metavar='QUERY',
                        help='search for restaurants by category e.g.\n'
                        '{{{}}}'.format(','.join(sample(CATEGORIES, 3))))
    parser.add_argument('-p', '--predict', action='store_true',
                        help='predict ratings for all restaurants')
    parser.add_argument('-r', '--restaurants', action='store_true',
                        help='outputs a list of restaurant names')
    args = parser.parse_args()

    # Output a list of restaurant names
    if args.restaurants:
        print('Restaurant names:')
        for restaurant in sorted(ALL_RESTAURANTS, key=restaurant_name):
            print(repr(restaurant_name(restaurant)))
        exit(0)

    # Select restaurants using a category query
    if args.query:
        restaurants = search(args.query, ALL_RESTAURANTS)
    else:
        restaurants = ALL_RESTAURANTS

    # Load a user
    assert args.user, 'A --user is required to draw a map'
    user = load_user_file('{}.dat'.format(args.user))

    # Collect ratings
    if args.predict:
        ratings = rate_all(user, restaurants, feature_set())
    else:
        restaurants = user_reviewed_restaurants(user, restaurants)
        names = [restaurant_name(r) for r in restaurants]
        ratings = {name: user_rating(user, name) for name in names}

    # Draw the visualization
    if args.k:
        centroids = k_means(restaurants, min(args.k, len(restaurants)))
    else:
        centroids = [restaurant_location(r) for r in restaurants]
    draw_map(centroids, restaurants, ratings)















