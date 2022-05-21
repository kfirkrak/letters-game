import random
from Dictionary import *

seven_cubes = [["א", "ח", "ל", "ע", "פ", "ת"],
               ["ד", "ז", "י", "ס", "צ", "ק"],
               ["א", "ג", "ט", "כ", "ס", "ק"],
               ["ב", "ה", "ה", "מ", "נ", "ש"],
               ["ב", "ה", "ו", "י", "י", "ר"],
               ["ד", "ח", "מ", "נ", "פ", "ש"],
               ["ג", "ו", "ל", "ע", "ר", "ת"]]

three_cubes = [["א", "ח", "ל", "ע", "פ", "ת"],
               ["ד", "ז", "י", "ס", "צ", "ק"],
               ["א", "ג", "ט", "כ", "ס", "ק"]]

four_letters = ["א", "ב", "ג", "ד"]

five_letters = ["א", "ב", "ג", "ד", "ה"]


def euclid_algo(num1, num2):
    large = max(num1, num2)
    small = min(num1, num2)
    c = large % small
    while c > 0:
        large = small
        small = c
        c = large % small
    return small


def roll_a_dice(num=7, on=False):
    if num != 7:
        cubes = three_cubes
    else:
        cubes = seven_cubes
    new = []
    for i in range(len(cubes)):
        num = random.randint(0, len(cubes[i]) - 1)
        new.append(cubes[i][num])
    if on:
        print("יצא בקוביות: " + ' '.join(new))
        print()
    return new


def subsets(roll):
    sub_sets = []
    for string in roll:
        add_list = [string]
        for item in sub_sets:
            add_list.append(item + string)
        sub_sets = sub_sets + add_list
    return sub_sets


def every_combination(lists):
    new_set = set()
    for item in lists:
        new_set.update(print_combi(item, ""))
    new_list = list(new_set)
    return (sorted(new_list, key=len))


def print_combi(word, pre):
    if len(word) == 0:
        new_set = set()
        new_set.add(pre)
        return new_set
    else:
        new_set = set()
        for i in range(len(word)):
            new_word = word[0:i] + word[i + 1:]
            new_set.update(print_combi(new_word, pre + word[i]))
        return new_set


def fix_word(word):
    if len(word) < 2:
        return word
    letter = word[-1]
    if letter == "צ":
        return word[:-1] + "ץ"
    if letter == "מ":
        return word[:-1] + "ם"
    if letter == "נ":
        return word[:-1] + "ן"
    if letter == "כ":
        return word[:-1] + "ך"
    if letter == "פ":
        return word[:-1] + "ף"
    return word


def print_words(words):
    dic = create_dic()
    i = 2
    j = 0
    for word in words:
        if word not in dic:
            continue
        if len(word) < 2:
            continue
        word = fix_word(word)
        if len(word) == i:
            j += 1
            print(word, end=" ")
            if j % 20 == 0:
                print()
        else:
            i += 1
            print()
            print()
            print(word, end=" ")


def load_words():
    with open('words_hebrew.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


roll = roll_a_dice(7, True)
subs = subsets(roll)
words = every_combination(subs)
print_words(words)
