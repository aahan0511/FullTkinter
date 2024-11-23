# CTkMenuBar | https://github.com/Akascape/CTkMenuBar | `pip install CTkMenuBar`
from .dropdownMenu import CustomDropdownMenu as DropdownMenu
from .titleMenu import CTkTitleMenu as TitleMenu
from .menuBar import CTkMenuBar as MenuBar

# CTkMessageBox | https://github.com/Akascape/CTkMessagebox | `pip install CTkMessageBox`
from .messageBox import CTkMessagebox as MessageBox

# CTkColorPicker | https://github.com/Akascape/CTkColorPicker | `pip install CTkColorPicker`
from .colorPicker import AskColor
from .colorPickerWidget import CTkColorPicker as ColorPicker

# CTkTable | https://github.com/Akascape/CTkTable | `pip install CTkTable`
from .table import CTkTable as Table

# CustomTkinter | https://github.com/TomSchimansky/CustomTkinter | `pip install customtkinter`
from customtkinter import CTkButton as Button, \
    CTkCanvas as Canvas, \
    CTkCheckBox as CheckBox, \
    CTkComboBox as ComboBox, \
    CTkEntry as Entry, \
    CTkFrame as Frame, \
    CTkLabel as Label, \
    CTkOptionMenu as OptionMenu, \
    CTkProgressBar as ProgressBar, \
    CTkRadioButton as RadioButton, \
    CTkScrollbar as Scrollbar, \
    CTkSegmentedButton as SegmentedButton, \
    CTkSlider as Slider, \
    CTkSwitch as Switch, \
    CTkTabview as Tabview, \
    CTkTextbox as Textbox, \
    CTkScrollableFrame as ScrollableFrame
from customtkinter import AppearanceModeTracker, \
    FontManager, \
    ScalingTracker, \
    ThemeManager, \
    DrawEngine, \
    CTkImage
from customtkinter import CTk as Window, \
    CTkToplevel as Toplevel, \
    CTkInputDialog as InputDialog
from customtkinter import CTkFont as Font
from customtkinter import set_appearance_mode as setAppearanceMode, \
    get_appearance_mode as getAppearanceMode, \
    set_default_color_theme as setDefaultColorTheme, \
    set_widget_scaling as setWidgetScaling, \
    set_window_scaling as setWindowScaling, \
    deactivate_automatic_dpi_awareness as deactivateAutomaticDPIAwareness, \
    set_ctk_parent_class as setCTkParentClass

# TkinterMapView | https://github.com/TomSchimansky/CustomTkinter | pip install tkintermapview
from tkintermapview import TkinterMapView as MapView, \
    OfflineLoader, \
    convert_coordinates_to_address as convertCoordinatesToAddress, \
    convert_coordinates_to_country as convertCoordinatesToCountry, \
    convert_coordinates_to_city as convertCoordinatesToCity, \
    convert_address_to_coordinates as convertAddressToCoordinates, \
    decimal_to_osm as decimalToOSM, \
    osm_to_decimal as OSMToDecimal