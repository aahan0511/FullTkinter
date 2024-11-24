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

import ast
import tkinter


class DictVar(tkinter.Variable):
    """
#### Value holder for Dictionaries.
Get a specific value by getting the key from this \
`get(self, key=None, d=None)` method if exists in the dictionary. \n
if `key=None` it will return the complete dictionary.

DictVar of tkmacosx stores python dictionary. It is very similar to tkinter `StringVar` with few modifications to it. `DictVar.get()` returns an instance of `dict` type whereas StringVar returns `str` type also DictVar method `get()` is a bit different `get(key=None, d=None)` get a key from `get()` method if `key=None` it will return the complete dictionary.

- Configurable options for a DictVar variable. Syntax: `DictVar(root, options=value, ...)`

  | Options | Description                                                                                                                                                   |
  | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | _value_ | The value is an optional value (defaults to {}).                                                                                                              |
  | _name_  | The name is an optional Tcl name (defaults to PY*VARnum). If \_name* matches an existing variable and _value_ is omitted then the existing value is retained. |

- Methods on `DictVar` variable objects:

  | Methods                            | Description                                                                                                                                                |
  | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | _.get(key: any=None, d: any=None)_ | Returns the current value of the variable. To get a specific value of dictionary use `key`, give a default value to `d` if the `key` is not available.     |
  | _set(value: str)_                  | Changes the current value of the variable. If any widget options are slaved to this variable, those widgets will be updated when the main loop next idles. |

- **Example:**

  ```python
  from tkinter import *
  from tkmacosx import DictVar

  root = Tk()
  dictionary = DictVar(value = {'width': 100, 'height': 200})

  print(type(dictionary.get()))
  print(dictionary.get())
  print(dictionary.get('width'))
  ```

---

Author: Saad Mairaj | https://github.com/Saadmairaj
    """
    _default = {}

    def __init__(self, master=None, value=None, name=None):
        """Construct a string variable.

        MASTER can be given as master widget.
        VALUE is an optional value (defaults to {})
        NAME is an optional Tcl name (defaults to PY_VARnum).

        If NAME matches an existing variable and VALUE is omitted
        then the existing value is retained.
        """
        tkinter.Variable.__init__(self, master, value, name)

    def get(self, key=None, d=None):
        """Return value of variable as string."""
        value = self._tk.globalgetvar(self._name)
        if not isinstance(value, dict):
            value = ast.literal_eval(value)
        if key:
            return value.get(key, d)
        return value
