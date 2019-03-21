from setuptools import setup


setup(
    name="fyinit",
    version="0.1",
    py_modules=["fyinit"],
    install_requires=["Click"],
    entry_points="""
        [console_scripts]
        fyinit=fyinit:cli
    """,
)
