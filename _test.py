my_list = [1, 4, 1.23]
my_dict = {'k1' : 1, 'k2' : 2}
my_tuple = ('t', 'r', 'e')
my_set = set([1, 1])
my_set.add('s')
my_set.add('s')
num_list = my_list
print(my_list)
print(num_list)
for i in my_set:
    print(i)


if 1 in my_list:
    print("Found 1 in list")

# result = input('Enter a number: ')
#     print(result)

my_list = [key for key, value in my_dict.items()]
print(my_list)

my_list = [item**2 for item in range(20) if item%2 == 0]
print(my_list)
