from setuptools import setup

setup(name='pyflight',
      version='0.1',
      description='A simple wrapper for the Google Flights Search API.',
      url='https://github.com/AnthonyBloomer/pyflight',
      author='Anthony Bloomer',
      author_email='ant0@protonmail.ch',
      license='MIT',
      packages=['pyflight'],
      install_requires=[
          'requests',
      ],
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          "Topic :: Software Development :: Libraries",
          'Programming Language :: Python :: 2.7'
      ],
      zip_safe=False)
