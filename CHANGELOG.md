# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [Keep a changelog](https://github.com/olivierlacan/keep-a-changelog).

## [Unreleased](https://github.com/idealista/tomcat_role/tree/develop)


## [1.10.0](https://github.com/idealista/tomcat_role/tree/1.10.0)
[Full Changelog](https://github.com/idealista/tomcat_role/compare/1.9.1...1.10.0)
### Added
- *[#91](https://github.com/idealista/tomcat_role/issues/91) Add support for downloaded agents as jar instead of compressed file* @sorobon
### Changed
- * Allow the option to change maxHttpHeaderSize value
### Fixed
- *[#88](https://github.com/idealista/tomcat_role/issues/88) Systemd security default limits fixed* @ftsao
- *Updated test dependencies* @ftsao
- *Force using python3 interpreter in tests; replaced python-lxml by python3-lxml dependency in managed nodes* @ftsao

## [1.9.1](https://github.com/idealista/tomcat_role/tree/1.9.1)
[Full Changelog](https://github.com/idealista/tomcat_role/compare/1.9.0...1.9.1)
### Changed
- *[#81](https://github.com/idealista/tomcat_role/issues/81) Add support to ansible 2.9* @sorobon

## [1.9.0](https://github.com/idealista/tomcat_role/tree/1.9.0)
[Full Changelog](https://github.com/idealista/tomcat_role/compare/1.8.0...1.9.0)
### Changed
- *[#61](https://github.com/idealista/tomcat_role/issues/61) Update molecule to 3.x* @sorobon
- *[#63](https://github.com/idealista/tomcat_role/issues/63) Rename role to tomcat_role* @sorobon
- *[#66](https://github.com/idealista/tomcat_role/issues/66) Improve agents management* @sorobon
- *[#64](https://github.com/idealista/tomcat_role/issues/64) Adding testing scenarios for tomcat 7.x and 8.x* @sorobon
- *[#69](https://github.com/idealista/tomcat_role/issues/69) Improve systemd template adding limits* @sorobon

## [1.8.0](https://github.com/idealista/tomcat_role/tree/1.8.0)
[Full Changelog](https://github.com/idealista/tomcat_role/compare/1.7.0...1.8.0)
### Added
- *[#56](https://github.com/idealista/tomcat_role/issues/56) Add Ansible 2.6 support for module maven_artifact* @jnogol

## [1.7.0](https://github.com/idealista/tomcat_role/tree/1.7.0)
[Full Changelog](https://github.com/idealista/tomcat_role/compare/1.6.2...1.7.0)
### Changed
- *[#53](https://github.com/idealista/tomcat_role/issues/53) Allow the option to pass additional environment vars* @sorobon
- *Tomcat version to 8.5.31* @sorobon
### Fixed
- *[#4](https://github.com/idealista/tomcat_role/issues/4) Notify restart handler after new files copied/template* @sorobon

## [1.6.2](https://github.com/idealista/tomcat_role/tree/1.6.2)
[Full Changelog](https://github.com/idealista/tomcat_role/compare/1.6.1...1.6.2)
### Changed
- *[#49](https://github.com/idealista/tomcat_role/issues/49) Updated tomcat version to 8.5.29* @sorobon

## [1.6.1](https://github.com/idealista/tomcat_role/tree/1.6.1)
[Full Changelog](https://github.com/idealista/tomcat_role/compare/1.6.0...1.6.1)
### Changed
- *[#46](https://github.com/idealista/tomcat_role/issues/46) Updated tomcat version to 8.5.28* @sorobon

## [1.6.0](https://github.com/idealista/tomcat_role/tree/1.6.0)
[Full Changelog](https://github.com/idealista/tomcat_role/compare/1.5.0...1.6.0)
### Added
- *[#43](https://github.com/idealista/tomcat_role/issues/43) Allow to change log files directory* @sorobon

## [1.5.0](https://github.com/idealista/tomcat_role/tree/1.5.0)
[Full Changelog](https://github.com/idealista/tomcat_role/compare/1.4.0...1.5.0)
### Added
- *[#40](https://github.com/idealista/tomcat_role/issues/40) Support for addons like java-agents* @sorobon

## [1.4.0](https://github.com/idealista/tomcat_role/tree/1.4.0)
[Full Changelog](https://github.com/idealista/tomcat_role/compare/1.3.1...1.4.0)
### Added
- *[#29](https://github.com/idealista/tomcat_role/issues/29) Upgrade molecule* @jdvr
- *[#26](https://github.com/idealista/tomcat_role/issues/26) Fix to copy extra configuration recursively* @dortegau
- *[#24](https://github.com/idealista/tomcat_role/issues/24) Follow OWASP recommendations to protect Shutdown port* @dortegau
- *[#21](https://github.com/idealista/tomcat_role/issues/21) Remove pre-installed folders from webapps* @dortegau

## [1.3.1](https://github.com/idealista/tomcat_role/tree/1.3.1)
[Full Changelog](https://github.com/idealista/tomcat_role/compare/1.3.0...1.3.1)
### Fixed
- *[#17](https://github.com/idealista/tomcat_role/issues/17) Fix war user and group after download* @jdvr

## [1.3.0](https://github.com/idealista/tomcat_role/tree/1.3.0)
[Full Changelog](https://github.com/idealista/tomcat_role/compare/1.2.0...1.3.0)
### Added
- *[#13](https://github.com/idealista/tomcat_role/issues/13) Add maven repository as a valid download war source* @jdvr

## [1.2.0](https://github.com/idealista/tomcat_role/tree/1.2.0)
[Full Changelog](https://github.com/idealista/tomcat_role/compare/1.1.2...1.2.0)
### Added
- *[#5](https://github.com/idealista/tomcat_role/issues/5) Add a name for the downloaded war during deployment* @jdvr

## [1.1.2](https://github.com/idealista/tomcat_role/tree/1.1.2)
[Full Changelog](https://github.com/idealista/tomcat_role/compare/1.1.0...1.1.2)
### Fixed
- *[#8](https://github.com/idealista/tomcat_role/issues/8) Fix systemd startup* @jmonterrubio
- *[#6](https://github.com/idealista/tomcat_role/issues/6) Fix conf directory template copy* @jnogol

## [1.1.0](https://github.com/idealista/tomcat_role/tree/1.1.0)
[Full Changelog](https://github.com/idealista/tomcat_role/compare/1.0.0...1.1.0)
### Added
- *[#1](https://github.com/idealista/tomcat_role/issues/1) Add deploy task* @jdvr


## [1.0.0](https://github.com/idealista/tomcat_role/tree/1.0.0)
### Added
- *First release*
