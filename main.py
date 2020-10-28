"""
3. Implement a direct infix evaluator that combines the functionality of infix-to-postfix conversion and the
  postfix evaluation algorithm. Your evaluator should process infix tokens from left to right and use two stacks,
  one for operators and one for operands, to perform the evaluation.
10.Implement a radix sorting machine. A radix sort
  for base 10 integers is a mechanical sorting technique that utilizes a collection of bins, one main bin and 10 digit
  bins. Each bin acts like a queue and maintains its values in the order that they arrive. The algorithm begins by
  placing each number in the main bin. Then it considers each value digit by digit. The first value is removed and
  placed in a digit bin corresponding to the digit being considered. For example, if the ones digit is being
  considered, 534 is placed in digit bin 4 and 667 is placed in digit bin 7. Once all the values are placed in the
  corresponding digit bins, the values are collected from bin 0 to bin 9 and placed back in the main bin. The process
  continues with the tens digit, the hundreds, and so on. After the last digit is processed, the main bin contains the
  values in order.
27.The linked list implementation given above is called a singly linked list because each node has a single reference
  to the next node in sequence. An alternative implementation is known as a doubly linked list. In this implementation,
  each node has a reference to the next node (commonly called next) as well as a reference to the preceding node (
  commonly called back). The head reference also contains two references, one to the first node in the linked list and
  one to the last. Code this implementation in Python.
"""
import prob_3 as a
import prob_10 as b


def main():
    print("")
    print("3. Direct infix evaluator ")
    print(f" 5 + 3 * ( 2 - 1 ) = {a.infix_eval('5 + 3 * ( 2 - 1 )')}")
    print(f" 5 + 3 * ( 0 - 1 ) = {a.infix_eval('5 + 3 * ( 0 - 1 )')}")
    print(f" 9 + 3 * ( 2 - 1 ) = {a.infix_eval('9 + 3 * ( 2 - 1 )')}")


    print("")
    print("10. ")

    print("")
    print("27. ")


if __name__ == '__main__':
    main()
