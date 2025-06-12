#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;

struct Node
{
    int data = NULL;
    Node *left = &Node(NULL, false);
    Node *right = &Node(NULL, false);
    Node *parent = NULL;
    bool isLeaf;
    bool color; // true:red, false:black
    Node(int data = 0, bool color = true)
    {
        this->data = data;
        this->color = color;
        this->isLeaf = color;
    }
};

class Red_Black_Tree
{
public:
    Node root;
    Node leaf(0, false);
    leaf.left = NULL;
    leaf.right = NULL;
    Red_Black_Tree(int data)
    {
        this->root = Node(data, false);
    }
    void insert(int data)
    {
        Node *trace = &this->root;
        while (trace->isLeaf == false)
        {
            if (data < trace->data)
            {
                trace = trace->left;
            }
            else if (data > trace->data)
            {
                trace = trace->right;
            }
            else
            {
                cout << "Data already exists" << endl;
                return;
            }
        }
        Node temp;
        temp =
            trace->data = data;
        trace->isLeaf = false;
        trace->color = true;
    }
};

int main()
{

    int a = 0;
}
