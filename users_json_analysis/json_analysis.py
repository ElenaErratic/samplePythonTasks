from collections import Counter
import json


# f = open("C:/Users/Elena.Tikhomirova/Downloads/users.json")
f = open("users_json_analysis/datasets/users.json")
users_json = json.load(f)

# min number of properties in a set per user. Used for filtering users.
NUMBER = 2
# min number of neighbors a popular user must have. E.g. if more than five, then MEASURE equals 6.
MEASURE = 6


def filter_json(json_name):
    """Shorten the list of eligible users 10 times (10100 > 1089).
    Example result: neighbor_candidates = [{'properties': ['D', 'C'], 'id': 1}, {'properties': ['Y', 'A'], 'id': 2},
    {'properties': ['O', 'U', 'I', 'C'], 'id': 48}]"""

    neighbor_candidates = []
    for user in json_name:
        if len(user['properties']) >= NUMBER:
            neighbor_candidates.append(user)
    # print(len(neighbor_candidates))
    return neighbor_candidates


def extract_feature_lists(json_name):
    """
    Prepare lists for further analysis.
    :param: json_name is a reduced JSON with only users that have 2 or more properties.
    :return:
    1. neighbor_id_pairs [1, 2, 3, 7]
    2. common_property_sets: common properties per all user pairs.
    [('C', 'O'), ('I', 'U'), ('X', 'Z'), ('J', 'X'), ('M', 'U'), ('M', 'V'),
     ('G', 'M'), ('C', 'X'), ('M', 'U'), ('H', 'M'), ('M', 'V'), ('D', 'O'), ('X', 'Z'), ('C', 'O')]
    """
    common_property_sets = []  # common between a pair of users
    neighbor_id_pairs = []  # id pairs of users who have min 2 common properties >> to get the most popular users
    for user1 in json_name:
        for user2 in json_name:

            if user1 != user2:

                # take only users that have at least 2 properties in common
                user1_prop = set(user1['properties'])
                user2_prop = set(user2['properties'])
                # print(user1_prop)
                # print(user2_prop)
                intersecting_props = list(user1_prop.intersection(user2_prop))
                # print(f"intersection {intersecting_props}, {len(intersecting_props)}")
                if len(intersecting_props) >= NUMBER:
                    neighbor_id_pairs.append(user1['id'])  # can append both items at once to get a nested []
                    neighbor_id_pairs.append(user2['id'])

                    '''Iterate to get pairs from intersecting sets and sort items in the resulting pairs
                     in alphabetical order so that identical pairs can be detected and the top pair returned in the 
                     required alphabetical order.'''
                    property_pairs = [(a, b) if a < b else (b, a) for idx, a in enumerate(intersecting_props)
                                      for b in intersecting_props[idx + 1:]]

                    common_property_sets.append(property_pairs)
                    # print(f"common_property_sets = {common_property_sets}")
                    # print(f"neighbor_id_pairs = {neighbor_id_pairs}")

    # flatten the list from nesting_level = 2 to 1
    common_property_sets = [item for sublist in common_property_sets for item in sublist]

    # print(f"final common_property_sets = {common_property_sets}")
    # todo: deduplicate common_property_sets and neighbor_id_pairs
    # todo remove print's

    return neighbor_id_pairs, common_property_sets


def rank_prop_pairs(list_name):
    """
    Count unique pairs of properties from the list of such pairs.
    :param: list_name: Take a list of property pairs common between user pairs (`common_property_sets`).
    :return: Return the most popular pair of values from all input sublists.
    Example: ('Y', 'A') > 'Y', 'A'
    """

    # Now the input list is duplicated, therefore // 2
    most_common_pair, num_most_common = Counter(list_name).most_common(1)[0]
    # most_common_pair = ','.join(map(str, most_common_pair))  # G,M
    # num_most_common //= 2
    print(f"most_common_pair: {most_common_pair}")
    # answer 3.2 ('G', 'M')
    return most_common_pair


def find_popular_users(list_name):
    """
    Find users who have more than 5 neighbors.
    The number of user occurrences in the list equals the number of matches/neighbors.
    :param: list_name = neighbor_id_pairs
    :return: the number of users that have > 5 matches.
    `.count(x) // 2` because the list is duplicated
    """

    # popular_users example: [[2225, 66], [4274, 34]] format: [[user_id, matches]]

    popular_users = [[x, list_name.count(x) // 2]
                     for x in set(list_name)
                     if list_name.count(x) // 2 >= MEASURE]
    # alt = Counter(list_name)
    # print(popular_users)
    popular_users_number = len(popular_users)
    print(f"popular_users_number: {popular_users_number}")
    '''answer 3.1 = 1088
    (popular_users has 1088 users, which equals len(neighbor_candidates) - 1: as a result of pre-filtering, 
    neighbor_candidates does not include users without a neighbor. in fact all users except id 4513 
    have >= 6 neighbors (MEASURE)
    Proof: bottom of popular_users [... 4316: 6, 2536: 6, 4513: 5]
    ''' 

    return popular_users_number


neighbor_candidates = filter_json(users_json)
neighbor_id_pairs, common_property_sets = extract_feature_lists(neighbor_candidates)
most_common_pair = rank_prop_pairs(common_property_sets)
popular_users_number = find_popular_users(neighbor_id_pairs)


# task 4
class User:
    def __init__(self, json_name):
        self.json_name = json_name


    def find_friends(self, query_user_prop):
        """
        :param: ['Y', 'E', 'S']
        :return: ids of  7  most similar users sorted by similarity desc. similarity > 0. or returns []"""

        friends = {}
        for user1 in self.json_name:

            user1_prop = set(user1['properties'])
            user2_prop = set(query_user_prop)
            similarity = len(user1_prop.intersection(user2_prop)) / len(user1_prop.union(user2_prop))


            if similarity > 0:
                friends.update({user1['id']: similarity})

        most_similar_users = []
        if bool(friends):
            user_ids_with_similarity = Counter(friends).most_common(7)  # a list of tuples
            for k, v in user_ids_with_similarity:
                most_similar_users.append(k)
 
            
        # print(most_similar_users)
        return most_similar_users  # todo check

query_user_prop = ['F', 'G', 'M']
user_instance = User(users_json)
user_instance.find_friends(query_user_prop)
