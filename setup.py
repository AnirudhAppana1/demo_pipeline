from setuptools import setup,find_packages

setup(name = "cencus_income",
      version = "0.0.1",
      author = "Anirudh",
      author_email = "anirudhappana@gmail.com",
      packages=find_packages(include=['cencus_income']),
      install_requires = ["pandas","numpy","flask"]
         )