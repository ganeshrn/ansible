#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2017, Ansible by Red Hat, inc
#
# This file is part of Ansible by Red Hat
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

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'core'}


DOCUMENTATION = """
---
module: net_interface
version_added: "2.4"
author: "Ganesh Nalawade (@ganeshrn)"
short_description: Manage Interface on network devices
description:
  - This module provides declarative management of Interfaces
    on network devices.
options:
  name:
    description:
      - Name of the Interface.
  description:
    description:
      - Description of Interface.
  enabled:
    description:
      - Operational status of the interface link
    default: yes
  speed:
    description:
      - Interface link speed
  mtu:
    decription:
      - Maximum size of transmit packet
  duplex:
    description:
      - Interface link status
    default: full
    choices: ['full', 'half', 'auto']
  tx_rate:
    description:
      - Transmit rate
  rx_rate:
    descriptiom:
      - Recevier rate
  collection:
    description: List of Interfaces definitions
  purge:
    description:
      - Purge Interfaces not defined in the collections parameter.
        This applies only for logical interface
    default: no
  state:
    description:
      - State of the Interface.
    default: present
    choices: ['present', 'absent']
"""

EXAMPLES = """
- name: configure interface
  net_interface:
    name: ge-0/0/1
    description: test-interface

- name: remove interface
  net_interface:
    name: ge-0/0/1
    state: absent

- name: make interface up
  net_interface:
    name: ge-0/0/1
    description: test-interface
    state: present
    enabled: True

- name: make interface down
  net_interface:
    name: ge-0/0/1
    description: test-interface
    state: present
    enabled: False
"""

RETURN = """
commands:
  description: The list of configuration mode commands to send to the device
  returned: always
  type: list
  sample:
    - interface 20
    - name test-interface
rpc:
  description: load-configuration RPC send to the device
  returned: when configuration is changed on device
  type: string
  sample: "<interfaces>
             <interface>
               <name>ge-0/0/0</name>
               <description>test interface</description>
              </interface>
           </interfaces>"

Note: Return value varies based on the newtork os platform
For junos platform C(rpc) is returned.
For other platform C(commands) is returned.
"""
