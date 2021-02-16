from setuptools import setup


setup(name='pyfutebol',
      version='2.2.2',
      description='Crawler para resultados de futebol',
      url='https://github.com/fagnersouza666/pyfutebol/',
      author='Vinnicyus Gracindo',
      author_email='vini.gracindo@gmail.com',
      license='MIT',
      packages=['pyfutebol'],
      install_requires=[
        'beautifulsoup4',
      ],
      zip_safe=False)