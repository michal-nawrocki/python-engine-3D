"""
Read models from files.

Right now it supports only .obj files
"""
from math_3d.vec3 import Vec3
from pipeline.helpers.triangle import Triangle


class ModelReader:

    @staticmethod
    def read_obj_model(path: str) -> [Triangle]:
        """
        Read .obj file and return a list of Triangles, a Model.

        :param path: Path to the .obj file
        :return: Model represented as a list of Triangle objects
        """
        v = []  # Vertices
        f = []  # Faces/Triangles

        with open(path) as file:
            lines = file.readlines()

        for line in lines:
            line = line.split()  # Remove whitespaces

            # Based of first char put in appropriate container
            if 'v' in line:
                v.append(Vec3(float(line[1]), float(line[2]), float(line[3])))
            elif 'f' in line:
                f.append(Triangle(v[int(line[1])-1], v[int(line[2])-1], v[int(line[3])-1]))
            else:
                continue

        return f
