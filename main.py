from typing import List
# Skeleton code for even_list
def even_list(int_list: List[int]) -> List[int]:
    return_list = []
    for i in int_list:
        if i%2==0:
           return_list.append(i)
    return return_list

# Skeleton code for sum_of_squares_of_even
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    return_int = 0
    for i in even_int_list:
        return_int += (i**2)
    return return_int


def main():
# Example list
    int_list = [58,6,-22,91,33,49,44,63,-79,12]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)

if __name__ == "__main__":
    main()