
###АЛГОРИТМЫ СОРТИРОВКИ#######

##Сортировка  бульбашкою

##

# def bubble_sort(nums):
#     sorted = True
#     while sorted:
#         sorted = False
#         for i in range(len(nums)- 1):
#             if nums[i] > nums[i+1]:
#                 #swap elements
#                 nums[i], nums[i+1] = nums[i+1], nums[i]
#                 print(f"Compare: {nums[i]} > {nums[i+1]}: {nums}")
#                 sorted = True   
#             else:
#                 print(f"Compare: if {nums[i]} > {nums[i+1]}")

# ll = [5, 2, 1, 8, 4]
# print(ll)
#bubble_sort(ll)
#print(ll)

##Сортировка выборкой##

#O(n) # - лінійна складність

#O(log n) # - логарифмічна (бінарна) складність
#37
# range (0, 100)
# 50 - (100/2) <
# 25 - (50/2) >
#37
#O(n^2)# - Квадратична складність

# def selection_sort(nums):
#     for i in range(len(nums)):
#         lowest_index = i
#         print(f"Element - {i}")
#         #Loop for not sorted elements
#         for j in range(i+1, len(nums)):
#             print(f"Compare {nums[j]} < {nums[lowest_index]}")
#             if nums[j] < nums[lowest_index]:
#                 lowest_index = j
            
#         #Swap min and first element
#         nums[i], nums[lowest_index] = nums[lowest_index], nums[i]
#         print(nums)
#         print("*"*15)


# ll = [12, 8, 3, 20, 11]                
# selection_sort(ll)
# print(ll)

###Сортировка вставками

def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        #Зберігаємо посилання на індекс попереднього елемента
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert

ll = [9, 1, 15, 28, 6]
print(ll)
insertion_sort(ll)
print(ll)

