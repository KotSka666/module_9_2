first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

result_1 = [len(i) for i in first_strings if len(i) >= 5]
print(result_1)

result_2 = [(i, j) for i in first_strings for j in second_strings if len(i) == len(j)]
print(result_2)

result_3 = {i: len(i) for i in first_strings + second_strings if len(i) % 2 == 0}
print(result_3)