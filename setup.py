#!/usr/bin/env python
from setuptools import setup, find_packages
import os

fp = open(os.path.join(os.path.dirname(__file__), "README.rst"))
readme_text = fp.read()
fp.close()

setup(
    name='CleverCSS',
    version='0.2.1',
    description='python inspired sass-like css preprocessor',
    long_description=readme_text,
    
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    maintainer='David Ziegler',
    maintainer_email='david.ziegler@gmail.com',
    
    url='http://sandbox.pocoo.org/clevercss/',
    download_url='http://github.com/dsc/clevercss/tree',
    
    packages=find_packages('.', exclude=['ez_setup', 'tests']),
    entry_points={
        'console_scripts': [
            'clevercss = clevercss.clevercss:main',
            'ccss = clevercss.bin.ccss:main [ccss]',
            'clevercss_extract_sprites = clevercss.bin.extract_sprites:main [extract_sprites]',
        ]
    },
    test_suite = 'clevercss.tests.all_tests',
    install_requires=[
        "cssutils>=0.9.8a1",
    ],
    extras_require = {
        'ccss':  [],
        'extras_require': [],
    },
    
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python'
    ],
    zip_safe = False,
)
