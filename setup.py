# setup.py
from setuptools import setup, find_packages

setup(
    name="GaugeSToVbo",
    version="0.1.0",
    author="Daniel Kuecker",
    author_email="daniel@kuecker.net",
    description="A tool to convert gauge.S data to VBO format",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/GaugeSToVbo",
    packages=find_packages(),
    install_requires=[
        "pandas",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'GaugeSToVbo=GaugeSToVbo.GaugeSToVbo:main',
        ],
    },
)
