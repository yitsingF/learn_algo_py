import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class MinStack {

    private List<Integer> data;
    private int minIndex;

    public MinStack() {
        data = new ArrayList<>();
    }

    public void push(int x) {
        data.add(x);
        if (data.size() == 1) {
            minIndex = 0;
            return;
        }
        if (x < data.get(minIndex)) {
            minIndex = data.size() - 1;
        }
    }

    public void pop() {
        data.remove(data.size() - 1);
    }

    public int top() {
        return data.get(data.size() - 1);
    }

    public int getMin() {
        return data.get(minIndex);

    }
}


/**
 * Your MinStack object will be instantiated and called as such: MinStack obj =
 * new MinStack(); obj.push(x); obj.pop(); int param_3 = obj.top(); int param_4
 * = obj.getMin();
 */