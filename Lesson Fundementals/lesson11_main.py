# What is main()?
#   main() is a procedure that holds your whole program's plan.
#   It runs the steps in order: get input, call your procedure,
#   show output. The last line of the file, main(), starts it.
#   The name "main" isn't required by Python, but programmers use
#   it so anyone can find where the program begins.

# Top-down design:
#   Start with the big picture (the TOP), then fill in the
#   details (the BOTTOM). Like writing an essay outline before
#   the paragraphs.
#     TOP    = main(): the steps your program follows, in order.
#     BOTTOM = your procedure: the detailed algorithm for one step.
#   Don't start with the algorithm! Plan main() first, so you
#   know exactly what your procedure needs to do.

# ---------- DATA ----------
# A list stores many values under one name.
# Replace this list with YOUR data.
# What group of things does your program use?
my_list=["apple", "banana", "cherry", "grape", "mango", "orange"]

def my_procedure(word):
    # 1. Check the input. Keep asking if it's not a string or it's blank.
    type(word)




def main():
    #put code here
    print("Hi welcome to my program :)")
    word= input("Type a word:")
    
    my_procedure(word)


main()