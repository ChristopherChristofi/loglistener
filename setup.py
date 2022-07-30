from setuptools import setup, find_packages

setup(
    name='lelisten',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'cachetools==5.2.0',
        'certifi==2022.6.15',
        'charset-normalizer==2.1.0',
        'google-api-core==2.8.2',
        'google-api-python-client==2.54.0',
        'google-auth==2.9.1',
        'google-auth-httplib2==0.1.0',
        'google-auth-oauthlib==0.5.2',
        'googleapis-common-protos==1.56.4',
        'httplib2==0.20.4',
        'idna==3.3',
        'oauthlib==3.2.0',
        'protobuf==4.21.3',
        'pyasn1==0.4.8',
        'pyasn1-modules==0.2.8',
        'pyparsing==3.0.9',
        'python-dotenv==0.20.0',
        'requests==2.28.1',
        'requests-oauthlib==1.3.1',
        'rsa==4.9',
        'six==1.16.0',
        'uritemplate==4.1.1',
        'urllib3==1.26.11',
    ],
    entry_points={
        'console_scripts': [
            'lelisten = src.lelisten.lelisten:run',
        ],
    },
)
