#!/usr/bin/env python3

import rpyc
c = rpyc.connect("localhost", 18861)
print(c.root)
print(c.root.exposed_get_answer())
print(c.root.get_answer())