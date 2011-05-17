from setuptools import setup,find_packages

setup(
    name="stddeviation",
    version="0.1",
    description="Calculate standard deviation",
    author="Russell Miller",
    install_requires=['argparse',],
    packages=find_packages(),
    entry_points=
        """
        [console_scripts]
        stddeviation = stddeviation.main:main
        """
    )
