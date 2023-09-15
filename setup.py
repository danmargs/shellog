from setuptools import setup

setup(
    name='shellog',
    version='1.0.2',    
    description='A Python package to get notifications about the logs of a process',
    url='https://github.com/danmargs/shellog',
    author='Daniele Margiotta',
    author_email='daniele.margiotta11@gmail.com',
    license='BSD 2-clause',
    packages=['shellog'],
    install_requires=['telepot'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    long_description_content_type="text/markdown",

)
