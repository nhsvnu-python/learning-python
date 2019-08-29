a = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
flat_list = lambda x: [item for sublist in a for item in sublist]

print(flat_list)