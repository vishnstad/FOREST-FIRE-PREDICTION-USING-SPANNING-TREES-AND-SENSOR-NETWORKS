from Module1_v2 import Graph
from minheap import minheap
from Module2 import Algorithms
from johnson import Johnson

g = Graph()
johnson = Johnson(g)
algorithms = Algorithms(g)
while True:
    print("---------------------------------------------------------------------------")
    print("1 : Create Graph \n2 : Modify Graph\n3 : Algorithms\n4 : view Graph\n5 : Quit")
    a = int(input("Enter you  choice : "))
    if a == 1:
        pass
        #g.create_graph()
    elif a == 2: 
        print("Choose:\n1 : Adjacency List\n2 : Adjacency Matrix")
        a = int(input("Enter your choice: "))
        if a == 1:
            print("Choose:\n1 : Add Sensor\n2 : Add connection\n3 : Remove connection\n4 : Remove sensor")
            b = int(input("Enter your choice: "))
            if b == 1:
                s = int(input("Enter Source sensor: "))
                d = int(input("Enter Destination sensor: "))
                w = int(input("Enter weight: "))
                g.ALaddvert(s,d,w)
                print("Sensor Succesfully Added")
            elif b == 2:
                s = int(input("Enter Source sensor: "))
                d = int(input("Enter Destination sensor: "))
                w = int(input("Enter weight: "))
                g.ALaddedge(s, d, w)#### need to take input from user and give prompt if task done
                print("Connection Succesfully Established")
                
            elif b == 3:
                s = int(input("Enter Source sensor: "))
                d = int(input("Enter Destination sensor: "))
                w = int(input("Enter weight: "))
                g.ALremoveedge(s, d, w)#### need to take input from user and give prompt if task done
                print("Connection Succesfully removed")
            elif b == 4:
                v = int(input("Enter Vertex: "))
                g.ALremovevert(v)
                print("Sensor succesfully removed")

        elif a == 2:
            print("Choose:\n1 : Addvertex\n2 : Addedge\n3 : Remove Edge\n4 : Remove vertex")
            b = int(input("Enter your choice: "))
            if b == 1:
                s = int(input("Enter Source sensor: "))
                d = int(input("Enter Destination sensor: "))
                w = int(input("Enter weight: "))
                g.addvert_AM(s,d,w)#### need to take input from user and give prompt if task done
                print("Sensor Succesfully Added")
            elif b == 2:
                s = int(input("Enter Source sensor: "))
                d = int(input("Enter Destination sensor: "))
                w = int(input("Enter weight: "))
                g.addedge_AM(s, d, w)#### need to take input from user and give prompt if task done
                print("Connection Succesfully Added")
                
            elif b == 3:
                s = int(input("Enter Source: "))
                d = int(input("Enter Destination: "))
                w = int(input("Enter weight: "))
                g.removedge_AM(s, d, )#### need to take input from user and give prompt if task done
                print("Connection Succesfully removde")
            elif b == 4:
                v = int(input("Enter Vertex: "))
                g.removevertex_AM(v)
                print("Sensor succesfully removed")
        else:
            print("Wrong Input")
    elif a == 3:
        #######################################----Adjacency List----##################################
        print("Choose:\n1 : Dijkstra\n2 : Bellman Ford\n3 : Floyd Warshall : \n4 : Johnson's")
        c = int(input("Enter your choice: "))
        if c == 1:
            source = int(input("Enter the source sensor: "))
            destination = int(input("Enter the destination sensor: "))

            # Run Dijkstra using adjacency list
            dijkstra_list = algorithms.Dijkstra(algorithms, source, use_adj_list=True)
            if dijkstra_list.find_shortest_paths():
                distance_list = dijkstra_list.get_shortest_distance(destination)
                path_list = dijkstra_list.get_path(destination)
                if distance_list != float('inf'):
                    print(f"Shortest distance (Adjacency List) from {source} to {destination} is: {distance_list}")
                    print(f"Path (Adjacency List): {' -> '.join(map(str, path_list))}")
                else:
                    print(f"There is no path from {source} to {destination} using Adjacency List.")

            dijkstra_matrix = algorithms.Dijkstra(algorithms, source, use_adj_list=False)
            if dijkstra_matrix.find_shortest_paths():
                distance_matrix = dijkstra_matrix.get_shortest_distance(destination)
                path_matrix = dijkstra_matrix.get_path(destination)
                if distance_matrix != float('inf'):
                    print(f"Shortest distance (Adjacency Matrix) from {source} to {destination} is: {distance_matrix}")
                    print(f"Path (Adjacency Matrix): {' -> '.join(map(str, path_matrix))}")
                else:
                    print(f"There is no path from {source} to {destination} using Adjacency Matrix.")
        elif c == 2:
            source = int(input("Enter the source sensor: "))
            destination = int(input("Enter the destination sensor: "))

            # Run Bellman-Ford using adjacency list
            bf_list = algorithms.BellmanFord(algorithms, source, use_adj_list=True)
            if bf_list.find_shortest_paths():
                distance_list = bf_list.get_shortest_distance(destination)
                path_list = bf_list.get_path(destination)
                if distance_list != float('inf'):
                    print(f"Shortest distance (Adjacency List) from {source} to {destination} is: {distance_list}")
                    print(f"Path (Adjacency List): {' -> '.join(map(str, path_list))}")
                else:
                    print(f"There is no path from {source} to {destination} using Adjacency List.")
            bf_matrix = algorithms.BellmanFord(algorithms, source, use_adj_list=False)
            if bf_matrix.find_shortest_paths():
                distance_matrix = bf_matrix.get_shortest_distance(destination)
                path_matrix = bf_matrix.get_path(destination)
                if distance_matrix != float('inf'):
                    print(f"Shortest distance (Adjacency Matrix) from {source} to {destination} is: {distance_matrix}")
                    print(f"Path (Adjacency Matrix): {' -> '.join(map(str, path_matrix))}")
                else:
                    print(f"There is no path from {source} to {destination} using Adjacency Matrix.")
        elif c == 3:
            source = int(input("Enter the source sensor: "))
            destination = int(input("Enter the destination sensor: "))

            # Run Floyd-Warshall using adjacency list
            fw_list = algorithms.FloydWarshall(algorithms, use_adj_list=True)
            fw_list.floyd_warshall()
            distance_list = fw_list.get_shortest_distance(source, destination)
            path_list = fw_list.get_path(source, destination)

            if distance_list != float('inf'):
                print(f"Shortest distance (Adjacency List) from {source} to {destination} is: {distance_list}")
                print(f"Path (Adjacency List): {' -> '.join(map(str, path_list))}")
            else:
                print(f"There is no path from {source} to {destination} using Adjacency List.")

            # Run Floyd-Warshall using adjacency matrix
            fw_matrix = algorithms.FloydWarshall(algorithms, use_adj_list=False)
            fw_matrix.floyd_warshall()
            distance_matrix = fw_matrix.get_shortest_distance(source, destination)
            path_matrix = fw_matrix.get_path(source, destination)

            if distance_matrix != float('inf'):
                print(f"Shortest distance (Adjacency Matrix) from {source} to {destination} is: {distance_matrix}")
                print(f"Path (Adjacency Matrix): {' -> '.join(map(str, path_matrix))}")
            else:
                print(f"There is no path from {source} to {destination} using Adjacency Matrix.")

        elif c == 4:
            source = int(input("Enter the source sensor: "))
            destination = int(input("Enter the destination sensor: "))
            all_pairs_shortest_paths = johnson.johnson_algorithm()
            if all_pairs_shortest_paths:
                distance_list = all_pairs_shortest_paths[source].get(destination, float('inf'))
                path_list = johnson.get_path_list(source, destination, use_adj_list=True)

                if distance_list != float('inf'):
                    print(f"Shortest distance (Adjacency List) from {source} to {destination} is: {distance_list}")
                    print(f"Path (Adjacency List): {' -> '.join(map(str, path_list))}")
                else:
                    print("There is no path.")

                # Re-run Johnson's algorithm if adjacency matrix is available
                distance_matrix = all_pairs_shortest_paths[source].get(destination, float('inf'))
                path_matrix = johnson.get_path_list(source, destination, use_adj_list=False)
                if distance_matrix != float('inf'):
                    print(f"Shortest distance (Adjacency Matrix) from {source} to {destination} is: {distance_matrix}")
                    print(f"Path (Adjacency Matrix): {' -> '.join(map(str, path_matrix))}")
                else:
                    print(f"There is no path from {source} to {destination} using Adjacency Matrix.")

    elif a ==4:
        print("Adjacency List")
        g.printG_AL()
        print("Adjacency Matirx")
        g.print_AM()
    elif a == 5:
        break
    else:
        print("Wrong Input")
    #######################################----Adjacency Matrix----##################################

