def greedy_bag(max, items):
    items = sorted(items, key = lambda x: x[1] / x[0], reverse=True)
    total = 0
    details = list()

    for item in items:
        if max >= item[0]:
            max -= item[0]
            total += item[1]
            details.append([item[0], item[1], 1])
        else:
            fraction = max / item[0]
            fraction_value = item[1] * fraction
            total += fraction_value
            details.append([item[0], item[1], fraction])
            break;
    return total, details

items_list = ([10, 10], [20, 10], [30, 8], [25, 12], [60, 24])
test = ([10, 10], [15, 12], [20, 10], [25, 8], [30, 5])
print(greedy_bag(27, items_list))
print(greedy_bag(30, test))

