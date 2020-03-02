from decimal import Decimal
from typing import List


class WavefrontObj:
    __slots__ = (
        "geometric_vertices",
        "faces",
    )

    @classmethod
    def from_file_path(cls, file_path: str) -> WavefrontObj:
        with open(file_path, 'r') as model_file:
            line = model_file.readline()

    def __init__(self, geometric_vertices: List[Decimal]):
        self.geometric_vertices = []
        self.faces = []
