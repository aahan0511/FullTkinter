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

from macosx.basewidgets.marquee_base import MarqueeBase


class Marquee(MarqueeBase):
    """
Marquee widget.

Use `Marquee` for creating scrolling text which moves from right to left only if the text does not fit completely on the window.

- Configurable options for a Marquee widget. Syntax: `Marquee(root, options=value, ...)`

  | Options               | Description                                                                                                                                                                           |
  | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | _bg or background_    | The background color of the marquee area.                                                                                                                                             |
  | _bd or borderwidth_   | Width of the border around the marquee. The default value is two pixels.                                                                                                              |
  | _cursor_              | Cursor that appears when the mouse is over this marquee.                                                                                                                              |
  | _disabledforeground_  | The color to use when the button is disabled. The default is systemspecific.                                                                                                          |
  | _end_delay_           | Time to wait before reseting at the end of movement. Default is 1000 ms.                                                                                                              |
  | _font_                | If you are displaying text in this marquee with the text option, the font option specifies in what font that text will be displayed.                                                  |
  | _fg or foreground_    | If you are displaying text in this marquee, this option specifies the color of the text.                                                                                              |
  | _fps_                 | Set fps(frames per seconds) indirectly is the speed of text movement. Default is 30.                                                                                                  |
  | _height_              | The height of the _Marquee_ is in pixels. If this option is not set, the _Marquee_ will be sized to fit its contents.                                                                 |
  | _highlightbackground_ | Color of the focus highlight when the widget does not have focus.                                                                                                                     |
  | _highlightcolor_      | The color of the focus highlight when the widget has focus.                                                                                                                           |
  | _highlightthickness_  | The thickness of the focus highlight.                                                                                                                                                 |
  | _initial_delay_       | Time to wait before starting the movement of the text. Default is 1000 ms.                                                                                                            |
  | _justify_             | Specifies how multiple lines of text will be aligned with respect to each other: _tk.LEFT_ for flush left, _tk.CENTER_ for centered (the default), or _tk.RIGHT_ for right-justified. |
  | _left_margin_         | Text to keep moving to right after last character is displayed before reseting.                                                                                                       |
  | _smoothness_          | Millisecond delay in movement of each frame. Default is 1 ms.                                                                                                                         |
  | _state_               | By default, a _Marquee_ widget is in the _tk.NORMAL_ state. Set this option to _tk.DISABLED_ to make it unresponsive to mouse events.                                                 |
  | _relief_              | Specifies the appearance of a decorative border around the _Marquee_. The default is _tk.FLAT_; for other values.                                                                     |
  | _takefocus_           | Normally, focus does not cycle through _Marquee_ widgets. If you want this widget to be visited by the focus, set `takefocus=1`.                                                      |
  | _text_                | To display one or more lines of text in a _Marquee_ widget, set this option to a string containing the text. Internal newlines ('\n') will force a line break.                        |
  | _width_               | The width of the _Marquee_ is in pixels. If this option is not set, the _Marquee_ will be sized to fit its contents.                                                                  |

- Methods on `Marquee` widget objects:

  | Methods              | Description                                                                                                                                   |
  | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
  | _.reset()_           | Resets the position of the text to default.                                                                                                   |
  | _.stop(reset: bool)_ | Stops the moving text to the current position. Set parameter `reset=True` to stop the movement and reset the position of the text to default. |
  | _.play(reset: bool)_ | Plays the stopped text from the current position. Set parameter `reset=True` to play from the default position.                               |

- **Example:**

  ```python
  from tkinter import *
  from tkmacosx import Marquee

  text1 = \"""This text will move from right to left \
  if does not fit the window.\"""
  text2 = \"""Please hover over the text to move it. \
  This text will move only if the cursor hovers over \
  the text widget.\"""

  root = Tk()
  root['bg'] = '#333'
  Marquee(root, bg='#FEE715', fg='#101820', text=text1).pack(pady=10)
  m = Marquee(root, fg='#FEE715', bg='#101820', text=text2)
  m.pack(pady=(0,10), padx=10)
  m.stop(True)
  m.bind('<Enter>', lambda _: m.play())
  m.bind('<Leave>', lambda _: m.stop())
  root.mainloop()
  ```

   <p align="center">
      <img src="https://user-images.githubusercontent.com/46227224/114269092-70fb1200-9a22-11eb-99f0-08f87078ff53.gif">
   </p>

---

Author: Saad Mairaj | https://github.com/Saadmairaj
    """

    def __init__(self, master=None, cnf={}, **kw):
        """Use `Marquee` for creating scrolling text which moves from 
        right to left only if the text does not fit completely.

        ### Args:
        - `text`: Give a string to display.
        - `font`: Font of the text.
        - `fg`: Set foreground color of the text.
        - `fps`: Set fps(frames per seconds).
        - `left_margin`: Set left margin to make text move further in right direction before reset.
        - `initial_delay`: Delay before text start to move.
        - `end_delay`: Delay before text reset.
        - `smoothness`: Set the smoothness of the animation.

        ### Example: 
        ```
        root=tk.Tk()
        marquee = Marquee(root, 
                        text='This text will move from right to left if does not fit the window.')
        marquee.pack()
        root.mainloop()
        ```

        ### To move the text when cursor is over the text then follow the below example.
        ```
        text = "Please hover over the text to move it. "
               "This text will move only if the cursor "
               "hovers over the text widget."
        root = tk.Tk()
        m = tkm.Marquee(root, bg='lightgreen', text=text)
        m.pack()
        m.stop(True)
        m.bind('<Enter>', lambda _: m.play())
        m.bind('<Leave>', lambda _: m.stop())
        root.mainloop()
        ```"""
        MarqueeBase.__init__(self, master=master, cnf=cnf, **kw)

    def reset(self):
        """Reset the text postion."""
        self._reset(True)
        self._stop_state = False

    def stop(self, reset=False):
        """Stop the text movement."""
        if reset:
            self.reset()
        self._stop_state = True
        self.after_cancel(self.after_id)
        self.after_id = ' '

    def play(self, reset=False):
        """Play/continue the text movement."""
        if not self._stop_state and not reset:
            return
        self._stop_state = False
        if reset:
            self.reset()
        self._animate()
