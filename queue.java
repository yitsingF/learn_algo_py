import java.util.ArrayList;

class MyCircularQueue {
    
    private List<Integer> data; 
    private Integer start_p;
    private Integer end_p;
    private Integer size;
    /** Initialize your data structure here. Set the size of the queue to be k. */
    public MyCircularQueue(int k) {
        data = new ArrayList<Integer>(k);
        start_p=null;
        end_p=null;
        size=k;
        
    }
    
    /** Insert an element into the circular queue. Return true if the operation is successful. */
    public boolean enQueue(int value) {
        if(start_p == null) {
            // empty list
            data[0] = value;
            start_p=0;
            end_p=0;
            return true;
        }
        

        
    }
    
    /** Delete an element from the circular queue. Return true if the operation is successful. */
    public boolean deQueue() {


        if (isEmpty()){
            start_p=null;
            end_p=null;
        }
        return true;
        
    }
    
    /** Get the front item from the queue. */
    public int Front() {
        if (isEmpty()) {
            return -1;
        }
        int ans;
        ans = data[start_p];
        data[start_p]=null; 
        if (start_p < end_p) {
            start_p++;
        }
        else if (start_p == end_p) {
            start_p=null;
            end_p=null;
        }else{
            if (start_p == size-1) {
                start_p=0;
            }else{
                start_p ++;
            }
        }

        return ans;
        
    }
    
    /** Get the last item from the queue. */
    public int Rear() {
        
    }
    
    /** Checks whether the circular queue is empty or not. */
    public boolean isEmpty() {
        
    }
    
    /** Checks whether the circular queue is full or not. */
    public boolean isFull() {
        if (start_p > end_p) {
            return end_p+1 == start_p;
        }
        return 
        
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */


 /**
 * Return the length of the shortest path between root and target node.
 */

/