#!/usr/bin/env python
#coding=utf8

##########################################################################################
import os
import sys
import psutil
import resource
import getopt
# from random import randint
from datetime import datetime
from persistent import pDict, pList

##########################################################################################
def set_memory_limit(limit=1024):
	limit *= 1024*1024 # MegaByte
	rsrc = resource.RLIMIT_AS
	# soft, hard = resource.getrlimit(rsrc) # defualt is -1,-1 (no limit)
	resource.setrlimit(rsrc, (limit, limit)) #limit to one kilobyte
	soft, hard = resource.getrlimit(rsrc)
	return soft == limit and hard == limit

##########################################################################################
def getReadableSize(lv):
	"""
		'1.23 GB' 처럼 TB(TerraByte), GB(GigaByte), MB(MegaByte), KB(KilloByte) 로 표시
		:param lv: int 또는 long 형식의 값
		:return: 사람이 읽기 쉬운 형태의 바이트 문자열 값
	"""
	if not isinstance(lv, (int, long)):
		return '0'
	if lv >= 1024 * 1024 * 1024 * 1024:
		s = "%4.2f TB" % (float(lv) / (1024 * 1024 * 1024 * 1024))
	elif lv >= 1024 * 1024 * 1024:
		s = "%4.2f GB" % (float(lv) / (1024 * 1024 * 1024))
	elif lv >= 1024 * 1024:
		s = "%4.2f MB" % (float(lv) / (1024 * 1024))
	elif lv >= 1024:
		s = "%4.2f KB" % (float(lv) / 1024)
	else:
		s = "%d B" % lv
	return s

##########################################################################################
def print_heap(msg):
	# return msg
	rl = []
	if msg:
		# print msg,
		rl.append(msg)
	pid = os.getpid()
	p = psutil.Process(pid)
	# print(pid)
	for map in p.memory_maps(grouped=False):
		if '[heap]' in map.path:
			rl.append(getReadableSize(map.pss))
			break
	return ' '.join(rl)

##########################################################################################
def big_dict_test(persistent=False, limit=1024):
	sts = datetime.now()
	bd = dict() if not persistent else pDict()
	loop_limit = 200000
	print(print_heap('before loop [%s]'%loop_limit))
	for i in xrange(loop_limit):
		try:
			# k = randint(1,1000000)
			k = i
			bd[k] = '%s%s'%(k, '*'*1024)
			if i and i % 10000 == 0:
				print(print_heap('Dict %s inserted...'%i))
		except MemoryError:
			print("[%s] error" % i)
			return False
	print(print_heap('after loop [%s]' % loop_limit))
	print("bd[%s]=%s" % (loop_limit/2, bd[loop_limit/2]))
	for k in bd.keys():
		del bd[k]
	del bd
	print(print_heap('after delete [%s]' % loop_limit))
	ets = datetime.now()
	print("big_list_test takes %s"%(ets-sts))
	return True

##########################################################################################
def big_list_test(persistent=False, limit=1024):
	sts = datetime.now()
	bl = list() if not persistent else pList()
	loop_limit = 200000
	print(print_heap('before loop [%s]'%loop_limit))
	for i in xrange(loop_limit):
		try:
			bl.append('%s%s'%(i, '*'*1024))
			if i and i % 10000 == 0:
				print(print_heap('List %s inserted...'%i))
		except MemoryError:
			print("[%s] MemoryError" % i)
			return False
	print(print_heap('after loop [%s]' % loop_limit))
	print("bl[%s]=%s" % (loop_limit/2, bl[loop_limit/2]))
	del bl
	print(print_heap('after delete [%s]' % loop_limit))
	ets = datetime.now()
	print("big_list_test takes %s"%(ets-sts))
	return True

##########################################################################################
def usage(msg=None):
	if msg:
		sys.stderr.write('%s\n'%msg)
	sys.stderr.write('''usage:%s [options]
  set memory limit and raise malloc error
  [options] are:
    -h : show this message
    -p, --persistent : use persistent dict and list
    -l, --limit : memory limit in MegaBytes (mendotory)
''' % sys.argv[0])
	sys.exit(1)

##########################################################################################
if __name__ == '__main__':

	try:
		opts, args = getopt.getopt(sys.argv[1:], "hpl:",
		                           ["help", "persistent", 'limit'])
	except getopt.GetoptError, e:
		usage(str(e))
	Options = { 'persistent':False }
	for o, a in opts:
		if o in ("-h", "--help"):
			usage()
		elif o in ("-p", "--persistent"):
			Options['persistent'] = True
		elif o in ("-l", "--limit"):
			Options['limit'] = int(a)
	if 'limit' not in Options:
		usage('-l, --limit is mandotory')

	limit = Options['limit']
	print("set_memory_limit(%d)=%d" % (limit, set_memory_limit(limit)))
	if not big_list_test(**Options):
		sys.exit(2)
	if not big_dict_test(**Options):
		sys.exit(1)
