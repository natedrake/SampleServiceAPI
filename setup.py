from setuptools import setup

setup(
    name='SampleServiceAPI',
    version=0.1,
    description='A sample API service.',
    url='https://github.com/natedrake/SampleServiceAPI',
    author='John O\'Grady <natedrake>',
    author_email='john@johnogrady.ie',
    license='MIT',
    packages=['SampleServiceAPI'],
    install_requires=[
        'flask',
    ],
    zip_safe=False
)
