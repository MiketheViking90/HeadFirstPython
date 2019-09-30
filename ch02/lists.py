prices = []

temps = [32.0, 212.0, 81.6]

words = ["hello", "world"]

car_details = ["Toyota", "RAV4", 2.2, 60807]

all_data = [prices, temps, words, car_details]

lst_of_lsts = [
    [1,2,3],
    ['a', 'b', 'c'],
    ["One", "Two", "Three"]]

nums = [1,2,3,4]
nums.remove(2)
print(nums)

nums = [1,2,3,4]
n = nums.pop(2)
print(n)
print(nums)

nums.extend([3,4,5])
print(nums)

nums.insert(0, 0)
print(nums)

nums = [1,2,3,4]
nums.insert(2, "2.5")
print(nums)