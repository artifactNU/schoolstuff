def treecoords(tree: dict, current_coord: tuple = ()) -> tuple:
    result = []
    for key, value in tree.items():
        new_coord = current_coord + (key,)
        if isinstance(value, dict):
            result.extend(treecoords(value, new_coord))
        else:
            result.append((new_coord, value))
    return tuple(result)


treecoords({"a": 1, "b": 2})
