import setuptools

__version__ = "0.01"

setuptools.setup(name='pypheno',
               version=__version__,
               description='Methods to extract land surface phenology from timeseries of\
                            of vegetation indices',
               url='https://github.com/geopanda1/pypheno',
               author='Andreas Kollert',
               author_email='andikollert@gmail.com',
               license='GNU GPLv3',
               packages=setuptools.find_packages(),
               install_requires=['numpy',
                                 'scipy'],
               platforms='any',
                         python_requires='>=3.6',
               zip_safe=False)
