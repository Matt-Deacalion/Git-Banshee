#!/usr/bin/env python2

import os
import sys
import random
import string
import shutil

file_directory = os.path.dirname(__file__)
file_location = os.path.abspath( __file__ )
hooks_root = os.path.join(os.getcwd(), ".git", "hooks")
hooks_source = os.path.join(file_directory, "hooks")

hooks = {
    "merge":    [ os.path.join(hooks_root, "post-merge"),
                  os.path.join(hooks_source, "post-merge"), ],
    "commit":   [ os.path.join(hooks_root, "post-commit"),
                  os.path.join(hooks_source, "post-commit"), ],
    "checkout": [ os.path.join(hooks_root, "post-checkout"),
                  os.path.join(hooks_source, "post-checkout"), ],
}

def get_random_string(length=12):
    "Returns a randomly generated string."
    return "".join(random.choice(string.ascii_lowercase) for x in range(length))

def get_ident():
    "Returns the Git Banshee ident code for this repository."
    ident_file = os.path.join(os.getcwd(), ".git", "hooks", ".git-banshee")

    try:
        with open(ident_file, "r+") as f:
            ident = f.read()

            if not ident:
                ident = get_random_string()
                f.write(ident)
    except IOError:
        with open(ident_file, "w+") as f:
            ident = get_random_string()
            f.write(ident)

    return ident

def get_external_ip():
    "Returns the external ip address as a string."
    import urllib
    import re

    request = urllib.urlopen("http://checkip.dyndns.org").read()
    return re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", request)[0]

def is_installed():
    return any([os.path.exists(path[0]) for hook,path in hooks.iteritems()])

def install_hooks():
    ip = get_external_ip()

    if not is_installed():
        for hook, path in hooks.iteritems():
            shutil.copy2(path[1], path[0])
            os.chmod(path[0], 0755)

        print("Hooks have been installed, go to: http://{}/?hash={}".format(ip, get_ident()))
    else:
        print("Hooks are already installed, go to: http://{}/?hash={}".format(ip, get_ident()))
