# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='ssd',
    version=open('VERSION').read().strip(),
    description='Solid-State Drive Checker',
    long_description=open('README.rst').read(),
    keywords='ssd pyssd',
    url='https://github.com/vuolter/pySSD',
    download_url='https://github.com/vuolter/pySSD/releases',
    author='Walter Purcaro',
    author_email='vuolter@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        # 'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System',
        'Topic :: System :: Filesystems',
        'Topic :: Utilities'],
    platforms=['any'],
    py_modules=['ssd'],
    include_package_data=True,
    install_requires=[
        'psutil;os_name!="nt"',
        'pypiwin32>=154;os_name=="nt"',
        'wmi;os_name=="nt"'],
    python_requires='>=2.6,!=3.0,!=3.1,!=3.2',
    zip_safe=True)