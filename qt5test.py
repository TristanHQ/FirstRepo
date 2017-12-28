# -*- coding: utf-8 -*-
#
#  qt5test.py
#  
#  Copyright 2017 Tristan <Tristan@HQ>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import importlib,sys
importlib.reload(sys)
sys.setdefaultencoding('utf8')

from PyQt5 import QtGui

app=QTGui.QApplication(sys.argv)
Widget=QtGui.QWidget()
Widget.resize(350,250)
Widget.setWindowTitle(u'第一个窗口程序')
Widget.show()
sys.exit(app.exec_())
