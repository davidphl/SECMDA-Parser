SECMDA-Parser
=============

Getting the Management Discussion & Analysis (MDA) section is a massive pain. MDA-Parser should help you get started
with pulling that information.

This is very much a work in progress and the regex still needs some work to reduce the number of false positives.

Running
-------
Simply pass the file path of the filing and you'll get back the filing date and the text
from the MDA section.

Support Methods
---------------
Currently this parser only supports 2 filings
* 10-K
* 10-Q