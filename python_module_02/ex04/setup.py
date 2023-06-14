# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    setup.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/13 16:49:24 by lguisado          #+#    #+#              #
#    Updated: 2023/06/14 16:21:08 by lguisado         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from setuptools import setup, find_packages

with open("README.md", "r", encoding = "utf-8") as file:
	long_description = file.read()

setup(
	name='my_minipack',
	version='1.0.0',
	author='lguisado',
	author_email='lguisado@student.42malaga.com',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    project_urls = {
        "Bug Tracker": "package issues URL",
    },
    classifiers = [
		"OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3 :: Only",
    ],
	package_dir={"": "src"},
    packages=find_packages(where="./src"),
    python_requires = ">=3.7",
)
