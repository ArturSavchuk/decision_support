from itertools import chain, groupby
import copy


R1 = [
 [0,  1,  0,  0,  1,  0,  0,  0,  1,  0,  1,  1,  1,  1,  0], 
 [0,  0,  0,  1,  0,  0,  0,  0,  1,  1,  0,  1,  1,  0,  0], 
 [1,  0,  0,  0,  1,  1,  1,  1,  1,  1,  1,  0,  1,  0,  1], 
 [0,  0,  0,  0,  1,  1,  1,  0,  0,  0,  1,  1,  0,  1,  1], 
 [0,  0,  0,  0,  0,  1,  1,  0,  0,  1,  1,  0,  1,  0,  0], 
 [0,  0,  0,  0,  0,  0,  0,  1,  1,  0,  0,  0,  0,  1,  0], 
 [0,  0,  0,  0,  0,  1,  0,  1,  1,  0,  0,  1,  1,  0,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  0,  0,  0,  1,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  1,  1], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0], 
 [0,  0,  0,  0,  0,  0,  0,  1,  0,  1,  0,  0,  1,  0,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  0,  1,  0,  1], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
]

R2 = [
 [0,  1,  1,  1,  1,  0,  1,  1,  1,  1,  0,  1,  1,  1,  0], 
 [0,  0,  1,  1,  0,  0,  1,  1,  0,  1,  1,  0,  0,  1,  1], 
 [0,  0,  0,  0,  1,  1,  1,  0,  0,  1,  0,  0,  1,  1,  1], 
 [0,  0,  1,  0,  1,  1,  0,  0,  1,  0,  1,  1,  0,  1,  1], 
 [0,  0,  0,  0,  0,  1,  1,  0,  0,  0,  1,  0,  0,  0,  0], 
 [0,  0,  0,  0,  0,  0,  1,  1,  0,  1,  0,  1,  0,  0,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  0,  1,  1,  1], 
 [0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  0,  0,  0,  1], 
 [0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  1,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  0,  1,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0], 
]

R3 = [
 [0,  0,  1,  0,  0,  1,  0,  0,  0,  1,  1,  1,  0,  1,  1], 
 [0,  0,  1,  1,  1,  1,  0,  1,  1,  0,  1,  0,  1,  0,  0], 
 [0,  0,  0,  0,  1,  1,  0,  1,  0,  1,  0,  0,  1,  1,  1], 
 [0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  1,  0,  0,  1], 
 [0,  0,  0,  0,  0,  1,  0,  0,  1,  0,  1,  1,  0,  1,  1], 
 [0,  0,  0,  0,  0,  0,  1,  1,  0,  1,  1,  1,  0,  1,  1], 
 [0,  0,  0,  0,  0,  0,  0,  1,  1,  0,  1,  0,  0,  1,  1], 
 [0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  1,  0,  1], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  1,  0,  1,  1], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1], 
 [0,  0,  0,  1,  0,  0,  0,  1,  1,  1,  0,  0,  1,  0,  1], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  1,  1], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
]


R4 = [
 [0,  1,  1,  1,  0,  1,  1,  1,  1,  0,  1,  1,  0,  1,  0], 
 [0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
 [0,  0,  0,  0,  0,  0,  1,  1,  1,  0,  0,  1,  0,  1,  0], 
 [0,  0,  0,  0,  0,  0,  1,  1,  1,  0,  0,  1,  0,  1,  0], 
 [0,  0,  0,  0,  0,  0,  1,  1,  1,  0,  0,  1,  0,  1,  0], 
 [0,  1,  1,  1,  0,  1,  1,  1,  1,  0,  1,  1,  0,  1,  0], 
 [0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
 [0,  0,  0,  0,  0,  0,  1,  1,  1,  0,  0,  1,  0,  1,  0], 
 [0,  1,  1,  1,  0,  1,  1,  1,  1,  0,  1,  1,  0,  1,  0], 
 [0,  0,  0,  0,  0,  0,  1,  1,  1,  0,  0,  1,  0,  1,  0], 
 [0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
]


R5 = [
 [0,  1,  1,  1,  1,  0,  0,  0,  0,  0,  1,  0,  0,  1,  1], 
 [0,  0,  1,  1,  1,  0,  1,  1,  0,  0,  0,  1,  1,  0,  0], 
 [0,  0,  0,  1,  0,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1], 
 [0,  0,  0,  0,  0,  0,  1,  1,  0,  0,  0,  1,  1,  0,  0], 
 [0,  0,  1,  0,  0,  1,  1,  1,  1,  1,  0,  1,  1,  0,  0], 
 [0,  0,  0,  1,  0,  0,  0,  1,  0,  1,  1,  1,  1,  1,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  0,  0,  1,  1], 
 [0,  0,  0,  0,  0,  0,  1,  0,  0,  1,  1,  1,  1,  1,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  1,  1], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  1,  1,  1], 
 [0,  0,  0,  0,  0,  0,  1,  0,  0,  1,  1,  0,  1,  1,  1], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  1,  1], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  1,  0], 
]


R6 = [
 [1,  0,  1,  0,  0,  1,  0,  1,  1,  0,  0,  0,  0,  0,  0], 
 [0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
 [1,  0,  1,  0,  0,  1,  0,  1,  1,  0,  0,  0,  0,  0,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
 [0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
 [1,  0,  1,  0,  0,  1,  0,  1,  1,  0,  0,  0,  0,  0,  0], 
 [0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
 [1,  0,  1,  0,  0,  1,  0,  1,  1,  0,  0,  0,  0,  0,  0], 
 [1,  0,  1,  0,  0,  1,  0,  1,  1,  0,  0,  0,  0,  0,  0], 
 [1,  0,  1,  1,  0,  1,  1,  1,  1,  0,  1,  1,  1,  0,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0], 
 [1,  0,  1,  1,  0,  1,  1,  1,  1,  0,  1,  1,  1,  0,  0], 
 [1,  0,  1,  1,  0,  1,  1,  1,  1,  0,  1,  1,  1,  0,  0], 
]


R7 = [
 [0,  1,  0,  1,  0,  0,  0,  1,  1,  0,  1,  0,  0,  0,  0], 
 [0,  0,  1,  1,  1,  1,  1,  0,  1,  1,  1,  1,  1,  0,  0], 
 [1,  0,  0,  0,  0,  0,  1,  1,  0,  1,  1,  1,  0,  0,  1], 
 [0,  0,  1,  0,  1,  1,  1,  1,  1,  1,  0,  0,  0,  1,  1], 
 [1,  0,  1,  0,  0,  1,  1,  1,  1,  0,  1,  1,  0,  0,  1], 
 [1,  0,  1,  0,  0,  0,  1,  1,  1,  1,  0,  0,  0,  1,  1], 
 [1,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,  1,  1,  0], 
 [0,  1,  0,  0,  0,  0,  1,  0,  0,  0,  0,  1,  0,  1,  1], 
 [0,  0,  1,  0,  0,  0,  0,  1,  0,  1,  0,  1,  1,  1,  0], 
 [1,  0,  0,  0,  1,  0,  0,  1,  0,  0,  0,  1,  0,  0,  1], 
 [0,  0,  0,  1,  0,  1,  0,  1,  1,  1,  0,  0,  0,  0,  1], 
 [1,  0,  0,  1,  0,  1,  0,  0,  0,  0,  1,  0,  0,  1,  1], 
 [1,  0,  1,  1,  1,  1,  0,  1,  0,  1,  1,  1,  0,  0,  0], 
 [1,  1,  1,  0,  1,  0,  0,  0,  0,  1,  1,  0,  1,  0,  0], 
 [1,  1,  0,  0,  0,  0,  1,  0,  1,  0,  0,  0,  1,  1,  0], 
 ]

R8 = [
 [0,  1,  0,  0,  1,  0,  0,  0,  1,  0,  0,  1,  0,  0,  1], 
 [0,  0,  0,  1,  1,  0,  0,  1,  0,  0,  0,  1,  0,  1,  1], 
 [1,  1,  0,  0,  0,  1,  0,  0,  0,  0,  1,  1,  0,  1,  0], 
 [0,  0,  0,  0,  1,  0,  1,  1,  1,  0,  0,  1,  0,  0,  1], 
 [0,  0,  0,  0,  0,  1,  1,  1,  0,  1,  1,  0,  0,  0,  0], 
 [0,  0,  0,  0,  0,  0,  0,  1,  1,  0,  1,  0,  0,  1,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1], 
 [0,  0,  0,  0,  0,  0,  1,  0,  0,  1,  1,  0,  1,  0,  1], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  1,  1], 
 [0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0], 
 [0,  0,  0,  0,  0,  0,  1,  0,  0,  1,  0,  0,  1,  1,  1], 
 [0,  0,  0,  0,  1,  1,  0,  0,  0,  1,  1,  0,  1,  0,  0], 
 [0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  1,  1], 
 [0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
]


R9 = [
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
 [1,  0,  0,  1,  0,  1,  1,  0,  0,  1,  1,  0,  1,  1,  1], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
 [1,  0,  0,  1,  0,  1,  1,  0,  0,  1,  1,  0,  1,  1,  1], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
 [1,  0,  0,  1,  0,  1,  1,  0,  0,  1,  1,  0,  1,  1,  1], 
 [1,  0,  0,  1,  0,  1,  1,  0,  0,  1,  1,  0,  1,  1,  1], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
 [1,  0,  0,  1,  0,  1,  1,  0,  0,  1,  1,  0,  1,  1,  1], 
]

R10 = [
 [0,  0,  1,  0,  0,  0,  1,  1,  0,  1,  1,  0,  0,  1,  1], 
 [0,  0,  0,  0,  1,  0,  1,  0,  0,  0,  1,  1,  0,  1,  1], 
 [0,  1,  0,  1,  1,  0,  1,  0,  1,  1,  0,  0,  1,  1,  0], 
 [0,  1,  0,  0,  1,  0,  1,  0,  1,  1,  0,  1,  0,  1,  0], 
 [0,  0,  0,  0,  0,  0,  1,  0,  1,  0,  1,  0,  1,  0,  1], 
 [0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  1,  1,  1,  0,  1], 
 [0,  0,  0,  0,  0,  0,  0,  1,  1,  0,  0,  0,  1,  1,  1], 
 [0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  1,  1,  0,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  0,  0,  0,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  1,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  1], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  1,  0], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1], 
 [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], 
]

relations = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10]

def to_graph(rel):
	graph = []
	for i in range(0, len(rel)):
		for j in range(0, len(rel)):
			if rel[i][j] == 1:
				graph.append((i + 1, j + 1))
	return graph



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


def is_looped(relation):
	return check_is_looped(to_graph(relation))



#find the biggest elements in relation

def get_blockers_by_R_strict(relation):
    blockers = []
    for j in range(0, len(relation)):
        is_blocker = True
        for i in range(0, len(relation)):
            if relation[i][j] != 0 and j != i:
                is_blocker = False
                break
        if is_blocker:
            blockers.append(j)

    return blockers

#getting next set of alternatives for relation and previous set of alternatives

def getSnext(relation, blockers):
	s1 = []
	for j in range(0, len(relation)):
		valid = True
		for i in range(0, len(relation)):
			if relation[i][j] == 1 and i not in blockers:
				valid = False
				break
			if j in blockers:
				valid = False
				break
		if valid:
			s1.append(j) 

	return s1


def add_to_arr(arr1, arr2):
	for i in range(0, len(arr2)):
		arr1.append(arr2[i])


#get sequence of sets of alternatives while last set != relation 

def get_s_seq(relation):
	omega = get_blockers_by_R_strict(relation)
	a = get_blockers_by_R_strict(relation)
	om = []
	om.append(a)
	t = []
	while len(omega) != len(relation):
			t = getSnext(relation, omega)
			add_to_arr(omega, t)
			om.append(t)

	return om

#get sequence of probably solutions and check internal and external stability

def get_q_seq(relation, s_seq):
	q_set = s_seq[0]
	for i in range(1, len(s_seq)):
		for j in range(0, len(s_seq[i])):
			valid = True;
			for k in range(0, len(relation)):
				if relation[k][s_seq[i][j]] == 1 and k in q_set:
					valid = False
					break
			if valid:
				q_set.append(s_seq[i][j])

	return q_set



def to_gen_view(sequence):
	for i in range(0, len(sequence)):
		for j in range(0, len(sequence[i])):
			sequence[i][j] = sequence[i][j] + 1

	return sequence


#implementation of Neuman-Morgenstern optimization

def NM_optimization(relation):
	s_seq = get_s_seq(relation)
	t_list = copy.deepcopy(s_seq)
	to_gen_view(t_list)
	q_seq = get_q_seq(relation, s_seq)

	print("S0 " + str(t_list[0]))
	to_gen_view(s_seq)

	for i in range(1, len(s_seq)):
		k = i - 1
		print("S" + str(i) + " without S" + str(k) + " " + str(s_seq[i]))
	print("Set S" + str(len(s_seq) - 1) + " = omega" + " = " + str(t_list))
	print ("Solution of the Neumann-Morgenstern optimization: " + str(q_seq))
	


#get matrix for symmetrical, asymmetric, incomparable part of the relation

def get_PNImatrix(relation):
	
	pni = copy.deepcopy(relation)

	for i in range(0, len(relation)):
		for j in range(0, len(relation)):
			if relation[i][j] == 0 and relation[j][i] == 1:
				pni[j][i] = 'P'
			if relation[i][j] and relation[j][i]:
				pni[j][i] = 'I'
			if relation[i][j] == 0 and relation[j][i] == 0:
				pni[j][i] = 'N'
			
	return pni

#majority check the candidates 

def get_opt_max_alternatives(candidates, s):
	_max = []
	_opt = []
	for c in candidates:
		for i in range(len(s)):
			valid = True
			if s[c][i] == 0:
				for j in range(len(s)):
					if s[j][i] == 1 and j != c:
						valid = False
						break	
		if valid:
			_max.append(c + 1)
			if count_1_for_row(s[c]) == len(s):
				_opt.append(c + 1)

	return _max, _opt


def count_1_for_row(r):
	count = 0
	for i in r:
		if i == 1:
			count += 1

	return count

#take the row with the largest number of 1

def get_max1_str(s):
	quantities = []
	counter = 0
	for i in range (len(s)):
		for j in range (len(s)):
			if s[i][j] == 1:
				counter += 1
		quantities.append(counter) 
		counter = 0
	

	max_value = max(quantities)
	max_value_indices = [i for i, e in enumerate(quantities) if e == max_value]
	return max_value_indices

#optimization by symmetrical, asymmetric, incomparable parts

def k1_optimize(PNImatrix):
	s1 = copy.deepcopy(PNImatrix)
	max1 = []
	opt1 = []
	for i in range(len(PNImatrix)):
		for j in range(len(PNImatrix)):
			if PNImatrix[i][j] != 0:
				s1[i][j] = 1

	print("****S1****")
	show(s1)
	candidates = get_max1_str(s1)
	return get_opt_max_alternatives(candidates, s1)

#optimization by asymmetric, incomparable parts

def k2_optimize(PNImatrix):
	s2 = copy.deepcopy(PNImatrix)

	for i in range(len(PNImatrix)):
		for j in range(len(PNImatrix)):
			if PNImatrix[i][j] == 'N' or PNImatrix[i][j] == 'P':
				s2[i][j] = 1
			if PNImatrix[i][j] == 'I':
				s2[i][j] = 0

	print("****S2****")
	show(s2)
	candidates = get_max1_str(s2)
	return get_opt_max_alternatives(candidates, s2)


#optimization by symmetrical, asymmetric parts

def k3_optimize(PNImatrix):
	s3 = copy.deepcopy(PNImatrix)
	for i in range(len(PNImatrix)):
		for j in range(len(PNImatrix)):
			if PNImatrix[i][j] == 'I' or PNImatrix[i][j] == 'P':
				s3[i][j] = 1
			if PNImatrix[i][j] == 'N':
				s3[i][j] = 0

	print("****S3****")
	show(s3)
	candidates = get_max1_str(s3)
	return get_opt_max_alternatives(candidates, s3)
	

#optimization by symmetrical, asymmetric, incomparable parts

def k4_optimize(PNImatrix):
	s4 = copy.deepcopy(PNImatrix)
	for i in range(len(PNImatrix)):
		for j in range(len(PNImatrix)):
			if PNImatrix[i][j] == 'P':
				s4[i][j] = 1
			if PNImatrix[i][j] == 'N' or PNImatrix[i][j] == 'I' :
				s4[i][j] = 0
	
	print("****S4****")	
	show(s4)		
	candidates = get_max1_str(s4)
	return get_opt_max_alternatives(candidates, s4)

#implementation of k-optimization

def k_optimization(relation):
	PNImatrix = get_PNImatrix(relation)
	print("PNImatrix")
	show(PNImatrix)

	k1_result = k1_optimize(PNImatrix)
	print ("1-max alternatives: " + str(k1_result[0]) + "  | 1-opt alternatives: " + str(k1_result[1]))
	
	k2_result = k2_optimize(PNImatrix)
	print ("2-max alternatives: " + str(k2_result[0]) + "  | 2-opt alternatives: " + str(k2_result[1]))

	k3_result = k3_optimize(PNImatrix)
	print ("3-max alternatives: " + str(k3_result[0]) + "  | 3-opt alternatives: " + str(k3_result[1]))
	
	k4_result = k4_optimize(PNImatrix)
	print ("4-max alternatives: " + str(k4_result[0]) + "  | 4-opt alternatives: " + str(k4_result[1]) )
	

def show(matrix):
	for r in matrix	:
    		for c in r:
        		print(c,end = " ")
    		print()


#general optimization function 

def optimize(relations):
	for i in range(0, len(relations)):
		print("Relation " + str(i + 1))
		if is_looped(relations[i]):
			print ("K optimization")
			k_optimization(relations[i])
		else:
			print ("Neumann-Morgenstern optimization")
			NM_optimization(relations[i])

optimize(relations)

