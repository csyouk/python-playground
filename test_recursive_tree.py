def r_max(nxs):
	largest = None
	first_time = True
	for e in nxs:
		if type(e) == type([]):
			val = r_max(e)
		else:
			val = e
		if first_time or val > largest:
			largest = val
			first_time = False
	return largest

data = [2,5,[3,200,31,-3],9,952,[3,[4,869]]]
assert r_max(data) == 952
assert r_max(data) == 869
