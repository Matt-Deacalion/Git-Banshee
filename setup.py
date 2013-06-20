#!/usr/bin/env python2

from setuptools import setup

setup(
    name='GitBanshee',
    version='0.1',
    url='http://dirtymonkey.co.uk/Git-Banshee',
    license='MIT',
    author='Matt Deacalion Stevens',
    author_email='matt@dirtymonkey.co.uk',
    description='Play sound effects when you commit, checkout and merge in git.',
    keywords='git hooks sound effects',
    packages=['gitbanshee'],
    scripts=['bin/git-banshee'],
    include_package_data=True,
    install_requires=[
        'gevent>=0.13',
        'gevent-socketio>=0.3.5-rc2',
        'socketIO-client==0.4',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Games/Entertainment',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Software Development',
        'Topic :: Software Development :: User Interfaces',
    ],
)
