from setuptools import setup
import json

package_data = json.load(open('package.json', 'r', encoding='utf-8'))

setup(
    name=package_data['name'],
    version=package_data['version'],
    description=package_data['description'],
    url=package_data['url'],
    author=package_data['author'],
    author_email=package_data['author_email'],
    packages=package_data['packages'],
    install_requires=package_data['install_requires']
)