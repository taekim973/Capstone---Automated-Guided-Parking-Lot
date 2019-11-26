from GraphGen import Graph
from GraphGen import make_edge	

graph = Graph([
("0","1", 1),
("1","2", 1),
("2","3", 1),
("3","4", 3),
("4","5", 1),
("5","6", 1),
("6","7", 1),
("3","12", 2),
("12","13", 1),
("13", "4", 2),
("12","19", 15),
("0","23", 1.5),
("7", "23", 1.5),
("0","7", 3),
("2", "5", 3),
("1", "6", 3),
("3","5", 3.16),
("3","6", 3.61),
("3","7", 4.24),
("2","4", 3.16),
("2","6", 3.16),
("2","7", 3.61),
("1","7", 3.16),
("1","5", 3.16),
("1","4", 3.61),
("0","4", 4.24),
("0","5", 3.61),
("0","6", 3.16),
("7","11", 3),
("22","11", 1.5),
("8","9", 1),
("9","10", 1),
("10","11", 1),
("8","18", 2),
("18","19", 1),
("19", "14", 2),
("14","15", 1),
("15","16", 1),
("16","17", 1),
("17","22", 1.5),
("8", "14", 3),
("8", "15", 3.16),
("8", "16", 3.61),
("8", "17", 4.24),
("9", "14", 3.16),
("9", "15", 3),
("9", "16", 3.16),
("9", "17", 3.61),
("10", "14", 3.61),
("10", "15", 3.16),
("10", "16", 3),
("10", "17", 3.16),
("11", "14", 4.24),
("11", "15", 3.61),
("11", "16", 3.16),
("11", "17", 3),
("23","22", 4.75),
#
("1","0", 1),
("2","1", 1),
("3","2", 1),
("4","3", 3),
("5","4", 1),
("6","5", 1),
("7","6", 1),
("12","3", 2),
("13","12", 1),
("4", "13", 2),
("19","12", 15),
("23","0", 1.5),
("23", "7", 1.5),
("7","0", 3),
("5", "2", 3),
("6", "1", 3),
("5","3", 3.16),
("6","3", 3.61),
("7","3", 4.24),
("4","2", 3.16),
("6","2", 3.16),
("7","2", 3.61),
("7","1", 3.16),
("5","1", 3.16),
("4","1", 3.61),
("4","0", 4.24),
("5","0", 3.61),
("6","0", 3.16),
("11","7", 3),
("11","22", 1.5),
("9","8", 1),
("10","9", 1),
("11","10", 1),
("18","8", 2),
("19","18", 1),
("14", "19", 2),
("15","14", 1),
("16","15", 1),
("17","16", 1),
("22","17", 1.5),
("14", "8", 3),
("15", "8", 3.16),
("16", "8", 3.61),
("17", "8", 4.24),
("14", "9", 3.16),
("15", "9", 3),
("16", "9", 3.16),
("17", "9", 3.61),
("14", "10", 3.61),
("15", "10", 3.16),
("16", "10", 3),
("17", "10", 3.16),
("14", "11", 4.24),
("15", "11", 3.61),
("16", "11", 3.16),
("117", "11", 3),
("22","23", 4.75)
])

destination = input("Enter your destination: ")
print(graph.dijkstra("23", destination))