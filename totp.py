# -*- coding: utf-8 -*-
# totp.py
# Copyright (C) 2019 KunoiSayami
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
import pyotp
import pyperclip
import time

with open('secret', 'r') as fin:
    totp = pyotp.TOTP(fin.read().splitlines()[0])

betk = tk = totp.now()
print(tk)
while True:
    time.sleep(1)
    tk = totp.now()
    if tk == betk:
        continue
    pyperclip.copy(tk)
    print(tk)
    betk = tk