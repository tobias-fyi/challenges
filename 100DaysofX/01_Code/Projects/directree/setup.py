from setuptools import setup

setup(
    name="directree",
    version="0.1",
    py_modules=["directree"],
    install_requires=["Click"],
    entry_points="""
        [console_scripts]
        directree=directree:cli
    """,
)
