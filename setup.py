from setuptools import setup, find_packages

setup(
    name='libc_offdb',
    version='0.0.1',
    packages=['libc_offdb'],
    scripts=[
        'scripts/download_libcs'
    ],
    description='A simple tool to locate libc offsets',
    author='Anciety(EscapingBug)',
    install_requires=['pwntools'],
)
