from json import loads, dumps

def load(fp, **kw):
	return [loads(obj, **kw) for obj in fp]

def dumps(objs, fp, **kw):
	for obj in objs:
		fp.write(dumps(obj, **kw))
		fp.write('\n')