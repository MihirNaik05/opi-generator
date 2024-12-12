def mangle_name(name: str):
    """ Convert the name found in a color or font configuration file into
    a Python variable:
    - convert to upper-case
    - replace non-letters with underscores
    - avoid consecutive underscores

    Parameters
    ----------
    name : str
        Name to convert.

    Returns
    -------
    r: str
        The converted name
    """
    last = ''
    deduped = []
    for char in name:
        if not char.isalpha() and not char.isdigit():
            if last == '_':
                continue
            else:
                char = '_'
        last = char
        deduped.append(char)

    name = ''.join(deduped).upper()
    return name


def add_attr_to_module(name, value, module):
    """Attach value to the namespace of module with a names converted
       into appropriate a constant by the mangle_name() function.

    Args:
        name to be converted and used
        value to be assigned
        module to attach the value to
    """
    var = mangle_name(name)
    if hasattr(module, var):
        print('Warning: overwriting variable {} in module {}'.format(
            var, module))
    setattr(module, var, value)
