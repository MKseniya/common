class Hometask(self):
    a =[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b =[1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    def common_numbers():
        c = set(a) & set(b)
        new_list = []
        for num in c:
            new_list.append(num)
        print(new_list)

    common_numbers()
