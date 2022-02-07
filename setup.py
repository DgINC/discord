from setuptools import setup, find_packages

version = '0.0.1'

install_requires = [
    'setuptools>=39.0.1',
    'sqlalchemy[asyncio]',
]

setup(
    name='discord',
    version=version,
    description='Discord API',
    url='https://',
    author='Leonid Kuzin',
    author_email='dg.inc.lcf@gmail.com',
    license='MIT',
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Topic :: Internet :: WWW/HTTP',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Flask',
        'Topic :: System :: Networking',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(),
    install_requires=install_requires,
    )
