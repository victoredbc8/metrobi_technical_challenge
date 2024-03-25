# i chose set because set eliminates duplicates and is O(1) complexity with 'in'
def find_duplicates(arr):
    duplicates = []
    seen = set()

    for item in arr:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)

    return duplicates

list = ['a', 'b', 'a']
print(find_duplicates(list))
