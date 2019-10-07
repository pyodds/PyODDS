from distutils.core import setup

from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pyodds',
    version='1.0.0a0',
    description='An end-to-end anomaly detection system',
    author='Data Analytics at Texas A&M (DATA) Lab, Yuening Li',
    author_email='yuehningli@gmail.com',
    download_url='https://github.com/yli96/PyOutlierDetectionSys/archive/master.zip',
    keywords=['AnomalyDetection', 'SQLServer'],
    install_requires=[
        'tensorflow>=2.0.0b1',
        'scikit-learn',
        'numpy',
        'luminol',
        'seaborn',
        'torch',
        'tqdm',
        'pandas',
        'matplotlib',
    ],
    packages=find_packages(),
    python_requires='>=3.6',
)
