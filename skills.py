"""Skills Assessment: Lists

Edit the function bodies until all of the doctests pass when you run this file.
"""


def print_list(my_list):
    """Print each item in the input list

        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9

    """
# As the loop goes through each item in the list,
# it will print that specific item.
# Run time is o(n) linear
    for item in my_list:

        print item


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """

    new_list = []  # Create an empty list

    # assume all items in the list are numbers
    # to avoid the numbers that are strings
    for item in number_list:  # ctypecast all the items in the list into an int.
        item = int(item)

        if item % 2 != 0:  # if the remainder of the item/2 is NOT 0, then append it to the new list.
            new_list.append(item)

    return new_list


def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """

    new_list = []  # Create an empty list
    # assume all items in the list are numbers
    # to avoid the numbers that are strings
    for item in number_list:  # typecast all the items in the list into an int.
        item = int(item)

        if item % 2 == 0:  # if the remainder of the item/2 IS 0, then append it to the new list.
                new_list.append(item)
    return new_list


def every_other_item(my_list):
    """Return a list that contains every other item in my_list starting
       with the first item.

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(["you", "friend", "are", "very", "good", " ", "at", " ", "coding"])
       ['you', 'are', 'good', 'at', 'coding']

    """
    return my_list[0::2]
    # [starts:stop:steps]. It will return every other starting from [0], which is the very beginning, then until the very end (empty between colons).


def print_indexes(my_list):
    """Print the index of each item in the input_list, followed by the item itself.

    Do this without using a counting variable---that is, don't do something
    like this:

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this:

        >>> print_indexes(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

    """
    for item in my_list:
        index_item = str(my_list.index(item)) + " " + str(item)
        # type cast the index number and the item, then concatinate the index number, the space within a str and the item.
        print index_item


def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """
    long_words_list = []
    for item in word_list:
        if len(item) > 4:
        #len method will count the number of characters that the item has. If it is greater than 4, that item will be appended to the long_word_list.
            long_words_list.append(item)
    return long_words_list


def n_long_words(word_list, n):
    """Return all words in input list that are longer than n characters.

    >>> n_long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"], 3)
    ['hello', 'spam', 'spam', 'bacon', 'bacon']

    >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
    ['apples', 'bananas']
    """

    n_long_words_list = []
    for item in word_list:
        if len(item) > n:
        #len method will count the number of characters that the item has. If it is greater than n, that item will be appended to the n_long_word_list.
            n_long_words_list.append(item)

    return n_long_words_list


def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

    DO NOT USE the built-in function `min`!

        >>> smallest_int([-5, 2, -5, 7])
        -5


        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return None:


        >>> smallest_int([]) is None
        True

    """

    # # option A:
    # for num1 in number_list:
    #     for num2 in number_list:

    #         if num2 < num1:
    #             return num2

    # option B:

    smallest = None

    for num in number_list:
        if smallest is None or num < smallest:
            smallest = num
    return smallest


def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

    DO NOT USE the built-in function `max`!

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """

    largest = None

    for num in number_list:
        if largest is None or num > largest:
            largest = num
    return largest

def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """
    halvesies_list = []
    #Create an empty list
    for item in number_list:
        item = float(item)
        # type cast all items into a float
        halvesies = item/2
        # divide each item by 2, them append it to the halvesies_list empty list.
        halvesies_list.append(halvesies)
    return halvesies_list


def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """
    word_lengths_list = []  # Create an empty list
    for item in word_list:
        item = str(item)  # type cast each item on the list into a str
        item_length = len(item)  # find the length of each str (len() built-in fn only works with str)
        word_lengths_list.append(item_length)  # add each length value to the empty list.
    return word_lengths_list


def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """
    total = 0  # set the initial conditions, so total is 0
    for item in number_list:
        item = int(item)  # tycast all numbers to float in case there is an int or str.
        total += item  # this means total = total + item

    return total


def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """
    total = 1  # set initial conditions to 1 because if set to 0, total will be always 0.

    for item in number_list:
        try:  # check if all items in the list are numbers.
            item = int(item)  # tycast all numbers to float in case there is an int or str.
            total = total * item  # means: total = the previous total multiply by the next item on the list.
        except ValueError:
            print "Oops! %s is not a number..." % item

    return total


def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python has a built-in method on lists, `join`---but for this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """

    joined_string_results = ""  # initials conditions: empty str.
    for string in word_list:
        string = str(string)  # type cast string in word_list to a str.
        joined_string_results = joined_string_results + string  # means: joined_string_results = concatinate previous joined_string_results with the next string.
    return joined_string_results


def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """

    total = 0  # set initial conditions starting from 0
    for number in number_list:
        try:  # check that all items in the list are numbers
            number = float(number)  # type cast the number into a float
            total += number  # means: total = previous total + the next number int he list.
            average = total / len(number_list)  # the built-in fn. len() counts the total number of items in a list.
        except ValueError:
            print "Oops! %s number is not a number..." % number
    return average


def join_strings_with_comma(list_of_words):
    """Return ['list', 'of', 'words'] like "list, of, words".

        >>> join_strings_with_comma(["Labrador", "Poodle", "French Bulldog"])
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course:

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'

    """
    joined_string_results = ""

    for string in list_of_words:
        string = str(string)
        if len(list_of_words) == 1:  # if there is only one item in the list return only the that item.
            joined_string_results = string + ", "
        else:
            joined_string_results = joined_string_results + string + ", "

    return joined_string_results[:-2]  # A whole set of string is returned ei. "hello, bacon, cake, case, " To get rid of the extra "," and " " at the end of the string. It has been asked to return from the beginning of the string until [-3]. NOTE: [-2]is not included, it is where it stops returning.


def foods_in_common(foods1, foods2):
    """Using ANY Python data structure presented in the last week, given 2 lists of foods,
    return a set of items that are in common between the two. (Don't include any duplicates
    in the output collection.)

    For example:

    >>> foods_in_common(["cheese", "bagel", "cake"], ["hummus", "beets", "bagel", "lentils"])
    set(['bagel'])

    If there are no foods in common, return an empty set.

    >>> foods_in_common(["lamb", "chili", "cheese"], ["cake", "ice cream"])
    set([])

    """

    in_common = []

    for food1 in foods1:
        for food2 in foods2:
            if food2 in food1:
                in_common.append(food2)

    return set(in_common)


def reverse_list(my_list):
    """Return the inputted list, reversed.

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

    Do not use the python methed reverse()/reversed().

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

    """
    list_reversed = my_list[::-1]
    return list_reversed


def reverse_list_in_place(my_list):
    """Return the inputted list reversed--WITHOUT creating a new list.
       This will involve moving the items in my_list to different positions
       in the same list.

       Do not use the python methed reverse()/reversed()

        >>> reverse_list_in_place([1, 2, 3])
        [3, 2, 1]

        >>> reverse_list_in_place(["cookies", "love", "I"])
        ['I', 'love', 'cookies']


    """
    unreverse_list = my_list[::-1]
    return unreverse_list


def duplicates(my_list):
    """Return a list of words which are duplicated in the input list.
       The returned list should be in ascending order.

    >>> duplicates(["apple", "apple", "banana", "cherry", "banana", "apple"])
    ['apple', 'banana']

    >>> duplicates([1, 2, 2, 4, 4, 4, 7])
    [2, 4]


    """
    # duplicates = []
    # for item1 in my_list:
    #     for item2 in my_list:
    #         if item2 not in duplicates & in item1:
    #             duplicates.append(item2)


    # return duplicates

    pass


def find_letter_indices(list_of_words, letter):
    """Given a list of words and a letter, return a list of integers that correspond
    to the index of the first occurance of the letter in that word.

    Do not use the .index() list method.

    >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
    [0, 1, 2]

    If the letter doesn't occur in one of the words, use None for that word in
    the output list. For example:

    >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
    [0, 1, 2, None]

    """

    #How to find out the index location of a letter in a string?

    # index_list = []

    # for word in list_of_words:
    #     if letter in word:
    #         index_list.append(word[letter])

    # return index_list

    pass


def largest_n_items(input_list, n):
    """Given a list of integers along with an integer n, return a
    list of the largest n numbers in the input list in ascending order.

    You can assume that n will be less than the length of the list.

    For example:

    >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
    [59, 700, 6006]

    """

    input_list = sorted(input_list)

    if n == 0:
        return []
    else:
        return input_list[-n:]


##############################################################################
# END OF ASSIGNMENT: You can ignore everything below.
if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
