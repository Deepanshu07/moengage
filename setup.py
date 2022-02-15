from setuptools import setup
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
  name='moengage',
  packages=['moengage'],
  version='0.3.4',
  license='MIT',
  description='Wrapper library for calling Moengage APIs in python',
  long_description=README,
  long_description_content_type="text/markdown",
  author='Deepanshu Gupta',
  author_email='deepanshu71095@gmail.com',
  url='https://github.com/Deepanshu07/moengage',
  download_url='https://github.com/Deepanshu07/moengage/archive/refs/tags/v0.3.4.tar.gz',
  keywords=['MOENGAGE', 'MOENGAGE WRAPPER'],
  install_requires=[
          'asgiref',
          'certifi',
          'charset-normalizer',
          'decorator',
          'idna',
          'pytz',
          'requests',
          'six',
          'soupsieve',
          'sqlparse',
          'urllib3',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.9',
  ],
)