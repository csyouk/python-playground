#!/usr/bin/env python
#coding=utf8

##########################################################################################
import os
import shelve
from random import randint

##########################################################################################
class pDict(object):
	#=====================================================================================
	FOLER='/ferret/tmp'
	INT_PREFIX='__int__'
	#=====================================================================================
	def _open(self):
		if not os.path.isdir(self.FOLER):
			self.FOLER = '/tmp'
		if not os.path.isdir(self.FOLER):
			raise IOError('Cannot wirte at folder "%s"' % self.FOLER)
		while (True):
			self.filename = '%s/.%08d.__dict__' % (self.FOLER, randint(1,99999999))
			if not os.path.exists(self.filename):
				break
		self.d = shelve.open(self.filename)
	#=====================================================================================
	def _close(self, is_delete=True):
		if self.d is not None:
			self.d.close()
			self.d = None
		if is_delete and os.path.exists(self.filename):
			os.remove(self.filename)
	#=====================================================================================
	def __init__(self, d={}):
		self.filename = None
		self.d = None
		self._open()
		if d and not isinstance(d, (dict, pDict)):
			raise ReferenceError('pDict construct need only dict or pDict type but <%s>'
				% str(type(d)))
		for k, v in d.items():
			self.__setitem__(k, v)
	#=====================================================================================
	def __del__(self):
		self._close()
	#=====================================================================================
	def __repr__(self):
		rl = list()
		rl.append('{')
		for i,k in enumerate(sorted(self.d.keys())):
			if i > 0: rl.append(',')
			rk = self.__r_keytransform__(k)
			if isinstance(rk, basestring):
				rk = '"%s"' % rk
			rv = self.d[k]
			if isinstance(rv, basestring):
				rv = '"%s"' % rv
			rl.append('%s:%s'%(rk,rv))
		rl.append('}')
		return ''.join(rl)
	#=====================================================================================
	def __getitem__(self, key):
		if isinstance(key, slice):
			return [ self.d[self.__keytransform__(k)]
			         for k in range(key.start, key.stop, key.step) ]
		return self.d[self.__keytransform__(key)]
	#=====================================================================================
	def __setitem__(self, key, value):
		self.d[self.__keytransform__(key)] = value
	#=====================================================================================
	def __delitem__(self, key):
		r = self.d[self.__keytransform__(key)]
		del self.d[self.__keytransform__(key)]
		return r
	#=====================================================================================
	def __iter__(self):
		return iter(self.d)
	#=====================================================================================
	def __len__(self):
		return len(self.d)
	#=====================================================================================
	def __keytransform__(self, key):
		if isinstance(key, basestring):
			return key
		if isinstance(key, (int, long)):
			return '%s%10d' % (self.INT_PREFIX, key)
		return str(key)
	#=====================================================================================
	def __r_keytransform__(self, key):
		if key.startswith(self.INT_PREFIX):
			return int(key[len(self.INT_PREFIX):].strip())
		return key
	#=====================================================================================
	def __contains__(self, key):
		# return self.__keytransform__(key) in self.d
		return self.has_key(key)
	#=====================================================================================
	def has_key(self, key):
		return self.d.has_key(self.__keytransform__(key))
	#=====================================================================================
	def keys(self):
		# for k in self.d.keys():
		# 	yield self.__r_keytransform__(k)
		return [ self.__r_keytransform__(k) for k in sorted(self.d.keys()) ]
	#=====================================================================================
	def values(self):
		vl = list()
		for k in sorted(self.d.keys()):
			# yield self.d[k]
			vl.append(self.d[k])
		return vl
	#=====================================================================================
	def items(self):
		for k in sorted(self.d.keys()):
			yield self.__r_keytransform__(k), self.d[k]

##########################################################################################
class pList(pDict):
	#=====================================================================================
	def __init__(self, l=[]):
		pDict.__init__(self)
		self.len = 0
		if l and not isinstance(l, (list, pList)):
			raise ReferenceError('pList construct need only list or pList type but <%s>'
			                     % str(type(l)))
		for v in l:
			self.append(v)
	#=====================================================================================
	def __repr__(self):
		rl = list()
		rl.append('[')
		for i in xrange(self.len):
			if i > 0: rl.append(',')
			rv = self.d[self.__keytransform__(i)]
			if isinstance(rv, basestring):
				rv = '"%s"' % rv
			rl.append('%s'%rv)
		rl.append(']')
		return ''.join(rl)
	#=====================================================================================
	def __setitem__(self, ndx, value):
		if ndx < 0 or ndx > self.len:
			raise IndexError('Invalid index <%s>' % ndx)
		self.d[self.__keytransform__(ndx)] = value
	#=====================================================================================
	def __delitem__(self, ndx):
		if ndx < 0 or ndx >= self.len:
			raise IndexError('Invalid index <%s>' % ndx)
		r = self.d[self.__keytransform__(ndx)]
		del self.d[self.__keytransform__(ndx)]
		for i in range(ndx, self.len-1):
			self.d[self.__keytransform__(i)] = self.d[self.__keytransform__(i+1)]
		self.len -= 1
		if self.len > 0:
			del self.d[self.__keytransform__(self.len)]
		return r
	#=====================================================================================
	def __contains__(self, v):
		return v in self.values()
	#=====================================================================================
	def __iter__(self):
		return iter(self.values())
	#=====================================================================================
	def append(self, v):
		self.__setitem__(self.len, v)
		self.len += 1
	#=====================================================================================
	def extend(self, l):
		for item in l:
			self.append(item)
		self.len += len(l)

##########################################################################################
def test_pDict():
	d = {
		'abc':111,
		123:"def"
	}
	d = pDict(d)
	print('d=%s' % d)
	print('123 in d? %s' % (123 in d,))
	print('d.has_key(23)? %s' % d.has_key(23))
	for i in xrange(10):
		d[i] = '%s_%s' % (i, '*'*1)
	print('d=%s' % d)
	for k, v in d.items():
		print k, v
		if isinstance(k,int) and k % 3 == 0:
			del d[k]
	print('d=%s' % d)
	print('len(d)=%s' % len(d))
	for k, v in d.items():
		print k, v
	print("d.keys()=%s"%d.keys())
	print("d.values()=%s" % d.values())

##########################################################################################
def test_pList():
	l = [
		'abc',
		123
	]
	l = pList(l)
	print('l=%s' % l)
	print('len(l)=%s' % len(l))
	print('"abc" in l? %s' % ("abc" in l,))
	print('23 in l? %s' % (23 in l,))
	for i in xrange(10):
		l.append('%s_%s' % (i, '*'*1))
	print('l=%s' % l)
	# for v in l: print v
	for i in range(len(l)-1,-1,-1):
		v = l[i]
		print "[%s] %s"%(i, v)
		if i % 3 == 0:
			del l[i]
			print('l=%s' % l)
	print('l=%s' % l)


##########################################################################################
def test_shelve():
	filename='/tmp/foo.dic'
	d = shelve.open(filename) # open -- file may get suffix added by low-level
	key = 'foo_key'
	data = 'bar_data'*3

	d[key] = data	# store data at key (overwrites old data if
	print d
	data = d[key]	# retrieve a COPY of data at key (raise KeyError if no
	print data
	flag = key in d	# true if the key exists
	print flag
	del d[key]		# delete data stored at key (raises KeyError
	flag = d.has_key(key)	# true if the key exists
	print flag
	klist = d.keys() # a list of all existing keys (slow!)
	print klist
	# as d was opened WITHOUT writeback=True, beware:
	d['xx'] = range(4)  # this works as expected, but...
	d['xx'].append(5)	# *this doesn't!* -- d['xx'] is STILL range(4)!

	# having opened d without writeback=True, you need to code carefully:
	temp = d['xx']		# extracts the copy
	temp.append(5)		# mutates the copy
	d['xx'] = temp		# stores the copy right back, to persist it

	# or, d=shelve.open(filename,writeback=True) would let you just code
	# d['xx'].append(5) and have it work as expected, BUT it would also
	# consume more memory and make the d.close() operation slower.

	d.close()		 # close it

##########################################################################################
if __name__ == '__main__':
	# test_pDict()
	test_pList()
