import sys
# from ez_setup import use_setuptools
# use_setuptools()
from setuptools import setup


classifiers = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: End Users/Desktop',
    'Intended Audience :: Information Technology',
    'Intended Audience :: System Administrators',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Utilities',
]

long_description = open('README.rst').read()

version = '0.7'


def main():
    install_requires = [
        'pyexiv2',
        'mfind',
    ]
    if sys.version_info < (2, 7) or (3,) <= sys.version_info < (3, 2):
        install_requires.append('argparse')

    setup(
        name='mfind-exif',
        version=version,
        description="Extends mfind with EXIF tests and actions",
        author='Meitham Jamaa',
        author_email='m at meitham.com',
        url='https://meitham.com/mfind/',
        license='BSD',
        py_modules=('mfindexif', ),
        classifiers=classifiers,
        entry_points ="""[mfind.plugin]
                           tests=mfindexif:tests
                           actions=mfindexif:actions
                           cli_args=mfindexif:cli_args""",
    )


if __name__ == '__main__':
    main()
