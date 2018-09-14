
from queue import Queue
def find_sum(n):
    upper = int(n**0.5)
    cond = [i**2 for i in range(1,upper+1)]
    q = Queue()
    q.put(n)
    step = 0
    visited=set()
    while not q.empty():
        step +=1
        for index in range(q.qsize()):
            node = q.get()
            if node in visited:
                continue
            visited.add(node)
            for j in cond:
                res =node - j
                if res == 0:
                    return step
                elif res<0:
                    continue
                else:
                    q.put(res)
                    

if __name__ == "__main__":
    print(find_sum(7168))


    