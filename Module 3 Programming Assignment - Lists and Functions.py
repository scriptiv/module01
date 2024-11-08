# 7.4
things = ["mozzarella", "cinderella", "salmonella"]
print("Initial list:", things)

# 7.5
things[1] = things[1].capitalize()
print("After capitalizing 'cinderella':", things)

# 7.6
things[0] = things[0].upper()
print("After making 'mozzarella' uppercase:", things)

# 9.1
def good():
    return ["Harry", "Ron", "Hermione"]

print("Good function output:", good())

# 9.2
def get_odds():
    for num in range(10):
        if num % 2 != 0:
            yield num

count = 0
for odd in get_odds():
    count += 1
    if count == 3:
        print("Third odd number:", odd)
        break