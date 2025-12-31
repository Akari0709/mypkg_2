from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'mypkg_2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='akari',
    maintainer_email='s24C1068FQ@s.chibakoudai.jp',
    description='ロボットシステム工学課題',
    license='BSD-3-Clause',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'clock = mypkg_2.clock:main',
            #'listener = mypkg_2.listener:main',
        ],
    },
)
