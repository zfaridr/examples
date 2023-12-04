def recursive_sum(array):
    global sum
    iterable = []
    for element in array:
        if hasattr(element, '__iter__') and not isinstance(element, str):
            iterable.append(element)
        elif type(element) in [int, float]:
            sum += element
    
    for elem in iterable:
        recursive_sum(elem)

array = [1, 4, (4, 3), [3, 8, 12, 'dfg', (2, 10), 4, 'wer'], {3, 8}]

sum = 0
recursive_sum(array)
print('sum_3')

def recursive_sum_2(*args, path=[]):
    total_sum = 0
    for index, arg in enumerate(args):
        if hasattr(arg, '__iter__') and not isinstance(arg, str):
            total_sum += recursive_sum_2(*arg, path=path + [index])
        elif isinstance(arg, (int, float)):
            total_sum += arg
        elif isinstance(arg, str):
            print(f"string '{arg}' on the", ''.join(f'[{n}]' for n in path+[index]))
    
    return total_sum

print(recursive_sum_2(*array))