from setuptools import setup

setup(
    name="mani_skill",
    version="1.0",
    author="SU Lab at UC San Diego",
    zip_safe=False,
    install_requires=[
        "gym",
        "open3d",
        "pyyaml",
        "rtree",
        "sapien",
        "scipy",
        "shapely",
        "transforms3d",
        "trimesh",
    ]
)
