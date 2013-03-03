Raspberry Filling
=============
A collection of programs and accompanying schematics for various projects using the Raspberry Pi GPIO system.

Program source can be found in the programs directory (note that this includes a submodule 
for the pi-crust repo which is used in all the contained programs).  Hardware 
schematics can be found in the schematics directory.  The naming convention 
should be fairly self-explanatory but in case it isn't, programs are named 
with whether they are using the bus or parallel wrapper for GPIO, followed 
by the name of the program.  So, for the bus version of the binary clock program, 
the file is:
	raspi_bus_binaryClock.py
Likewise, for the parallel version:
	raspi_parallel_binaryClock.py
	
If you intend to convert between bus and parallel or you want to develop your own 
software that makes use of the pi-crust GPIO wrappers, take a look at the [documentation](https://github.com/thenaterhood/pi-crust/blob/master/README.md).

Contents
------------
	binaryClock		a binary clock.  Outputs on an array of 8 LEDs.


LICENSE
------------

thenaterhood/basically-ti-basic repository (c) 2012-2013 Nate Levesque (TheNaterhood), [www.thenaterhood.com](http://www.thenaterhood.com)

[![Creative Commons License](http://i.creativecommons.org/l/by-sa/3.0/88x31.png)](http://creativecommons.org/licenses/by-sa/3.0/)

TL;DR: You can use, copy and modify this SO LONG AS you credit me and distribute your remixes with the same license.

This work is licensed under the [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/).

You should have received a copy of the license along with this
work. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/ or send
a letter to Creative Commons, 444 Castro Street, Suite 900, Mountain View, California, 94041, USA.
