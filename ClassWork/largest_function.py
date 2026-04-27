def get_largest(alpha , beta, gamma):

    largest = alpha 

    if beta > largest:
        largest = beta

    if gamma > largest:
        largest = gamma

    return largest
    

user_input = print(get_largest(200,5,300))
