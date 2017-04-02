import setuptools

setuptools.setup(
    name="kinto-github-token",
    version="0.1.0",
    url="https://github.com/ptgamr/kinto-github-token",

    author="Anh Trinh",
    author_email="anh.trinhtrung@gmail.com",

    description="Github Authentication support for Kinto",
    long_description=open('README.md').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
