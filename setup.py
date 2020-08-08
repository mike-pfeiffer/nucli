from setuptools import setup

setup(
    name='nucli',
    version='0.2',
    py_modules=['nucli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        nucli=app.nucli:click_entry
    ''',
)
