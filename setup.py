import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'A package for finding and confirming prime numbers'

# Setting up
setup(
    name="primarypy",
    version=VERSION,
    author="lasanga_boi",
    author_email="alriksen@outlook.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 2 - Finished",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
