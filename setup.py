import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyTransdec",
    version="0.2.0",
    author="Piotr Zielinski",
    author_email="piotr_zielinski@g.pl",
    description="Transdec environment https://github.com/pwrdc/TransdecEnvironment controlling with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pwrdc/PyTransdec",
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'tqdm',
        'opencv-python',
        'mlagents==0.7.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
