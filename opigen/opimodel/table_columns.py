from typing import Optional


class Column:
    """ Representation of a Table column. """

    def __init__(self, name: str, width: int = 100, editable: bool = True,
                 options: Optional[list[str]] = None) -> None:
        self.name = name
        self.width = width
        self.editable = editable
        self.options = options

