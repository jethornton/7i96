==========
Installing
==========

7i96 Configuration Tool

I now have a Debian deb for installing 7i96!!!

Download the `deb <https://github.com/jethornton/7i96/raw/master/deb_dist/python3-c7i96_1.2.2-1_all.deb>`_

Or use wget from a terminal
::

	wget https://github.com/jethornton/7i96/raw/master/deb_dist/python3-c7i96_1.2.2-1_all.deb

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

To uninstall the 7i96 Configuration Tool right click on the .deb file
and open with Gdebi and select `Remove Package`.

To upgrade the 7i96 Configuration Tool delete the .deb file and download
a fresh copy then right click on the .deb file and open with Gdebi and
select `Reinstall Package`.
