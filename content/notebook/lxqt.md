---
title: lxqt shortcuts
---

### Maximize left/right

```xml
<keyboard>
  <chainQuitKey>C-g</chainQuitKey>

  <!-- Keybindings for desktop switching -->
  <keybind key="C-A-Left">
    <action name="GoToDesktop"><to>left</to><wrap>no</wrap></action>
  </keybind>
  <keybind key="C-A-Right">
    <action name="GoToDesktop"><to>right</to><wrap>no</wrap></action>
  </keybind>
  <keybind key="C-A-Up">
    <action name="GoToDesktop"><to>up</to><wrap>no</wrap></action>
  </keybind>
  <keybind key="C-A-Down">
    <action name="GoToDesktop"><to>down</to><wrap>no</wrap></action>
  </keybind>

  <keybind key="C-S-A-Left">
    <action name="SendToDesktop"><to>left</to><wrap>no</wrap></action>
  </keybind>
  <keybind key="C-S-A-Right">
    <action name="SendToDesktop"><to>right</to><wrap>no</wrap></action>
  </keybind>
<!--
-->
  <keybind key="C-S-A-Up">
    <action name="SendToDesktop"><to>up</to><wrap>no</wrap></action>
    </keybind>
  <keybind key="C-S-A-Down">
    <action name="SendToDesktop"><to>down</to><wrap>no</wrap></action>
  </keybind>
<!-- 
  <keybind key="W-F1">
    <action name="GoToDesktop"><to>1</to></action>
  </keybind>
  <keybind key="W-F2">
    <action name="GoToDesktop"><to>2</to></action>
  </keybind>
  <keybind key="W-F3">
    <action name="GoToDesktop"><to>3</to></action>
  </keybind>
  <keybind key="W-F4">
    <action name="GoToDesktop"><to>4</to></action>
  </keybind> 
-->
  <keybind key="W-m">
    <action name="ToggleShowDesktop"/>
  </keybind>

  <!-- Keybindings for windows -->
  <keybind key="A-F4">
    <action name="Close"/>
  </keybind>
  <keybind key="A-Escape">
    <action name="Lower"/>
    <action name="FocusToBottom"/>
    <action name="Unfocus"/>
  </keybind>
  <keybind key="A-space">
    <action name="ShowMenu"><menu>client-menu</menu></action>
  </keybind>
  <!-- Take a screenshot of the current window with scrot when Alt+Print are pressed -->
  <keybind key="A-Print">
    <action name="Execute"><command>scrot -s</command></action>
  </keybind>

  <!-- Keybindings for window switching -->
  <keybind key="A-Tab">
    <action name="NextWindow">
      <finalactions>
        <action name="Focus"/>
        <action name="Raise"/>
        <action name="Unshade"/>
      </finalactions>
    </action>
  </keybind>
  <keybind key="A-S-Tab">
    <action name="PreviousWindow">
      <finalactions>
        <action name="Focus"/>
        <action name="Raise"/>
        <action name="Unshade"/>
      </finalactions>
    </action>
  </keybind>
  <keybind key="C-A-Tab">
    <action name="NextWindow">
      <panels>yes</panels><desktop>yes</desktop>
      <finalactions>
        <action name="Focus"/>
        <action name="Raise"/>
        <action name="Unshade"/>
      </finalactions>
    </action>
  </keybind>

  <!-- Keybindings for window switching with the arrow keys -->
<!--
  <keybind key="W-S-Right">
    <action name="DirectionalCycleWindows">
      <direction>right</direction>
    </action>
  </keybind>
  <keybind key="W-S-Left">
    <action name="DirectionalCycleWindows">
      <direction>left</direction>
    </action>
  </keybind>
  <keybind key="W-S-Up">
    <action name="DirectionalCycleWindows">
      <direction>up</direction>
    </action>
  </keybind>
  <keybind key="W-S-Down">
    <action name="DirectionalCycleWindows">
      <direction>down</direction>
    </action>
  </keybind>
-->
  <!-- Keybindings for running applications -->
  <keybind key="W-e">
    <action name="Execute">
      <startupnotify>
        <enabled>true</enabled>
        <name>Konqueror</name>
      </startupnotify>
      <command>kfmclient openProfile filemanagement</command>
    </action>
  </keybind>
  <!-- Launch scrot when Print is pressed -->
  <keybind key="Print">
    <action name="Execute"><command>scrot</command></action>
  </keybind>

<keybind key="S-A-Left">
    <action name="UnmaximizeFull"/>
    <action name="MaximizeVert"/>
    <action name="MoveResizeTo">
        <width>50%</width>
    </action>
    <action name="MoveToEdge"><direction>west</direction></action>
</keybind>
<keybind key="S-A-Right">
    <action name="UnmaximizeFull"/>
    <action name="MaximizeVert"/>
    <action name="MoveResizeTo">
        <width>50%</width>
    </action>
    <action name="MoveToEdge"><direction>east</direction></action>
</keybind>
<keybind key="S-A-Down">
   <action name="Unmaximize"/>
</keybind>
<keybind key="S-A-Up">
   <action name="Maximize"/>
</keybind>
</keyboard>
```

### Tiling

```bash
<!-- Vertical tiling -->
<keybind key="C-W-v">
  <action name="UnmaximizeFull"/>
  <action name="MoveResizeTo">
    <width>50%</width>
  </action>
  <action name="MaximizeVert"/>
  <action name="MoveResizeTo">
    <x>0</x>
    <y>0</y>
  </action>
  <action name="NextWindow">
    <interactive>no</interactive>
    <dialog>none</dialog>
    <finalactions>
      <action name="UnmaximizeFull"/>
      <action name="MoveResizeTo">
        <width>50%</width>
      </action>
      <action name="MaximizeVert"/>
      <action name="MoveResizeTo">
        <x>-0</x>
        <y>0</y>
      </action>
    </finalactions>
  </action>
</keybind>

<!-- Horizontal tiling -->
<keybind key="C-W-h">
  <action name="UnmaximizeFull"/>
  <action name="MoveResizeTo">
    <height>50%</height>
  </action>
  <action name="MaximizeHorz"/>
  <action name="MoveResizeTo">
    <x>0</x>
    <y>0</y>
  </action>
  <action name="NextWindow">
    <interactive>no</interactive>
    <dialog>none</dialog>
    <finalactions>
      <action name="UnmaximizeFull"/>
      <action name="MoveResizeTo">
        <height>50%</height>
      </action>
      <action name="MaximizeHorz"/>
      <action name="MoveResizeTo">
        <x>0</x>
        <y>-0</y>
      </action>
    </finalactions>
  </action>
</keybind>

<!-- Restore window dimensions -->
<keybind key="C-W-r">
  <action name="UnmaximizeFull"/>
  <action name="NextWindow">
    <interactive>no</interactive>
    <dialog>none</dialog>
    <finalactions>
      <action name="UnmaximizeFull"/>
    </finalactions>
  </action> 
</keybind>
```

## Set up XRDP

from here: <https://code.luasoftware.com/tutorials/linux/lubuntu-setup-remote-desktop-with-xrdp>

```bash
sudo apt-get install xrdp
lxsession -e LXDE -s Lubuntu
sudo service xrdp restart
```

## External Resources

* <https://askubuntu.com/questions/516303/tiling-windows-horizontally-and-vertically-under-lubuntu-lxde-openbox>
* <https://askubuntu.com/questions/1409509/is-it-possible-in-lxqt-lubuntu-22-04-to-maximize-left-right-as-in-lxde-lubunt>
* <https://code.luasoftware.com/tutorials/linux/lubuntu-setup-remote-desktop-with-xrdp>
