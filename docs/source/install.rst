==========
Installing
==========

7i96 Configuration Tool

I now have a Debian deb for installing 7i96!!!

Download the `deb <https://github.com/jethornton/7i96/raw/master/deb_dist/python3-c7i96_1.2.1-1_all.deb>`_

Or use wget from a terminal
::

	wget https://github.com/jethornton/7i96/raw/master/deb_dist/python3-c7i96_1.2.1-1_all.deb

If you get `bash: wget: command not found` you can install it from a terminal with
::

	sudo apt install wget

Open the File Manager and right click on the file and open with Gdebi then install.

If you don't have Gdebi installed you can install it from a terminal
::

	sudo apt install gdebi

If you don't have LinuxCNC installed then the 7i96 Configuration tool
will show up in the Applications > Other menu otherwise it will be in
the CNC menu.

To flash firmware to the 7i96 you need to install 
`mesaflash <https://github.com/LinuxCNC/mesaflash>`_ from the LinuxCNC
repository.


OLD INSTALL INFO To Be Deleted Shortly
************************************************************************

1. Install required dependencies. In a terminal do:
::

    sudo apt install python3-pip python3-pyqt5 libpci-dev git

Note: some OS's might not have `python-setuptools` and you would need to
install it with apt install.

2. Install the 0.1.5 branch (stable) 7i96 Configuration Tool. In a terminal do:
::

    pip3 install git+https://github.com/jethornton/7i96.git@0.1.5


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


To upgrade the 0.1.5 branch (stable) 7i96 Configuration Tool. In a terminal do:
::

    pip3 install git+https://github.com/jethornton/7i96.git@0.1.5 --upgrade


To uninstall the 7i96 Configuration Tool In a terminal do:
::

    pip3 uninstall 7i96


To install the master branch:
::

    pip3 install git+https://github.com/jethornton/7i96.git
    

To upgrade the master branch:
::

    pip3 install git+https://github.com/jethornton/7i96.git --upgrade
