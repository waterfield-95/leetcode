# 递归 recursion
1. 什么是递归？如何工作？
2. 如何使用递归解决问题？
3. 如何分析递归算法的时间和空间复杂度
4. 如何更好的使用递归

## 递归题解思路
1. 思考如何构建递归函数，输入，输出，边界条件
2. 思考递推关系，可拆解到basic case思考（括号中为边界条件）  
   - 分治思想 -1/折半(n==0/1/2)
   - 前后双指针 (l>=r)
   - 链表问题：有时（交换节点）需要先构建新指针 -> 递归 -> 每级数据处理

3. 当递归关系复杂时，由简至复思考关系

## 递归原理
>递归是一种解决问题的有效方法，在递归过程中，函数将自身作为子例程调用。  
递归调用自身的诀窍在于：它会将给定的问题拆解为子问题，持续调用直到子问题无需进一步递归就可以解决。

为了确保递归函数不会无限循环，它应具有以下属性：  
1. basic case 基本案例，能够不使用递归来产生答案的终止方案（递归前即解决问题，通常if语句用于出口，即边界条件-如果没有，会导致栈溢出，由于函数调用会占用栈空间保存函数头尾指针）
2. recurrence relation 递推关系，可将所有情况拆分到基本案例（分治思想-> 减1/除2）

### 示例
> 以相反的顺序打印字符串

[344. Reverse String](https://leetcode-cn.com/problems/reverse-string/)

可以使用遍历，也可使用递归方法。  

要求不占用额外空间，因此可以划分2部分：1). 前导字符和末尾字符。2). 其他字符串。  

算法：  (尾递归优化）
1. 就地交换 str[0] 和 str[n-1]
2. 递归调用来反转剩余字符串

```cpp
class Solution {
public:
    void recursion(vector<char>& s, int left, int right){
        if(left >= right) return;
        swap(s[left], s[right]);
        recursion(s, left+1, right-1);
    }

    void reverseString(vector<char>& s) {
        int size = s.size();
        helper(s, 0, size-1);
    }
};
```

## 递归函数

当存在递归解决方案时，可按照以下步骤实施：  
我们将问题定义为有待实现的函数 *F(x)*  
1. 将问题逐步分为较小的范围，例如 $x_0\in X, x_1\in X$
2. 调用函数F递归解决X这些子问题
3. 最后，处理调用递归函数得到结果来解决X的问题  

### 示例
[24. Swap Nodes in Pairs](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)  

定义函数 `swap(head)` 按照下面流程实现：  
1. 交换列表中的两个节点 `head` `head.next`
2. 递归调用 `swap(head.next.next)`
3. 最后，将步骤2中的子列表返回头与步骤1中交换的两个节点相连，形成新的链表

```cpp
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if(head == nullptr || head->next == nullptr) return head;
        ListNode* first_node = head;
        ListNode* second_node = head->next;

        first_node->next = swapPairs(head->next->next);
        second_node->next = first_node;

        return second_node;
    }
};
```

## 递推关系
在实现递归函数之前，有两件事需要弄清楚：  
- 递推关系：一个问题的结果与其子问题的结果之间的关系
- 基本情况：不需要进一步的递归调用就可以直接计算答案的情况。有时，基本案例也被称为 `bottom cases` 因为他们往往是问题被减少到最小规模的情况，也就是如果我们认为将问题划分为子问题是一种自上而下的方式的最下层。

> 一旦我们计算出以上两个元素，再想实现一个递归函数，仅需要根据*递推关系*调用函数本身，直到其抵达*基本情况*


