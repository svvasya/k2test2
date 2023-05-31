from setuptools import setup, find_packages

setup(
    name='k2test2',
    version='1.0.0',
    description='Description of my project',
    author='Your Name',
    author_email='yourname@example.com',    
    package_data={'k2test': ['views.py', 'app.py', 'templates']},
    install_requires=[
        # Додаткові залежності
    ],
)
