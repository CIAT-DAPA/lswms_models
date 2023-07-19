from setuptools import setup, find_packages

setup(
    name="modelswp",
    version='v1.0.6',
    author="CarlosNasayo",
    author_email="c.nasayo@cgiar.com",
    description="Modelos para la base de datos waterpoints",
    url="https://github.com/CIAT-DAPA/lswms_models",
    download_url="https://github.com/CIAT-DAPA/lswms_models",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    keywords='mongodb orm waterpoints',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "mongoengine==0.26.0"
    ]
)
