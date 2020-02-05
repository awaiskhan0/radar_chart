import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="radar-chart",
    version="0.0.5",
    author="Awais Khan",
    author_email="awaisgithub@gmail.com",
    description="A package to quickly visualise radar charts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/awaiskhan0/radar_chart",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=["matplotlib", "numpy"]
)
