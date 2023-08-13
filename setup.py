import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    name="motion",
    py_modules=["BVH", "Animation", "quaternions", "Quaternions", "Pivots", "AnimationStructure", "InverseKinematics", "TimeWrap", "visualizations"],
    version="1.0",
    description="Motion library, forked from https://github.com/sigal-raab/Motion.git",
    author="Sigal Raab",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements"))
        )
    ],
    include_package_data=True
)
