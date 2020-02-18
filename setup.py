# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('bnarg/bnarg.py').read(),
    re.M
    ).group(1)


with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name="bnarg",
    packages=["bnarg"],
    entry_points={
        "console_scripts": ['bnarg=bnarg.bnarg:main']
        },
    version=version,
    description="Paquete no oficial para obtener datos del Banco de la Nación Argentina.",
    long_description=long_descr,
    long_description_content_type='text/markdown',
    author="Mijail Todorovich",
    author_email="mijailtodorovich@gmail.com",
    url="https://github.com/tmijail/bnarg",
    install_requires=['click',
                      'requests',
                      'beautifulsoup4']
)
