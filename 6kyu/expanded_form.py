def expanded_form(num):
    return ' + '.join(
        f"{digit}{'0' * (len(str(num)) - idx - 1)}"
        for idx, digit in enumerate(str(num))
        if digit != '0'
    )
