def check_is_looped(BR):
	graph = {}
	
	for k, it in groupby(sorted(BR), key=lambda x: x[0]):
	    graph[k] = {e for _, e in it}
	sub_graph = {}
	
	while True:
	    vertex_set = set(graph).intersection(chain.from_iterable(graph.values()))
	    sub_graph = {k: vertex_set & vs for k, vs in graph.items()
	                 if k in vertex_set and vertex_set & vs}
	    if sub_graph == graph:
	        break
	    else: 
	        graph = sub_graph
	
	# If find subgraph -> self looped
	if graph:
		return True	
	else:
		return False
