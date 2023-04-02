from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    version='0.1.0',
    description='An important piece of software that listens in on your conversation and suggests fitting songs inspired by your conversation topics. This will save humanity',
    author='GamleDrenge',
    license='MIT',
)
