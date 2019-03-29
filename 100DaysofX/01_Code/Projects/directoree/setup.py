from setuptools import setup

setup(
    name="directoree",
    version="0.1",
    py_modules=["directoree"],
    install_requires=["Click"],
    entry_points="""
        [console_scripts]
        directoree=directoree:cli
    """,
)

