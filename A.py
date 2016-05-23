class kwayHeap:


	def __init__(self,k,f):
		self._data=[]
		self._node=k
		self._f=f

	def is_empty(self):
		return len(self._data)==0

	def min(self):
		if self.is_empty():
			raise Empty('Priority queue is empty.')
		item=self._data[0]
		return item

	def remove_min(self):
		if self.is_empty():
			raise Empty('Priority queue is empty.')
		self._swap(0,len(self._data)-1)
		item=self._data.pop()
		self._downheap(0)
		return item

	def add(self,x):
		self._data.append(x)
		self._upheap(len(self._data)-1)

	def index_of_children(self,j):
		index=self._node*j+1
		while index<len(self._data) and index<=self._node*j+self._node:
			yield index
			index+=1

	def _parent(self,j):
		return (j-1)//self._node

	def _swap(self,i,j):
		self._data[i],self._data[j]=self._data[j],self._data[i]

	def _upheap(self,j):
		parent=self._parent(j)
		if j>0 and self._f(self._data[j],self._data[parent]):
			self._swap(j,parent)
			self._upheap(parent)

	def _downheap(self,j):
		if self._node*j+1<len(self._data):
			smallchild=self._node*j+1
			for i in self.index_of_children(j):
				if self._f(self._data[i],self._data[smallchild]):
					smallchild=i
			if self._f(self._data[smallchild],self._data[j]) and self._f(smallchild,len(self._data)):
				self._swap(j,smallchild)
				self._downheap(smallchild)
	def get(self):
		print(self._data)

def f(x,y):
	return x<y

a=kwayHeap(3,f)
a.add(2)
a.add(3)
a.add(7)
a.add(5)
a.add(6)
a.add(5)
b=a.remove_min()
a.get()




		