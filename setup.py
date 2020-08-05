"""Setup file."""

from setuptools import setup, find_packages

with open('./README.md', 'rb') as file:
    long_description = file.read().decode('UTF-8')


setup(
    name="TeleSendTime",
    version='0.1.1',
    description="Telegram Message Automation Module.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://gitlab.com/DarkSuniuM/TeleSendTime",
    project_urls={
        "Code": "https://gitlab.com/DarkSuniuM/TeleSendTime",
        "Issue tracker": "https://gitlab.com/DarkSuniuM/TeleSendTime/issues",
    },
    author="Alireza Ayinmehr",
    author_email="alireza.ayinmehr@gmail.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "requests>=2"
    ]
)
