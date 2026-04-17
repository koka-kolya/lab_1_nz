from setuptools import setup
import os
from glob import glob

package_name = 'super_koka_study_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
	    (os.path.join('share', package_name, 'launch'), 
         glob('launch/*.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='you@example.com',
    description='TODO: Package description',
    license='TODO: License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'time_printer = super_koka_study_pkg.time_printer:main',   # ← добавляем эту строку
            'talker = super_koka_study_pkg.talker:main',
            'listener = super_koka_study_pkg.listener:main',
            'even_talker = super_koka_study_pkg.even_number_publisher:main',
            'overflow_listener = super_koka_study_pkg.overflow_listener:main',
            'even_talker_params = super_koka_study_pkg.even_number_publisher_params:main',
            'overflow_listener_params = super_koka_study_pkg.overflow_listener_params:main',
            'static_tf_broadcaster = super_koka_study_pkg.static_tf_broadcaster'
        ],
    },
)
