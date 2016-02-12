try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup


setup(
    name='pytest-dbfixtures-memcached',
    version='0.1.3',
    description='pytest-dbfixtures Memcached support',
    author='Marek Kowalski',
    author_email='kowalski0123@gmail.com',
    install_requires=[
        'pytest-dbfixtures',
    ],
    packages=['pytest_dbfixtures_memcached'],
    include_package_data=True,
    zip_safe=False,
)
