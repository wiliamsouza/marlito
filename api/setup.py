from __future__ import print_function
from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys
import io


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md')


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--strict', '--verbose', '--tb=long',
                          '--cov', 'api', 'api']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name='api',
    version='0.1.0',
    url='http://github.com/wiliamsouza83/',
    license='Apache Software License 2.0',
    author='Wiliam Souza',
    tests_require=['pytest', 'pytest-cov'],
    install_requires=['Flask', 'Flask-Script'],
    cmdclass={'test': PyTest},
    author_email='wiliamsouza83@gmail.com',
    description='Cars application',
    long_description=long_description,
    packages=['api'],
    include_package_data=True,
    platforms='any',
    zip_safe=False,
    package_data={'api': ['templates/**', 'static/*/*']},
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    extras_require={
        'testing': ['pytest'],
    }
)
