# The combine_lists function merged the two lists by checking if the elements overlap based on their positions.if, all elements overlapped with each other, so they'd be combined into a single element

def combine_lists(list1, list2):
    combined = list1 + list2
    combined.sort(key=lambda x: x['positions'][0])

    result = []
    for element in combined:
        if not result:
            result.append(element)
        else:
            last_element = result[-1]
            if last_element['positions'][1] >= element['positions'][0]:
                last_element['values'].extend(element['values'])
                last_element['positions'][1] = max(last_element['positions'][1], element['positions'][1])
            else:
                result.append(element)

    return result

# Example Usage:
list1 = [{"positions": [1, 5], "values": [1, 2]}, {"positions": [6, 10], "values": [3, 4]}]
list2 = [{"positions": [3, 7], "values": [5, 6]}, {"positions": [8, 12], "values": [7, 8]}]

combined_list = combine_lists(list1, list2)
print("Combined List:", combined_list)
