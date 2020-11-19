MSG_NEGATIVES = "negatives not allowed"

def add(string_numbers: str) -> int:
    separator = ","

    if string_numbers.startswith("//"):
        first, string_numbers = string_numbers.split("\n", maxsplit=2)
        separator = first.replace("//", '')
        assert len(separator) == 1

    chunks = string_numbers.split()  # ["123", "12, 12"]
    str_numbers = []
    for chunk in chunks:
        str_numbers += chunk.split(separator)
        str_numbers.extend( chunk.split(separator) )

    result = 0
    negatives = []
    for s in str_numbers:
        if s:
            n = int(s)
            if n < 0:
                negatives.append(n)
            result += n

    if negatives:
        raise ValueError(f"{MSG_NEGATIVES}, found {negatives}")

    return result
