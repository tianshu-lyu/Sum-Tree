from heap_priority_queue import newHeapPriorityQueue
import pygame
from pygame.locals import *
class sumTree:
	class _Node:
		def __init__(self,element,left=None,right=None):
			self._element=element
			self._left=left
			self._right=right
		def getChildren(self,left,right):
			self._left=left
			self._right=right

	def __init__(self,element):
		self._root=self._Node(element)

	def __lt__(self,other):
		return self._element<other._element

	def sum(self):
		if self._left==None and self._right==None:
			return self._root._element
		else:
			return self._root._element+sum(self._left)+sum(self._right)

def createMinSumTree(L):
	heap=newHeapPriorityQueue()
	for i in L:
		heap.add(sumTree(i))
	while len(heap._data)>=2:
		left=heap.remove_min()
		right=heap.remove_min()
		newTree=sumTree(left._root._element+right._root._element)
		newTree._root.getChildren(left,right)
		heap.add(newTree)
	return heap.remove_min()

# L=[1,2,3,7]
# print(createMinSumTree(L)._root._element)
pygame.init()

SCREEN_HEIGHT=600
SCREEN_WIDTH=800
SCREEN_SIZE=(SCREEN_WIDTH,SCREEN_HEIGHT)
myfont=pygame.font.SysFont("times new roman", 20)

pygame.display.set_caption('Draw sumTree')
screen=pygame.display.set_mode(SCREEN_SIZE,pygame.RESIZABLE)
background=pygame.Surface(screen.get_size())
background=background.convert()
background.fill((255,255,255))

def main():
	global screen,SCREEN_HEIGHT,SCREEN_WIDTH,L
	L=[6, 7, 8, 9, 5, 4, 3, 2, 1]
	minSumTree=createMinSumTree(L)
	screen.fill((255,255,255))
	running=True
	while running:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
		drawMinSumTree(screen,minSumTree,200,50)
		pygame.display.flip()

def drawMinSumTree(screen,tree,x,y):
#this returns the position of where the root is drawn, which I need
#to draw lines to the roots of my subtrees
	inc=50
	if tree._root._left is not None:
		leftChildPos=drawMinSumTree(screen,tree._root._left,x,y+inc)
		x=x+inc*minSumTreeSubtreeSize(tree._root._left)
		pygame.draw.line(screen,(0,0,0),leftChildPos,(x,y))
	string=str(tree._root._element)
	text=myfont.render(string,True,(0,0,0))
	screen.blit(text,(x,y))
	retval=(x,y)
	x=x+inc
	if tree._root._right is not None:
		rightChildPos=drawMinSumTree(screen,tree._root._right,x,y+inc)
		pygame.draw.line(screen,(0,0,0),rightChildPos,retval)
	return retval

def minSumTreeSubtreeSize(tree):
	if tree._root._left is None and tree._root._right is None:
		return 1
	elif tree._root._left is None and tree._root._right is not None:
		return 1+minSumTreeSubtreeSize(tree._root._right)
	elif tree._root._left is not None and tree._root._right is None:
		return 1+minSumTreeSubtreeSize(tree._root._left)
	elif tree._root._left is not None and tree._root._right is not None:
		return 1+minSumTreeSubtreeSize(tree._root._left)+minSumTreeSubtreeSize(tree._root._left)
main()