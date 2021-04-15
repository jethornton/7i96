================
Smart Serial Tab
================

Basic support for a single Smart Serial Card.

If the pin you need is not shown then select `Signal Only` and the configuration
tool will create a net line in the sserial.hal file like this:
::

  net ss7i73in_0 hm2_7i96.0.7i73.0.0.input-00 <=  
  net ss7i73out_0 hm2_7i96.0.7i84.0.0.output-00 =>
