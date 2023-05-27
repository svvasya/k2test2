from setuptools import setup, find_packages

setup(
    name='k2test',
    version='1.0.0',
    description='Description of my project',
    author='Your Name',
    author_email='yourname@example.com',
    packages=find_packages(),
    package_data={'k2test':['views.py']},  # Додано 'views.py' як файл для копіювання
    install_requires=[

    ],
)