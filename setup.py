from setuptools import setup


setup(name='foobar',
      version='0.1',
      packages=['foobar',
                'foobar.flakes'],
      entry_points={
          'flake8.extension': [
              'X001 = foobar.flakes:KwArgsChecker'
          ]
      })
