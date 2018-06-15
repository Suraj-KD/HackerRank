from collections import Counter
Number_of_shoes = int(input())
List_of_shoe_size = Counter(input().strip().split(' '))
No_of_customer = int(input())
price = 0
for i in range(No_of_customer):
    value = input().strip().split(' ')
    if value[0] in List_of_shoe_size.keys() and List_of_shoe_size[value[0]] > 0:
        price += int(value[1])
        List_of_shoe_size[value[0]] -= 1
print(price)
