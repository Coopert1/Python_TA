def stats(input_data: list) -> list:
    element_counts = {}
    for element in input_data:
        if element in element_counts:
            element_counts[element] += 1
        else:
            element_counts[element] = 1
    max_count = max(element_counts.values())
    not_repeated_elements = [element for element, count in element_counts.items() if count == 1]
    max_repeated = [element for element, count in element_counts.items() if count == max_count]
    max_occurrence = [count for element, count in element_counts.items() if count == max_count]
    return [len(input_data),  # Total amount of received integers.
            len(set(input_data)),  # Total amount of different values the array has.
            len(not_repeated_elements),  # Total amount of values that occur only once.
            sorted(max_repeated),  # The element(s) that has (or have) the maximum occurrence.
            max_occurrence]  # Maximum occurrence of the integer(s)
