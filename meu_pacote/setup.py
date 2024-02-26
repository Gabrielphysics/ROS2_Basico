import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'meu_pacote'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "ola = meu_pacote.ola:main",
            "publicador = meu_pacote.publisher:main",
            "assinante = meu_pacote.subscriber:main",
            "frame_fixo = meu_pacote.frame_fixo:main",
            "frame_dinamico = meu_pacote.frame_dinamico:main",
            "parametros =  meu_pacote.parametros:main"
        ],
    },
)
