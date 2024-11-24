#                       Copyright 2021 Saad Mairaj
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import tkinter

# patch to make tkinter.Variable with multiple options of widgets.
from macosx.utils.colorvar_patches import patch
patch()


class ColorVar(tkinter.Variable):
    """
Value holder for HEX color. Default is white

ColorVar of tkmacosx set same color to each widget it is assigned to. As ColorVar is a tkinter variable wrapper so it will change the color of widgets whenever the change is made to ColorVar instances. ColorVar takes HEX values and all the color names which tkinter supports but the `get()` method returns only the HEX value. It will work with all of the following keyword arguments of different widgets _(eg:- `Canvas`, `Frame`, `Button`, `Label`, Canvas items, ...)_. **_'fg', 'foreground', 'bg', 'background', 'activebackground', 'activeforeground', 'disabledforeground', 'highlightbackground', 'highlightcolor', 'selectforeground', 'readonlybackground', 'selectbackground', 'insertbackground', 'disabledbackground', 'activefill', 'activeoutline', 'disabledfill','disabledoutline', 'fill', 'outline'_** _(might work with more but have not tested)._

- Configurable options for a ColorVar variable. Syntax: `ColorVar(root, options=value, ...)`

  | Options | Description                                                                                                                                                   |
  | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | _value_ | The value is an optional value (defaults to "").                                                                                                              |
  | _name_  | The name is an optional Tcl name (defaults to PY*VARnum). If \_name* matches an existing variable and _value_ is omitted then the existing value is retained. |

- Methods on `ColorVar` variable objects:

  | Methods            | Description                                                                                                                                                |
  | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | _.get()_           | Returns the current value of the variable.                                                                                                                 |
  | _.set(value: str)_ | Changes the current value of the variable. If any widget options are slaved to this variable, those widgets will be updated when the main loop next idles. |

- **Example:**

  ```python
  from tkinter import Tk, Label
  from tkmacosx import ColorVar, Button, gradient

  root = Tk()
  root['bg'] = '#333'
  root.geometry('200x200')

  def change_color(c=0):
     if c >= len(color_list): c=0
     color.set(color_list[c])
     root.after(50, change_color, c+1)

  color = ColorVar()
  color_list = gradient(200)
  L = Label(root, textvariable=color, bg='#333', fg=color)
  L.pack(fill='x', expand=1, padx=10, pady=10)
  B = Button(root, textvariable=color, bg=color, borderless=1, activeforeground=color)
  B.pack(fill='x', expand=1, padx=10, pady=10)

  change_color()
  root.mainloop()
  ```

   <p align="center">
      <img src="https://user-images.githubusercontent.com/46227224/114269131-b0c1f980-9a22-11eb-8f2a-13575329f71c.gif">
   </p>

---

Author: Saad Mairaj | https://github.com/Saadmairaj
    """

    _default = "white"

    def __init__(self, master=None, value=None, name=None):
        """Construct a color variable. (bg, fg, ..)

        MASTER can be given as master widget.
        VALUE is an optional value (defaults to "")
        NAME is an optional Tcl name (defaults to PY_VARnum).

        If NAME matches an existing variable and VALUE is omitted
        then the existing value is retained.
        """
        tkinter.Variable.__init__(self, master, value, name)

    def set(self, value):
        """Set the variable to VALUE."""
        self._root.winfo_rgb(value)
        return self._tk.globalsetvar(self._name, value)
    initialize = set

    def get(self):
        """Return value of variable color."""
        value = self._tk.globalgetvar(self._name)
        self._root.winfo_rgb(value)
        return str(value)
