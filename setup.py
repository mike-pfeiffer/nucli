from setuptools import setup

setup(
    name='nucli',
    version='0.1',
    py_modules=['nucli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        nucli=nucli:click_entry
    ''',
)