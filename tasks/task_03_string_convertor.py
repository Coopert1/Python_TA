def verify_sum_of_cubes_is_even(num):
    cube_sum = 0
    for i in num:
        cube_sum += int(i) ** 3
    return cube_sum % 2 == 0


def convert(input_str: str, divider: int) -> str:
    if divider > len(input_str) or divider <= 0:
        return ''
    else:
        parts = [input_str[i:i + divider] for i in range(0, len(input_str), divider)]
        if len(parts[-1]) < divider:
            parts.pop()
        converted = []
        for part in parts:
            if verify_sum_of_cubes_is_even(part):
                part = part[::-1]
            else:
                part = part[1:] + part[0]
            converted.append(part)
        return ''.join(converted)

