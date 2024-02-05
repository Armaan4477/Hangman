#     Copyright (C) 2022  Sumair Ijaz Hashmi - LUMS roll number: 24100004

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https:#www.gnu.org/licenses/>.


#####################################################################################################################################################
# The code below was used to generate some repetitive code, such as for connecting the buttons of the keybad to the relevant function calls
#####################################################################################################################################################



initial = """self.pushButton_10.setText(_translate("HangMan", "a"))
self.pushButton_11.setText(_translate("HangMan", "b"))
self.pushButton_12.setText(_translate("HangMan", "c"))
self.pushButton_13.setText(_translate("HangMan", "d"))
self.pushButton_14.setText(_translate("HangMan", "e"))
self.pushButton_15.setText(_translate("HangMan", "f"))
self.pushButton_16.setText(_translate("HangMan", "g"))
self.pushButton_17.setText(_translate("HangMan", "h"))
self.pushButton_18.setText(_translate("HangMan", "i"))
self.pushButton_19.setText(_translate("HangMan", "j"))
self.pushButton_20.setText(_translate("HangMan", "k"))
self.pushButton_21.setText(_translate("HangMan", "l"))
self.pushButton_22.setText(_translate("HangMan", "m"))
self.pushButton_23.setText(_translate("HangMan", "n"))
self.pushButton_24.setText(_translate("HangMan", "o"))
self.pushButton_25.setText(_translate("HangMan", "p"))
self.pushButton_26.setText(_translate("HangMan", "q"))
self.pushButton_27.setText(_translate("HangMan", "r"))
self.pushButton_28.setText(_translate("HangMan", "s"))
self.pushButton_29.setText(_translate("HangMan", "t"))
self.pushButton_30.setText(_translate("HangMan", "u"))
self.pushButton_31.setText(_translate("HangMan", "v"))
self.pushButton_32.setText(_translate("HangMan", "w"))
self.pushButton_33.setText(_translate("HangMan", "x"))
self.pushButton_34.setText(_translate("HangMan", "y"))
self.pushButton_35.setText(_translate("HangMan", "z"))"""


print("############################################ function calls #################################################")

connectOnClick = ""

lines = initial.split("\n")
for l in lines:
    connectOnClick += "self.pushButton_" + str(l[16]) + str(l[17]) + ".clicked.connect(self." + l[50] + "_press)\n"

connectOnClick = connectOnClick[:-1]

print(connectOnClick)

print("##################################### function definitions ###########################################")

funcDefs = ""

lines = initial.split("\n")
for l in lines:
    currentFunc = "def " + l[50] + "_press(self):\n    self.button_pressed('" + l[50] + "')"
    funcDefs += currentFunc + "\n"

funcDefs = funcDefs[:-1]

print(funcDefs)

print("###################################################### disconnect functions #####################################################")

disconnectFuncs = ""

lines = initial.split("\n")
for l in lines:
    disconnectFuncs += "self.pushButton_" + str(l[16]) + str(l[17]) + ".clicked.disconnect()\n"

disconnectFuncs = disconnectFuncs[:-1]

print(disconnectFuncs)

print("############################################################ disable buttons ##########################################################")

disableFuncs = ""

lines = initial.split("\n")
for l in lines:
    disableFuncs += "def " + l[50] + "_press(self):\n    self.button_pressed('" + l[50] + "')\n    self.pushButton_" + str(l[16]) + str(l[17]) + ".setEnabled(False)\n"

disableFuncs = disableFuncs[:-1]

print(disableFuncs)

print("############################################################ restore all buttons ###########################################################")

restoreButtons = ""

lines = initial.split("\n")
for l in lines:
    restoreButtons += "self.pushButton_" + str(l[16]) + str(l[17]) + ".setEnabled(True)\n"

restoreButtons = restoreButtons[:-1]

print(restoreButtons)
