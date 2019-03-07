import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyTransdec",
    version="0.0.2",
    author="Piotr Zielinski",
    author_email="piotr_zielinski@g.pl",
    description="Transdec environment https://github.com/PiotrJZielinski/TransdecEnvironment controlling with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PiotrJZielinski/PyTransdec",
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'tqdm',
        'opencv-python',
        'mlagents'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
