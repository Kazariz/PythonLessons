def replace_o_except_first_and_last(text):
    indexes = [i for i, c in enumerate(text) if c == 'о']

    if len(indexes) <= 2:
        return text

    chars = list(text)

    for i in indexes[1:-1]:
        chars[i] = 'О'

    return ''.join(chars)


input_text = 'Замените в этой строке все появления буквы "о" на букву "О", кроме первого и последнего вхождения.'
output_text = replace_o_except_first_and_last(input_text)
print(output_text)
