import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    README = fh.read()

setuptools.setup(
    name="vnfaker",
    version="0.0.3",
    author="Phan Duc Quang",
    author_email="phanducquang07@gmail.com",
    description="vnfaker is a Python package that generates fake data about fullname, address, phone, date_of_birth,... in Viet Nam.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/phanducquang/vnfaker",
    project_urls={
        "Bug Tracker": "https://github.com/phanducquang/vnfaker/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    package_data={"": ["data/*/*.name", "data/*/*.json", "data/*/*.txt"],},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        "orjson>=3.8.10",
        "unidecode>=1.3.6"
    ],
)
