*****************
Git Banshee, why?
*****************

Because I want **sound effects** to go with my git commands… and I want them to work everywhere: a shell, a GUI, a Putty session.


Installing
==========

.. code-block:: bash

    $ pip install GitBanshee

Using
=====


1. cd into any git repository
-----------------------------

.. code-block:: bash

    $ cd flask/

2. type the `git-banshee` command
---------------------------------

.. code-block:: bash

    $ git-banshee
    > Hooks have been installed, go to: http://205.186.163.125/?hash=yawubgzjlxlb
    > Server running

3. go to the url. Now whenever a ‘commit’, ‘merge’ or ‘checkout’ happen whilst the server is running, a sound effect will be played in the browser.
---------------------------------------------------------------------------------------------------------------------------------------------------

Todo and ideas
==============

+ Daemon mode for server
+ Usable way to choose sounds
+ Pretty web page
+ More sounds

### Licence
Copyright © 2013—2014 [Matt Deacalion Stevens](http://dirtymonkey.co.uk), released under [The MIT Licence](http://deacalion.mit-license.org/).
