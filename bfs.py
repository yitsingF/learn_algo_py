from queue import Queue
def sort_matrix(mat):
    row, col = len(mat), len(mat[0])
    q=Queue(row*col)

    # enqueue the start point
    for i in range(row):
        for j in range(col):
            if mat[i][j] == 0:
                q.put((i,j))
                visited=set()
                visited.add((i,j))
                bfs_mat(mat,visited,q)
    return mat

INF_INT = 2**31 -1

def bfs_mat(mat,visited,q):
    step = 0
    row, col = len(mat), len(mat[0])
    while not q.empty():
        step += 1
        for cnt in range(q.qsize()):
            node = q.get()
            if node == (0,1):
                print(q)
            adjanced_nodes = adjanct_block(node[0],node[1],row,col)
            for ad_node in adjanced_nodes:

                if ad_node in visited:
                    continue
                # make the node visited whatere it is 
                visited.add(ad_node)
                val = mat[ad_node[0]][ad_node[1]]
                if val in {0,-1}:
                    # it is a blocker
                    continue
                else:
                    # it is not a  blocker
                    mat[ad_node[0]][ad_node[1]] = min(val,step)
                    q.put(ad_node)



def adjanct_block(i, j, m, n):
    # generate block candate
    it_1 = [x for x in [i - 1, i + 1] if x > 0 and x < m]
    it_2 = [x for x in [j - 1, j + 1] if x > 0 and x < n]
    adjance = [(x, j) for x in it_1]
    adjance += [(i, x) for x in it_2]
    return adjance

if __name__ == "__main__":
    a=[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
    print(sort_matrix(a))