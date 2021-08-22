import os
from glob import glob
from setuptools import setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*_launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kzitn',
    maintainer_email='xxxxx@gmail.com',
    description='a package for practice',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = my_py_pkg.talker:main',
            'listener = my_py_pkg.listener:main'
        ],
    },
)
