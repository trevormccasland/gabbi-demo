from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="gabbi_demo",
    version="0.0.1",
    author="Trevor McCasland",
    description="gabbi demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trevormccasland/gabbi-demo",
    packages=["gabbi_demo"],
    entry_points={
            'console_scripts': [
                    'gabbi-demo=gabbi_demo.main:main',
            ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)