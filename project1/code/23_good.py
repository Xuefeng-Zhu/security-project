#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           ��7��Y�?-��dDM���I�^9�k0�����E�� w��@.6�F�#�s��n�hIA�/�hMU����0��Ũ��6"(�-I{X�+��-�?W.�Ⱦs�����Y�}n�s'P!"�#��*"""
from hashlib import sha256
if (sha256(blob).hexdigest() == "1d24dc79660781e1ca94fce1710ca72d95977a4bfb3e6844b5f154df5cf83cd8"):
	print "Prepare to be destroyed!"
else:
	print "I come in peace."
