#  Code that ALWAYS get executed; either main, or imported as module from other script.
# print(__name__)

#  VARIABLES DECLARATION.

#  FUNCTIONS DECLARATION.

#  Get lists from input file.
def getLists(iFileName):
    print(f"LOG/LOAD: getting lists of numbers from '{iFileName}'.")
    
    #  VARIABLES.
    list_lists = []

    #  OPERATIONS.
    input_file = open(iFileName, 'r')
    for input_line_str in input_file.readlines():
        input_line_str_clean = input_line_str.strip().replace(' ', '')
        input_list_str = input_line_str_clean.split(',')
        input_list = list(map(int, input_list_str))
        list_lists.append(input_list)
    input_file.close()
    
    #  OUTPUT.
    print(f"LOG/LOAD: {len(list_lists)} lists of numbers imported, from '{iFileName}'.")
    return list_lists

#  Search target number, according to requirements.
def solution(A):
    print(f"LOG/SEARCHING: looking for target number on list '{A}'.")
    
    #  VARIABLES.
    iList = A
    number_searched = None
    condition_assumption_1 = False
    condition_assumption_2 = False

    #  OPERATIONS.
    #  AssumptionS validation; both must be 'True', for function to return a number.
    #  Assumption 1:
    if len(iList) <= 100000 : condition_assumption_1 = True
    #  Assumption 2:
    min_iList = min(iList)
    max_iList = max(iList)
    if ((min_iList >= -1000000) and (max_iList <= 1000000)) : condition_assumption_2 = True

    #  If all conditions are 'True', searches the number; otherwise returns default value of 'None'.
    if all([condition_assumption_1, condition_assumption_2]):
        
        #  Gets list of uniques (converting to a 'set'), and then gets a copy sorted.
        list_uniques = list(set(iList))
        list_sorted_uniques = sorted(list_uniques)

        # Traverse clean list to validate number searching.
        for i in range(1, len(list_sorted_uniques)):
            # print(f'i: {i} | lower number: {list_sorted_uniques[i - 1]} | upper number: {list_sorted_uniques[i]}')
            if ((list_sorted_uniques[i] - list_sorted_uniques[i - 1]) == 1):
                number_searched = list_sorted_uniques[i] + 1
            else:
                number_searched = list_sorted_uniques[i - 1] + 1
                break
        
        # Compares number found so far vs. smallest positive integer (greater than 0).
        number_searched = max(1, number_searched)

    if number_searched is not None:
        print(f"LOG/SEARCHING: target number found is '{number_searched}' on list '{A}'.")
    else:
        print(f"LOG/SEARCHING: target number not found, since assumptions weren't met.")
    return number_searched

#  'main' function, to execute ONLY if direct execution of script.
def main():
    # print('Hello World')

    #  VARIABLES DECLARATION.
    INPUT_FILENAME = 'test-input-vDev.txt'

    #  CODE EXECUTION.
    
    #  Get lists of numbers.
    list_lists = getLists(INPUT_FILENAME)

    #  Search numbers for each list of numbers.
    for list_item in list_lists:
        solution(list_item)

#  CODE EXECUTION.

#  Code executed ONLY when script is called directly; NOT IMPORTED from other script.
if __name__ == '__main__':
    main()
