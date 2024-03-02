import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "ML-and-DSA-Fundamentals-Chatbot-using-Llama2"
AUTHOR_USER_NAME = "himanko"
SRC_REPO = "ML-and-DSA-chatbot"
AUTHOR_EMAIL = "himankoboruah@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small chatbot for fundamental knowlage sharing on DSA and ML via user promt. This Llama2 based chatbot is trained on fundamental/theoretical books of DSA and ML",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)