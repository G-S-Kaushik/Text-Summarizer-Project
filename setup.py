import setuptools

with open("README.md", "r",encoding="utf8") as f:
    long_description = f.read()

__version__ ="0.0.0"

REPO_NAME = "Text-Summerizer-Project"
AUTHOR = "G-S-Kaushik"
SRC_REPO = "textsumerizer"
AUTHOR_EMAIL = "g.skaushik41@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)