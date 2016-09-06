from module_a import *


def override_print(any_object):
  try:
    print(any_object)
  except Error as e:
    print(e)


override_print(test1)
override_print(test2)
#override_print(test3)
override_print(class1)
override_print(class2)
