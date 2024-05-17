def my_sort(lst_a: list[int], lst_b: list[int]) -> list[int]:
    index_a = len(lst_a) - 1
    index_b = len(lst_b) - 1
    result = []
    while index_a > 0 and index_b > 0:
        if lst_a[index_a] >= lst_b[index_b]:
            result.append(lst_a[index_a])
            index_a -= 1
        else:
            result.append(lst_b[index_b])
            index_b -= 1

    while index_a > 0:
        result.append(lst_a[index_a])
        index_a -= 1

    while index_b > 0:
        result.append(lst_b[index_b])
        index_b -= 1
    return result


def smart_igor(number_lights, quantity_convert, time_fire=2, number_fire_after_conversion=2) -> int:
    if quantity_convert <= 2:
        raise Exception("Игорь не на столько умен(")
    total_time = 0
    burnt = 0
    while number_lights > 0:
        total_time += number_lights * time_fire
        temp_number_lights = ((number_lights + burnt) // quantity_convert) * number_fire_after_conversion
        burnt = (number_lights + burnt) % quantity_convert
        number_lights = temp_number_lights

    return total_time
