"""Setup file."""

from setuptools import setup, find_packages


setup(
    name="TeleSendTime",
    version='0.1.0',
    description="Telegram Message Automation Module.",
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
