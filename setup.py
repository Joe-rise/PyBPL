from setuptools import setup, find_packages


setup(
    name='bpl',
    version='0.0.1',
    description='Bayesian Program Learning tookit',
    url='https://github.com/MaxwellRebo/PyBPL',
    author='Maxwell Rebo',
    author_email='maxwell.b.rebo@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'nose',
        'pymc3'
    ],
    dependency_links=[
        'git+https://github.com/pymc-devs/pymc3.git#egg=pymc3-3.0'
    ]
)
