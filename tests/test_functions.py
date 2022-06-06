class AbstractionViolation(Exception):
	pass

def datatype(obj):
	return type(obj).__name__


class Abstract(object):
	def __add__(self, other):
		raise AbstractionViolation('can not add {} object to {}'.format(datatype(self), datatype(other)))


	def __radd__(self, other):
		raise AbstractionViolation('can not add {} object to {}'.format(datatype(self), datatype(other)))


	def __eq__(self, other):
		if isinstance(other, type(self)):
			return other is not self

		raise AbstractionViolation('can not use != on {} object and {}'.format(datatype(self), datatype(other)))



	def __bool__(self):
		raise AbstractionViolation('can not use {} object as a boolean'.format(datatype(self)))



	def __getitem__(self, index):
		raise AbstractionViolation('can not use [] notation on {} object'.format(datatype(self)))



	def __iter__(self):
		raise AbstractionViolation('can not iterate on {} object'.format(datatype(self)))



	def __len__(self):
		raise AbstractionViolation('can not use len notation on {} object'.format(datatype(self)))


	def __call__(self, *args, **kwargs):
		raise AbstractionViolation('can not call {} object'.format(datatype(self)))



	def __hash__(self):
		return id(self)



class User(Abstract):
	def __init__(self, name, review):
		self.a, self.b = name, {review_restaurant_name(r): r for r in reviews}


	def __repr__(self):
		return '<User {} {}>'.format(self.a, list(map(repr, self.b)))




make_user = User











