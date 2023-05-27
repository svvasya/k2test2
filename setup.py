from setuptools import setup, find_packages

setup(
    name='myproject',
    version='1.0.0',
    description='Description of my project',
    author='Your Name',
    author_email='yourname@example.com',
    packages=find_packages(),
    package_data={'myproject': ['views.py']},  # Додано 'views.py' як файл для копіювання
    install_requires=[

    ],
)
