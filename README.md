![Logo](https://raw.githubusercontent.com/idealista/tomcat-role/master/logo.gif)

[![Build Status](https://travis-ci.org/idealista/tomcat-role.svg?branch=master)](https://travis-ci.org/idealista/tomcat-role)
# Tomcat Ansible role

This ansible role installs a Tomcat server in an Ubuntu 18.04 Bionic / 16.04 Xenial, Debian 9 Stretch / 8 Jessie, or CentOS 7 environment.

- [Getting Started](#getting-started)
	- [Prerequisities](#prerequisities)
	- [Installing](#installing)
- [Usage](#usage)
- [Testing](#testing)
- [Built With](#built-with)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)
- [Contributing](#contributing)

## Getting Started

These instructions will get you a copy of the role for your ansible playbook. Once launched, it will install a [Tomcat](https://tomcat.apache.org/) server.

### Prerequisities

For compatible Ansible versions check [.travis.yml](.travis.yml).
Inventory destination should be an Ubuntu 18.04 Bionic / 16.04 Xenial, Debian 9 Stretch / 8 Jessie, or CentOS 7 environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with Docker as driver and [Goss](http://goss.rocks) as verifier

### Installing

Create or add to your roles dependency file (e.g requirements.yml) from GitHub:

```
- src: http://github.com/idealista/tomcat-role.git
  scm: git
  version: 1.9.0
  name: tomcat
```

or using [Ansible Galaxy](https://galaxy.ansible.com/idealista/tomcat-role/) as origin if you prefer:

```
- src: idealista.tomcat-role
  version: 1.9.0
  name: tomcat
```

Install the role with ansible-galaxy command:

```
ansible-galaxy install -p roles -r requirements.yml -f
```

Use in a playbook:

```
- hosts: someserver
  roles:
    - { role: tomcat }
```

## Usage

Look to the defaults properties file to see the possible configuration properties.

## Testing

### Install dependencies

```sh
pipenv install -r test-requirements.txt --python 2.7
```

For more information read the [pipenv docs](https://docs.pipenv.org/).

### Running test

```
pipenv run molecule test --all
```

See molecule/molecule.yml to check possible testing platforms.

## Works With

![Ansible](https://img.shields.io/badge/ansible-2.8.2.0-green.svg)
![Molecule](https://img.shields.io/badge/molecule-2.20.1-green.svg)
![Goss](https://img.shields.io/badge/goss-0.3.7-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/tomcat-role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/Tomcat-role/contributors) who participated in this project.

## License

![Apache 2.0 License](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

## Contributing

Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
