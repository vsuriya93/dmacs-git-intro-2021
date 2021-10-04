from dmacs_utils import LinkedList, Stack, Sort, Tree
import random

# Group 1


def test_linkedlist():
    """
    Implement the following functions (use the exact names)

    1. insert
    2. delete
    3. sort
    4. reverse
    5. get_as_python_list

    mylist = LinkedList()  # to implement
    test_val = list(range(10**6))

    # Test 1
    for i in test_val:
        mylist.insert(i)
    assert(test_val == mylist.get_as_python_list())

    # Test 2
    mylist.reverse()
    assert(test_val[::-1] == mylist.get_as_python_list())

    # Test 3
    for i in random.shuffle(range(10**6)):
        mylist.delete(i)

    assert(mylist.get_as_python_list() == [])
    assert(mylist.head == None)

    # Test 4
    mylist = LinkedList()
    for i in random.shuffle(range(10**6)):
        mylist.insert(i)

    mylist.sort()
    assert(sorted(test_val) == mylist.get_as_python_list())

    < write code for testing other functions >
    """

    pass


# Group 2

def test_arrsort():
    """

    Implement the following sorting algorithms

    1. Bubble Sort
    2. Insertion Sort
    3. Selection
    4. Merge Sort
    5. Quick Sort

    my_sorter = Sort()

    my_list = random.shuffle(range(10**6))
    obj_sorted = my_sorter.merge_sort(my_list)

    .
    .
    .
    .
    .

    < write code for testing other functions >
    """
    pass

# Group 3


def test_tree():
    """

    implement binary tree

    1. insert
    2. search
    3. inorder
    4. preorder
    5. postorder

    my_tree = Tree()

    for i in range(10**6):
        my_tree.insert()
    .
    .
    .
    .
    .

    < write code for testing other functions >

    """

    pass

# Group 4


def test_stack():
    """
    implement stack (dont use python list - please implement as a LinkedList with push and pop at the head of the list)

    1. Push/Pop operations
    2. Given a string - use the above built stack to solve Valid Parenthesis (https://leetcode.com/problems/valid-parentheses/) using this data structure


    my_stack = Stack()
    for i in range(10**6):
        my_stack.push()

    < write code for testing other functions >
    .
    .
    .
    .
    """

    def valid_parenthesis(str_: str) -> str:
        return None

    # add more cases
    for test_str, exp_result in zip(["(((", "()()()", "))))"], [False, True,  False]):
        pass
        # assert(valid_parenthesis(test_str) == exp_result)
