from collections import defaultdict 
 
class Graph: 
    def __init__(self,vertices): 
        self.V= vertices 
        self.graph = [] 
                               
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 
         
    def find(self, parente, i): 
        if parente[i] == i: 
            return i 
        return self.find(parente, parente[i]) 
         
    def uniao(self, parente, link, x, y): 
        v = self.find(parente, x) 
        z = self.find(parente, y) 
        if link[v] < link[z]: 
            parente[v] = z 
        elif link[v] > link[z]: 
            parente[z] = v 
        else : 
            parente[z] = v 
            link[v] += 1
        
    def Kruskal(self): 
        resultado =[] 
        i = 0 
        e = 0 
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
        parente = [] ; link = [] 
        for no in range(self.V): 
            parente.append(no) 
            link.append(0) 
        while e < self.V -1 : 
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parente, u) 
            y = self.find(parente ,v) 
            if x != y: 
                e = e + 1     
                resultado.append([u,v,w]) 
                self.uniao(parente, link, x, y)             
        soma=0
        for u,v,z  in resultado: 
            soma+= z
        return soma
l=[]
while True:
	try:
		n= int(input())
	except:
		break
	g = Graph(n+1) 
	soma=0
	a=0
	b=1
	c=0
	g.addEdge(a, b, c) 
	for i in range(n-1):
		a,b,c=input().split(" ")
		a=int(a)
		b=int(b)
		c=int(c)
		g.addEdge(a, b, c) 
		soma+=c
	while True: 
		try:
			k= int(input())
		except:
			break
		for i in range(k):
			a,b,c=input().split(" ")
			a=int(a)
			b=int(b)
			c=int(c)
			g.addEdge(a, b, c)
	l.append(soma)
	l.append(g.Kruskal())
i=0
while i < len(l):
	print(l[i])
	print(l[i+1])
	i=i+2
	print('')
