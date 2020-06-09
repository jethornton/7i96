==========
Installing
==========

7i96 Configuration Tool

1. Install required dependencies. In a terminal do:
::

    sudo apt install python3-pip python3-pyqt5 libpci-dev git

Note: some OS's might not have `python-setuptools` and you would need to
install it with apt install.

2. Install the 7i96 Configuration Tool. In a terminal do:
::

    pip3 install git+https://github.com/jethornton/7i96.git

3. Create a file in your home directory called ``.xsessionrc`` and add the
following if your using Debian 9 then log out and back in or reboot the PC.

::

  if [ -d $HOME/.local/bin ]; then
    export PATH="$HOME/.local/bin:$PATH"
  fi

5. Follow the instructions at https://github.com/LinuxCNC/mesaflash to install
Mesaflash.

4. Run the 7i96 Configuration Tool. In a terminal do:
::

    7i96


To upgrade the 7i96 Configuration Tool. In a terminal do:
::

    pip3 install git+https://github.com/jethornton/7i96.git --upgrade


To uninstall the 7i96 Configuration Tool In a terminal do:
::

    pip3 uninstall 7i96

