class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        // We can use a stack because the most recent numbers are are always used next
        // When there is a number used, push it to the stack
        // When there is an operator, we pop the top two numbers, apply the operation, push the result
        stack<int> stack;
        // each element of tokens is a string so c represents that 
        // using string& passes c as a reference rather than a copy, without it it would copy c for each iteration
        // we use const because we don't want it to be modified directly, only want the result
        for (const string& c :tokens){
            if(c == "+"){
                int a = stack.top(); stack.pop();
                int b = stack.top(); stack.pop();
                stack.push(b + a);
            } else if (c == "-"){
                int a = stack.top(); stack.pop();
                int b = stack.top(); stack.pop();
                stack.push(b - a);
            } else if (c == "*"){
                int a = stack.top(); stack.pop();
                int b = stack.top(); stack.pop();
                stack.push(b * a);
            } else if (c == "/"){
                int a = stack.top(); stack.pop();
                int b = stack.top(); stack.pop();
                stack.push(b / a);
            } else {
                stack.push(stoi(c));
            }
        }
        return stack.top();
    }
};
