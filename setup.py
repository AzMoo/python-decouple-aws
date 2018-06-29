from setuptools import find_packages, setup

dev_deps = [
    'prospector',
]

setup(
    name="python-decouple-aws",
    version="0.1.0",
    packages=find_packages(),
    author="Matt Magin",
    author_email="matt.magin@cmv.com.au",
    description="AWS Extensions for Python Decouple",
    url="https://github.com/AzMoo/python-decouple-aws",
    license="MIT",
    install_requires=[
        'boto3',
    ],
    python_requires='>=3.4',
    extras_require={
        'dev': dev_deps
    },

)
