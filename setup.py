import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plotnineseqsuite",
    version="0.9.0",
    author="Cao Tianze",
    author_email="hnrcao@qq.com",
    description="A Python package for visualizing sequence data using ggplot2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/caotianze/plotnineseqsuite",
    project_urls={
        "Bug Tracker": "https://github.com/caotianze/plotnineseqsuite/issues",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['plotnineseqsuite','plotnineseqsuite.font','plotnineseqsuite.data'],
    python_requires=">=3.10",
    install_requires=['plotnine>=0.10.1'],
    license="MIT",
    keywords=['ggplot2', 'plotnine', 'Bioinformatics', 'Sequence logo'],
    package_data={
        "": ["*.csv"]
    }
)
