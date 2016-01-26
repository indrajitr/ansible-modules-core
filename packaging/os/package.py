#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2015, Ansible, inc
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

DOCUMENTATION = '''
---
module: package
version_added: 2.0
author:
    - Ansible Inc
maintainers:
    - Ansible Core Team
short_description: Generic OS package manager
description:
     - Installs, upgrade and removes packages using the underlying OS package manager.
options:
  name:
    description:
      - "Package name, or package specifier with version, like C(name-1.0)."
      - "Be aware that packages are not always named the same and this module will not 'translate' them per distro."
    required: true
  state:
    description:
      - Whether to install (C(present), C(latest)), or remove (C(absent)) a package.
    required: true
  pkg_args:
    description:
      - Additional package manager specific options to be passed on to the underlying package manager module in use (yum, apt, etc).
    required: false
    version_added: 2.1
  use:
    description:
      - The required package manager module to use (yum, apt, etc). The default 'auto' will use existing facts or try to autodetect it.
      - You should only use this field if the automatic selection is not working for some reason.
    required: false
    default: auto
requirements:
    - Whatever is required for the package plugins specific for each system.
notes:
    - This module actually calls the pertinent package modules for each system (apt, yum, etc).
'''
EXAMPLES = '''
- name: install the latest version of ntpdate
  package: name=ntpdate state=latest

# This uses a variable as this changes per distribution.
- name: remove the apache package
  package : name={{apache}} state=absent

# This uses variable name as well as pkg_args as these change per distribution.
- name: remove the apache package
  package: name={{apache}} pkg_args={{custom_args}}
# where custom_args: {'state': present, 'update_cache': yes}
'''
