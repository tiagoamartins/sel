from setuptools import setup, find_packages

setup(
    name='raspweb',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'gpiozero',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_reqire=[
        'pytest',
    ],
)
