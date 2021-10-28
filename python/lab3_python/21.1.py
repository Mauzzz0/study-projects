def from_string_to_list(string: str, container):
    [container.append(int(x)) for x in string.split(" ")]
    return container
