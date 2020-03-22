# -*- coding: utf-8 -*-
# totp.py
# Copyright (C) 2019-2020 KunoiSayami
#
# This module is part of simple-totp-paste and is released under
# the AGPL v3 License: https://www.gnu.org/licenses/agpl-3.0.txt
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
import sys
import time

import pyotp
import pyperclip


def run(token: str ='', _continue: bool=False):
	if token == '':
		with open('secret', 'r') as fin:
			token = fin.read().splitlines()[0]
	totp = pyotp.TOTP(token)

	if _continue:
		print('This program will continue copy totp code to clipboard,\npress Control+C to terminate is program.\n')

	betk = tk = totp.now()
	print(tk)
	pyperclip.copy(tk)
	while _continue:
		try:
			time.sleep(5)
		except KeyboardInterrupt:
			pyperclip.copy('')
			break
		tk = totp.now()
		if tk == betk:
			continue
		pyperclip.copy(tk)
		print(tk)
		betk = tk

if __name__ == "__main__":
	if len(sys.argv) == 1:
		run()
	elif len(sys.argv) == 2:
		if sys.argv[1] == '-t':
			run(_continue=True)
		else:
			run(sys.argv[1])
	else:
		run(sys.argv[1], '-t' in sys.argv)
