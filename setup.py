# setup.py
from setuptools import setup, find_packages

setup(
    name='k12bot',
    version='0.0.1',
    description='A K12 educational chatbot with various features including data ingestion, chatbot functionalities, MCQ generation, document-based chat and many more.',
    author='Dibyendu Biswas',
    author_email='dibyendubiswas1998@gmail.com',
    url='https://github.com/dibyendubiswas1998/K12bot',  # Update with your project's URL
    project_urls={
        "Bug Tracker": f"https://github.com/dibyendubiswas1998/K12bot/issues",
    },
    packages=find_packages(),
    include_package_data=True,
    # install_requires=[
    #     'Flask',
    # ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE',
    ],
    entry_points={
        'console_scripts': [
            'run-bot=scripts.run_bot:main',
        ],
    },
    python_requires='>=3.10',
)