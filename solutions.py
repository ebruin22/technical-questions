
import collections

# Question 1
# Given two strings s and t, determine whether
# some anagram of t is a substring of s.
# For example: if s = "udacity" and t = "ad",
# then the function returns True.
# Your function definition should look like:
# question1(s, t) and return a boolean True or False.


def question1(s, t):
    # check that t and s are not empty
    if (t == "" or None) or (s == "" or None):
        return False
    # check that len(s) is not less than len(t)
    elif len(t) > len(s):
        return False
    else:
        # create list of each string
        s_list = list(s)
        t_list = list(t)
        # count how many times each letter appears in each string using Counter
        s_count = collections.Counter(s_list)
        t_count = collections.Counter(t_list)
        # loop through t string and check if a letter
        # appears more than it appears in s,
        # then return false because not an anagram.
        # Then check is a letter has the same count in each
        # string and if so add one to counter.
        # At the end of the loop, return whether
        # count is equal to the number of
        # letters in t which means all letters
        # exist in the s and so t can be an anagram subset of s.
        counter = 0
        for t_letter in t_list:
            if t_count[t_letter] > s_count[t_letter]:
                return False
            elif t_count[t_letter] == s_count[t_letter]:
                counter += 1
        return counter == len(t_list)


def test1():
    print("-------------------------------------------------------")
    print("Question 1 Testing")
    print("Test 1: question1(udacity, empty string)")
    print("Result: ", question1("udacity", ""))
    print("Test 2: question1(empty string, empty string)")
    print("Result: ", question1("", ""))
    print ("Test 3: question1(dessert, esse)")
    print("Result: ", question1("dessert", "esse"))
    print("Test 4: question1(anna, and)")
    print("Result: ", question1("anna", "and"))


# Question 2
# Given a string a, find the longest palindromic
# substring contained in a.
# Your function definition should look like question2(a),
# and return a string.


def question2(a):
    if a != '' or None:
        a_input = a.replace(" ", "")
        a_length = len(a_input)
        longest_str = 0
        first = 0
        last = 0
        # need to slice string and test for palindrome
        for i in range(0, a_length):
            for j in range(i + 1, a_length + 1):
                sub_str = a_input[i:j]
                if (sub_str == sub_str[::-1]) and len(sub_str) > longest_str:
                    longest_str = len(sub_str)
                    first = i
                    last = j
        result = a_input[first:last]
        return result
    else:
        return "Your input cannot be empty"


def test2():
    print("-------------------------------------------------------")
    print("Question 2 Testing")
    print("Test 1: question2(dessert)")
    print("Longest palindrome: ", question2("dessert"))
    print("Test 2: question2(empty string)")
    print("Longest palindrome: ", question2(""))
    print("Test 3: question2(apple)")
    print("Longest palindrome: ", question2("apple"))


# Question 3
# Given two strings s and t, determine
# whether some anagram of t is a substring of s.
# For example: if s = "udacity" and t = "ad",
# then the function returns True.
# Your function definition should look like:
# question1(s, t) and return a boolean True or False.


def question3(G):
    # G must have at least 2 vertices to test edges
    if len(G) < 2:
        return "G doesn't contain enough vertices to form edges"

    # get a set of vertices (keys of the input dictionary)
    v = G.keys()

    # create an empty set
    edges = set()
    # loop through vertices' keys
    for i in v:
        # loop through adjacency list in each key's value pair
        for j in G[i]:
            if i > j[0]:
                edges.add((j[1], j[0], i))
            elif i < j[0]:
                edges.add((j[1], i, j[0]))

    # sort edges by weight
    edges = sorted(list(edges))

    # loop through edges and store non-cycle edges
    smallest_edges = []
    v = [set(i) for i in v]
    for i in edges:
        # get indices of both vertices
        for j in range(len(v)):
            if i[1] in v[j]:
                i1 = j
            if i[2] in v[j]:
                i2 = j

        # store union in the smaller index and pop the larger index
        # also store the edge in smallest_edges
        if i1 < i2:
            v[i1] = set.union(v[i1], v[i2])
            v.pop(i2)
            smallest_edges.append(i)
        if i1 > i2:
            v[i2] = set.union(v[i1], v[i2])
            v.pop(i1)
            smallest_edges.append(i)

        # terminate early when all vertices are in one graph
        if len(v) == 1:
            break

    # return min tree graph from smallest_edges array
    min_tree = {}
    for i in smallest_edges:
        if i[1] in min_tree:
            min_tree[i[1]].append((i[2], i[0]))
        else:
            min_tree[i[1]] = [(i[2], i[0])]

        if i[2] in min_tree:
            min_tree[i[2]].append((i[1], i[0]))
        else:
            min_tree[i[2]] = [(i[1], i[0])]
    return min_tree


def test3():
    print("-------------------------------------------------------")
    print("Question 3 Testing")
    G = {'A': [('B', 2)],
         'B': [('A', 2), ('C', 5)],
         'C': [('B', 5)]}
    print("G's min tree is: ")
    print(question3(G))
    A = {'A': [('B', 7), ('D', 5)],
         'B': [('A', 7), ('C', 8), ('D', 9), ('E', 7)],
         'C': [('B', 8), ('E', 5)],
         'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],
         'E': [('B', 7), ('C', 5), ('D', 15), ('F', 8), ('G', 9)],
         'F': [('D', 6), ('E', 8), ('G', 11)],
         'G': [('E', 9), ('F', 11)]}
    print("A's min tree is: ")
    print(question3(A))
    H = {'A': [('D', 5), ('B', 7)],
         'B': [('A', 7), ('E', 7)],
         'C': [('E', 5)],
         'D': [('A', 5), ('F', 6)],
         'E': [('C', 5), ('B', 7), ('G', 9)],
         'F': [('D', 6)],
         'G': [('E', 9)]}
    print("H's min tree is: ")
    print(question3(H))


# Question 4
# Objective:  Find the lowest node in the
# tree T taht has both n1 and n2 as descendants.
# Process: Use recursion to check if root is the
# lowest common ancestor by testing if nodes to
# left and right are larger than root


def question4(T, r, n1, n2):
    # Check if root has two children on right and left
    # if Yes, then return r since n1 and n2 have r as common ancestor
    if (n1 > r and n2 < r) or (n1 < r and n2 > r):
        return r
    # check if both n1 and n2 are smaller than root w
    # r is not root and must check if left node is root
    elif (n1 < r and n2 < r):
        # if Yes, get position of left child node
        left = T[r].index(1)
        # checks if n1 or n2 equals the left node
        if n1 == left or n2 == left:
            return r
        # otherwise left node become root
        # and continue checking using recursion
        else:
            r = left
    # checks if both n1 and n2 are greater than root
    # r is not root and so much check if right node is root
    elif (n1 > r and n2 > r):
        # get position of right child node
        right = len(T[r]) - T[r][::-1].index(1) - 1
        # checks if n1 or n2 equals right child of root
        if n1 == right or n2 == right:
            return r
        else:
            # change root to right child
            r = right

    # return to top of function using updated root
    return question4(T, r, n1, n2)


def test4():
    tree = [
                [
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0]
                ],
                [
                    [0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1]
                ],
                [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            ]
    print("-------------------------------------------------------")
    print("Question 4 Testing")
    print("Test 1:", "Pass" if 1 == question4(tree[1], 3, 0, 2) else "Fail")
    print("Test 2:", "Pass" if 3 == question4(tree[0], 3, 1, 4) else "Fail")
    print("Test 3:", "Pass" if 3 == question4(tree[2], 6, 1, 4) else "Fail")


# Question 5
# Find the element in a singly linked list that's m elements
# from the end.
# For example, if a linked list has 5 elements,
# the 3rd element from the end is the 3rd element.
# The function definition should look like question5(ll, m),
# where ll is the first node of a linked list and
# m is the "mth number from the end".
# You should copy/paste the Node class
# below to use as a representation of a
# node in the linked list
# Return the value of the node at that position.


head = None


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    # Insert node at the beginning of linked list
    def push(data):
        global head
        new_node = Node(data)
        new_node.next = head
        head = new_node

    def question5(ll, m):
        main = ll
        ptr = ll
        count = 0

        if(ll is not None):
            while (count < m):
                if ptr is None:
                    print ("Error, m does not exist")
                    return
                ptr = ptr.next
                count += 1

        while(ptr is not None):
            main = main.next
            ptr = ptr.next

        return main.data


def test5():
    Node.push(0)
    Node.push(1)
    Node.push(2)
    Node.push(3)
    Node.push(4)
    Node.push(5)
    Node.push(6)

    print("-------------------------------------------------------")
    print("Question 5 Testing")
    print("Test 1: question5(head, 4):")
    print("Pass" if Node.question5(head, 4) == 3 else "Fail")
    print("Test 2: question5(head, 15):")
    print("Pass" if Node.question5(head, 15) is None else "Fail")
    print("Test 3: question5(head, 1):")
    print("Pass" if Node.question5(head, 5) == 2 else "Fail")


# run tests
test1()
test2()
test3()
test4()
test5()
