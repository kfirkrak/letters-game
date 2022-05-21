import random
from heb_dict import *
import matplotlib.pyplot as plt

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
    i = 2
    j = 0
    for word in words:
        if len(word) < 2:
            continue
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


def valid_words(words, dic=None, letters=None):
    if not dic:
        dic = create_dic()
    longest = 0
    n_words = []
    ALEPH = 1488
    if not letters:
        letters = [0] * 27
    for word in words:
        if word not in dic:
            continue
        size = len(word)
        if size < 2:
            continue
        if size > longest:
            longest = size
        for letter in word:
            letters[ord(letter) - ALEPH] += 1
        word = fix_word(word)
        n_words.append(word)
    return n_words, longest, letters


def analyze_game(times):
    ALEPH = 1488
    longest_word = [0] * 8
    arr_len = 27
    letters = [0] * arr_len
    heb_dic = create_dic()
    letters_dis = [0] * arr_len
    for i in range(times):
        roll = roll_a_dice(7, False)
        for letter in roll:
            letters[ord(letter) - ALEPH] += 1
        subs = subsets(roll)
        words = every_combination(subs)
        words, size, letters_dis = valid_words(words, heb_dic, letters_dis)
        longest_word[size] += 1
    n_letters = [[], []]
    for i in range(len(letters)):
        n_letters[0].append(chr(i + ALEPH))
        n_letters[1].append(letters[i])
    plot_results_longest_pie(longest_word[1:], times)
    plot_results_letters_dis_bar(letters_dis, times)


def plot_results_longest_pie(data, nums):
    length = ['', '', '', '4', '5', '6', '7']
    slices = data
    colors = ['b', 'm', 'c', 'r', 'y', 'g', 'b']
    plt.pie(slices, labels=length, colors=colors,
            startangle=90, shadow=True, explode=(0, 0, 0, 0, 0, 0, 0),
            radius=1.2, autopct='%1.1f%%')
    my_str = "Distribution of longest word for " + str(nums) + " rolls"
    plt.title(my_str, pad=20)
    plt.legend()
    plt.show()


def plot_results_longest_bar(data, nums):
    length = [i for i in range(1, 8)]
    fig = plt.figure(figsize=(10, 8))
    plt.bar(length, data, color='maroon', width=0.4)
    plt.xlabel("Length")
    plt.ylabel("Times")
    my_str = "Distribution of longest word for " + str(nums) + " rolls"
    plt.title(my_str)
    plt.show()


def plot_results_letters_dis_bar(data, nums):
    fig = plt.figure(figsize=(10, 8))
    heb = [chr(i) for i in range(1488, 1488 + 27)]
    plt.bar(heb, data, color='maroon', width=0.4)
    plt.xlabel("Letter")
    plt.ylabel("Times")
    my_str = "Distribution of Hebrew letters for " + str(nums) + " rolls"
    plt.title(my_str)
    plt.show()


def single_turn():
    roll = roll_a_dice(7, True)
    subs = subsets(roll)
    words = every_combination(subs)
    words, size, letters = valid_words(words)
    print_words(words)
    #plot_results_letters_dis_bar(letters, 1)


if __name__ == '__main__':
    single_turn()