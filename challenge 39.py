import math

def generate_pythegorian_triplets(limit):
    triplets_array = [];
    c = 0;
    for a in range(3, limit // 3):
        for b in range(a + 1, limit):
            c = math.sqrt(math.pow(a, 2) + math.pow(b, 2));
            if c.is_integer() and a + b + c <= limit:
                triplets_array.append([a, b, int(c)]);
    return triplets_array

def get_triplet_sum(triplet):
    return triplet[0] + triplet[1] + triplet[2];

def get_number_of_solutions(triplets, p):
    number_of_solutions = 0;
    for triplet in triplets:
        if get_triplet_sum(triplet) == p:
            number_of_solutions += 1;
    return number_of_solutions;


def get_maximizing_p(limit):
    max_num_of_solutions = 0
    maximizing_p = 0
    n = 0
    triplets = generate_pythegorian_triplets(limit)
    for p in range(12, 1000):
        n = get_number_of_solutions(triplets, p) ;
        if n > max_num_of_solutions:
            max_num_of_solutions = n;
            maximizing_p = p;
    return maximizing_p;

print(get_maximizing_p(1000));
# print(generate_pythegorian_triplets(120));
# print(get_number_of_solutions(generate_pythegorian_triplets(120), 120));
