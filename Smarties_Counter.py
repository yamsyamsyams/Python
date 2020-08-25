import random


def generate_list():
    new_list = []
    colours = ["red", "green", "blue", "yellow", "orange", "brown"]
    for i in range(0, 41):
        smartie_colour = colours[random.randint(0, 5)]
        new_list.append(smartie_colour)
    return new_list


def count_smarties(smarties):
    red = 0
    green = 0
    blue = 0
    yellow = 0
    orange = 0
    brown = 0
    for j in smarties:
        if j == "red":
            red += 1
        elif j == "green":
            green += 1
        elif j == "blue":
            blue += 1
        elif j == "yellow":
            yellow += 1
        elif j == "orange":
            orange += 1
        else:
            brown += 1
    my_string = "red: %s green: %s blue: %s yellow: %s orange: %s brown: %s" % (red, green, blue, yellow, orange, brown)
    return my_string


if __name__ == '__main__':
    smarties = generate_list()
    print(count_smarties(smarties))
