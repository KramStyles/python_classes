class SuperList(list):
    def __len__(self) -> int:
        return 1000


list1 = SuperList()
list1.append(5)

print(len(list1))