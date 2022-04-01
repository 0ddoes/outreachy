>>> import networkx as nx
>>> import numpy as np
>>> 
>>> 
>>> 
>>> G = nx.Graph()
>>> edges = [(0,1),(2,2), ("love", "hate"), (1,"love")]
>>> G.add_edges_from(edges)
>>> nx.to_numpy_array(G, nodelist=[1, "love"])
array([[0., 1.],
       [1., 0.]])
>>> 
>>> 
>>> attrs = {edges[0]: {"weight": 20}, edges[1]: {"weight": 3}}
>>> nx.set_edge_attributes(G, attrs)
>>> A = nx.to_numpy_array(G, dtype= int, weight = "weight", nonedge = 99)
>>> A
array([[99, 20, 99, 99, 99],
       [20, 99, 99,  1, 99],
       [99, 99,  3, 99, 99],
       [99,  1, 99, 99,  1],
       [99, 99, 99,  1, 99]])
>>> 
>>> 
>>> 
>>> A = nx.to_numpy_array(G, dtype= int, weight = "weight", nonedge = float("nan"))
>>> A
array([[-9223372036854775808,                   20, -9223372036854775808,
        -9223372036854775808, -9223372036854775808],
       [                  20, -9223372036854775808, -9223372036854775808,
                           1, -9223372036854775808],
       [-9223372036854775808, -9223372036854775808,                    3,
        -9223372036854775808, -9223372036854775808],
       [-9223372036854775808,                    1, -9223372036854775808,
        -9223372036854775808,                    1],
       [-9223372036854775808, -9223372036854775808, -9223372036854775808,
                           1, -9223372036854775808]])
>>> 
>>> 
>>> 
>>> 
>>> attrs = {edges[2]: {"cost": 20, "money" : 5000}, edges[3]: {"cost": 3}}
>>> nx.set_edge_attributes(G, attrs)
>>> A = nx.to_numpy_array(G, dtype= int, weight = "cost")
>>> A
array([[ 0,  1,  0,  0,  0],
       [ 1,  0,  0,  3,  0],
       [ 0,  0,  1,  0,  0],
       [ 0,  3,  0,  0, 20],
       [ 0,  0,  0, 20,  0]])
>>> A = nx.to_numpy_array(G, dtype= int, weight = "money")
>>> A
array([[   0,    1,    0,    0,    0],
       [   1,    0,    0,    1,    0],
       [   0,    0,    1,    0,    0],
       [   0,    1,    0,    0, 5000],
       [   0,    0,    0, 5000,    0]])
>>> 
>>> 
>>> 
>>> 
>>> 
>>> G = nx.MultiDiGraph()
>>> edges = [(0,1), (0,1), (1,0), (2,2), ("love", "hate"), (1,"love")]
>>> G.add_edges_from(edges)
[0, 1, 0, 0, 0, 0]
>>> nx.to_numpy_array(G, nodelist=[0, 1, 2])
array([[0., 2., 0.],
       [1., 0., 0.],
       [0., 0., 1.]])
>>> 
>>> 
>>> 
>>> attributes = {(0,1,0): {"weight": 20, "cost": 5}, (2,2,4): {"weight": 10, "cost": 3}, (0,1,1): {"cost":5}}
>>> nx.set_edge_attributes(G, attributes)
>>> 
>>> dtype = np.dtype([("weight", float), ("cost", int)])
>>> A = nx.to_numpy_array(G, nodelist=[0, 1, 2], dtype=dtype, weight=None, multigraph_weight = sum)
>>> A["cost"]
array([[0, 2, 0],
       [1, 0, 0],
       [0, 0, 1]])
>>> 
>>> 
>>> A = nx.to_numpy_array(G, dtype=dtype, weight="cost", multigraph_weight = sum)
>>> A["cost"]
array([[ 0, 10,  0,  0,  0],
       [ 1,  0,  0,  1,  0],
       [ 0,  0,  1,  0,  0],
       [ 0,  0,  0,  0,  1],
       [ 0,  0,  0,  0,  0]])
>>> 
>>> 
>>> 
>>> 
>>> 
>>> A["weight"]
array([[ 0., 10.,  0.,  0.,  0.],
       [ 1.,  0.,  0.,  1.,  0.],
       [ 0.,  0.,  1.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  1.],
       [ 0.,  0.,  0.,  0.,  0.]])
>>> 
>>> 
>>> 
>>> A
array([[( 0.,  0), (10., 10), ( 0.,  0), ( 0.,  0), ( 0.,  0)],
       [( 1.,  1), ( 0.,  0), ( 0.,  0), ( 1.,  1), ( 0.,  0)],
       [( 0.,  0), ( 0.,  0), ( 1.,  1), ( 0.,  0), ( 0.,  0)],
       [( 0.,  0), ( 0.,  0), ( 0.,  0), ( 0.,  0), ( 1.,  1)],
       [( 0.,  0), ( 0.,  0), ( 0.,  0), ( 0.,  0), ( 0.,  0)]],
      dtype=[('weight', '<f8'), ('cost', '<i8')])
>>> 
>>> 
>>> 
>>> A = nx.to_numpy_array(G, dtype=dtype, weight= ("weight","cost"), multigraph_weight = sum)
>>> A
array([[(0., 0), (2., 2), (0., 0), (0., 0), (0., 0)],
       [(1., 1), (0., 0), (0., 0), (1., 1), (0., 0)],
       [(0., 0), (0., 0), (1., 1), (0., 0), (0., 0)],
       [(0., 0), (0., 0), (0., 0), (0., 0), (1., 1)],
       [(0., 0), (0., 0), (0., 0), (0., 0), (0., 0)]],
      dtype=[('weight', '<f8'), ('cost', '<i8')])
>>> 
KeyboardInterrupt
>>> 
