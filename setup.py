# -*- encoding: utf-8 -*-


import io
import re

from setuptools import find_packages, setup

test_requirements = [
    'pytest',
    'pytest-cov',
    'pyyaml',
    'requests'
]

prod_requirements = [
    'psycopg2-binary==2.8.6',
    'pika==1.2.0',
    'wheel',
    'pony',
    'psycopg2-binary==2.8.6',
    'loguru==0.5.3'
]

try:
    CONFIG = './worker/config/__init__.py'
    with io.open(CONFIG, encoding='utf8') as v:
        match = re.search(r"^VERSION = ['\"]([^'\"]*)['\"]", v.read(), re.M)
        version = match.group(1)

    with io.open(CONFIG, encoding='utf8') as v:
        match = re.search(r"^TITLE = ['\"]([^'\"]*)['\"]", v.read(), re.M)
        title = match.group(1)

    with io.open(CONFIG, encoding='utf8') as v:
        match = re.search(r"^DESCRIPTION = ['\"]([^'\"]*)['\"]", v.read(), re.M)
        description = match.group(1)
except AttributeError:
    raise RuntimeError("Unable to find 'version', 'title' and "
                       "'description' from config/__init__.py.")

setup(
    name="worker",
    version=version,
    author="Andy Jimenez",
    author_email="wasosky313@gmail.com",
    packages=find_packages(exclude='tests'),
    include_package_data=True,
    url="https://github.com/wasosky313/user_image_logs_service.git",
    license="COPYRIGHT",
    description=title,
    long_description=description,
    zip_safe=False,
    install_requires=prod_requirements,
    extras_require={
         'unit': test_requirements
    },
    python_requires='>=3.8',
    classifiers=[
        'Intended Audience :: My Team',
        'Natural Language :: English',
        'Operating System :: Ubuntu :: Linux',
        'Programming Language :: Python :: 3.8'
    ],
    keywords=(),
    entry_points={
        'console_scripts': [
            'worker = '
            'worker.main:worker'
        ],
    },
)
