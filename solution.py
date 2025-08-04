#  Search target number, according to requirements.
def solution(A):
    
    #  VARIABLES.
    iList = A
    number_searched = 1 #  Default result.
    condition_assumption_1 = False
    condition_assumption_2 = False

    #  OPERATIONS.
    #  Assumptions validation; both must be 'True', for function to search the target number.
    #  Assumption 1:
    if len(iList) <= 100000 : condition_assumption_1 = True
    #  Assumption 2:
    min_iList = min(iList)
    max_iList = max(iList)
    if ((min_iList >= -1000000) and (max_iList <= 1000000)) : condition_assumption_2 = True

    #  If all conditions are 'True', searches the target number.
    if all([condition_assumption_1, condition_assumption_2]):
        
        #  Gets list of uniques (converting to a 'set'), and then gets a copy sorted.
        list_uniques = list(set(iList))
        list_sorted_uniques = sorted(list_uniques)

        # Traverse clean list to validate number searching.
        for i in range(1, len(list_sorted_uniques)):
            if ((list_sorted_uniques[i] - list_sorted_uniques[i - 1]) == 1):
                number_searched = list_sorted_uniques[i] + 1
            else:
                number_searched = list_sorted_uniques[i - 1] + 1
                break
        
        # Compares number found so far vs. smallest positive integer (greater than 0).
        number_searched = max(1, number_searched)

    return number_searched
