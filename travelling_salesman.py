from time import clock
from collections import Counter
import matplotlib.pyplot as plt
import random
from itertools import permutations
alltours = permutations


def distance_tour(aTour):
    return sum(distance_points(aTour[i - 1], aTour[i]) for i in range(len(aTour)))


aCity = complex


def distance_points(first, second):
    return abs(first - second)


def generate_cities(number_of_cities):
    seed = 111
    width = 500
    height = 300

    random.seed((number_of_cities, seed))
    return frozenset(aCity(random.randint(1, width), random.randint(1, height)) for _ in range(number_of_cities))


def brute_force(cities):
    return shortest_tour(alltours(cities))


def shortest_tour(tours):
    return min(tours, key=distance_tour)


def visualize_tour(tour, style='bo-'):
    if len(tour) > 1000:
        plt.figure(figsize=(15, 10))
    start = tour[0:1]
    visualize_segment(tour + start, style)
    visualize_segment(start, 'rD')


def visualize_segment(segment, style='b0-'):
    plt.plot([x(c) for c in segment], [y(c) for c in segment], style, clip_on=False)
    plt.axis('scaled')
    plt.axis('off')


def x(city):
    return city.real


def y(city):
    return city.imag


def name(algorithm):
    return algorithm.__name__.replace('_tsp', '')


def tsp(algorithm, cities):
    t0 = clock()
    tour = algorithm(cities)
    t1 = clock()
    assert Counter(tour) == Counter(cities)
    visualize_tour(tour)
    print("{}: {} miast => długość trasy {:0f} (w {:.3f} sek)".format(
        name(algorithm), len(tour), distance_tour(tour), (t1 - t0)))


def greedy_algorithm(cities, start=None):
    c = start or first(cities)
    tour = [c]
    unvisited = set(cities - {c})
    while unvisited:
        c = nearest_neighbour(c, unvisited)
        tour.append(c)
        unvisited.remove(c)
    return tour


def first(collection):
    return next(iter(collection))


def nearest_neighbour(a, cities):
    return min(cities, key=lambda c: distance_points(c, a))


tsp(greedy_algorithm, generate_cities(2000))
