#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2015, Jon Hawkesworth (@jhawkesworth) <figs@unity.demon.co.uk>
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


ANSIBLE_METADATA = {'status': ['stableinterface'],
                    'supported_by': 'core',
                    'version': '1.0'}

DOCUMENTATION = '''
---
module: win_file
version_added: "1.9.2"
short_description: Creates, touches or removes files or directories.
description:
     - Creates (empty) files, updates file modification stamps of existing files,
       and can create or remove directories.
       Unlike M(file), does not modify ownership, permissions or manipulate links.
notes:
    - See also M(win_copy), M(win_template), M(copy), M(template), M(assemble)
requirements: [ ]
author: "Jon Hawkesworth (@jhawkesworth)"
options:
  path:
    description:
      - 'path to the file being managed.  Aliases: I(dest), I(name)'
    required: true
    default: []
    aliases: ['dest', 'name']
  state:
    description:
      - If C(directory), all immediate subdirectories will be created if they
        do not exist.
        If C(file), the file will NOT be created if it does not exist, see the M(copy)
        or M(template) module if you want that behavior.  If C(absent),
        directories will be recursively deleted, and files will be removed.
        If C(touch), an empty file will be created if the C(path) does not
        exist, while an existing file or directory will receive updated file access and
        modification times (similar to the way C(touch) works from the command line).
    required: false
    default: file
    choices: [ file, directory, touch, absent ]
'''

EXAMPLES = '''
- name: Create a file
  win_file:
    path: C:\temp\foo.conf
    state: file

- name: Touch a file (creates if not present, updates modification time if present)
  win_file:
    path: C:\temp\foo.conf
    state: touch

- name: Remove a file, if present
  win_file:
    path: C:\temp\foo.conf
    state: absent

- name: Create directory structure
  win_file:
    path: C:\temp\folder\subfolder
    state: directory

- name: Remove directory structure
  win_file:
    path: C:\temp
    state: absent
'''
