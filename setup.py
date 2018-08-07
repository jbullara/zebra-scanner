from setuptools import setup, Extension
import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

zebra_scanner_module = Extension("zebra_scanner",
    include_dirs=['/usr/include/zebra-scanner', './include', '/usr/include/python2.7'],
    library_dirs=['/usr/lib/zebra-scanner/corescanner', '/usr/lib/x86_64-linux-gnu'],
    libraries=['cs-client', 'cs-common', 'boost_python', 'python2.7', 'pugixml'],
    sources=['./src/BoostPythonCoreScanner.cpp'],
    extra_compile_args=['-Wno-deprecated', '-std=c++0x']

)

print(zebra_scanner_module)

setup(
    name="zebra-scanner",
    #    version_format="{tag}",
    author="David Jablonski",
    author_email="dayjaby@gmail.com",
    description="Scan barcodes with a zebra barcode scanner",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/dayjaby/zebra-scanner",
    packages=setuptools.find_packages(),
    #setup_requires=['setuptools-git-version'],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    ext_modules=[zebra_scanner_module]
)