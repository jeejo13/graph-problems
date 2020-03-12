graph ={ 
'a':['b'], 
'b':['d'], 
'c':['e'], 
'd':['a', 'e'], 
'e':['b', 'c'] 
} 

def find_shortest_path(graph, start, end, path =[]): 
		path.append(start) 
		if start == end: 
			return path 
		shortest = None
		for node in graph[start]: 
			if node not in path: 
				newpath = find_shortest_path(graph, node, end, path) 
				if newpath: 
					if not shortest or len(newpath) < len(shortest): 
						shortest = newpath 
		return shortest 

  
print(find_shortest_path(graph, 'd', 'c')) 
