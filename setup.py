from setuptools import setup, find_packages

setup(
    name='smartaddress',
    version='1.0.5',
    author='andy',
    author_email='liuxiaoming@yihaohulian.com',
    description='Intelligent resolution of receiving address',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    # url='',
    packages=find_packages(),
    python_requires='>=3.6',
)