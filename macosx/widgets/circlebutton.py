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

from macosx.basewidgets.button_base import ButtonBase


class CircleButton(ButtonBase):
    """
Colorscale is a new style color selector which is an alternate to tkinter's colorchooser.

- Configurable options for a Colorscale widget. Syntax: `Colorscale(root, options=value, ...)`

  | Options               | Description                                                                                                                                                                                                                                                                                       |
  | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | _bd or borderwidth_   | Width of the border around the outside of the _Colorscale_. The default is two pixels.                                                                                                                                                                                                            |
  | _command_             | A function or method with a parameter that is called when the slider is moved or scrolled and an argument is paased to the callback. The callback can be a function, bound method, or any other callable Python object. If this option is not used, nothing will happen when the slider is moved. |
  | _cursor_              | Cursor used in the _Colorscale_.                                                                                                                                                                                                                                                                  |
  | _gradient_            | Takes tuple of two colors. Two colors are required to form a gradient (`sequence[FROM, TO]`, For example: A tuple of `tuple('white', 'black')` will create a _Colorscale_ from _WHITE_ to _BLACK_ color). By default is complete color gradient.                                                  |
  | _height_              | Size of the _Colorscale_ in the Y dimension.                                                                                                                                                                                                                                                      |
  | _highlightbackground_ | Color of the focus highlight when the widget does not have focus.                                                                                                                                                                                                                                 |
  | _highlightcolor_      | Color is shown in the focus highlight.                                                                                                                                                                                                                                                            |
  | _highlightthickness_  | The thickness of the focus highlight. The default value is 1.                                                                                                                                                                                                                                     |
  | _mousewheel_          | Move the slider with mousewheel with _True._ By default the option is set _False._                                                                                                                                                                                                                |
  | _orient_              | Set the orientation _(VERTICAL, HORIZONTAL)_. By default is VERTICAL.                                                                                                                                                                                                                             |
  | _relief_              | The relief style of the _Colorscale_. Default is tk.FLAT.                                                                                                                                                                                                                                         |
  | _showinfo_            | Shows hex or rbg while selecting color.                                                                                                                                                                                                                                                           |
  | _showinfodelay_       | Delay before the show info disappears _(in ms)_.                                                                                                                                                                                                                                                  |
  | _takefocus_           | Normally, focus will cycle through this widget with the tab key only if there are keyboard bindings set for it (see Section 54, “Events”for an overview of keyboard bindings). If you set this option to 1, the focus will always visit this widget. Set it to '' to get the default behavior.    |
  | _value_               | Get either 'RGB' or 'HEX'. By deafult is hex.                                                                                                                                                                                                                                                     |
  | _variable_            | Associates a Tkinter variable (usually a _tk.StringVar_, _tkm.ColorVar_). If the slider is moved the value of the variable changes as well.                                                                                                                                                       |
  | _width_               | Size of the _Colorscale_ in the X dimension.                                                                                                                                                                                                                                                      |

- **Example:**

  ```python
  from tkinter import *
  from tkmacosx import Colorscale, ColorVar

  root = Tk()
  root['bg'] = '#333'
  bgvar = ColorVar(value='#333')
  fgvar = ColorVar(value='white')
  Label(root, text="I am a Label, Hello! :-)",bg=bgvar, fg=fgvar).pack(pady=10)
  Colorscale(root, value='hex', variable=bgvar, mousewheel=1).pack(padx=20)
  Colorscale(root, value='hex', variable=bgvar, mousewheel=1,
          gradient=('pink', 'purple')).pack(pady=10)
  Colorscale(root, value='hex', variable=fgvar, mousewheel=1,
          gradient=('lightgreen', 'orange')).pack()
  Colorscale(root, value='hex', variable=fgvar, mousewheel=1,
          gradient=('white', '#89ABE3')).pack(pady=10)

  root.mainloop()
  ```

   <p align="center">
      <img src="https://user-images.githubusercontent.com/46227224/114269070-55900700-9a22-11eb-8de5-38885fad5cf8.gif">
   </p>

---

Author: Saad Mairaj | https://github.com/Saadmairaj
    """

    def __init__(self, master=None, cnf={}, **kw):
        """
        Circle shaped Button supports almost all options of a tkinter button 
        and have some few more useful options such as 'activebackground', overbackground', 
        'overforeground', 'activeimage', 'activeforeground', 'borderless' and much more. 

        To check all the configurable options for CircleButton run `print(CircleButton().keys())`.

        Example:
        ```
        import tkinter as tk
        import tkmacosx as tkm

        root = tk.Tk()
        cb = tkm.CircleButton(root, text='Hello')
        cb.pack()
        root.mainloop()
        ```
        """
        ButtonBase.__init__(self, 'circle', master, cnf, **kw)
