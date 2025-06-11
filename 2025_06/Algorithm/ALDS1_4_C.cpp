#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Node
{
    Node *a = NULL;
    Node *c = NULL;
    Node *g = NULL;
    Node *t = NULL;
    string key = "";
};
Node root = Node();
void insert(string key)
{
    Node *traceNode = &root;
    int i = 0;
    for (char c : key)
    {
        if (c == 'A')
        {
            if (traceNode->a == NULL)
            {
                traceNode->a = new Node();
                traceNode = traceNode->a;
            }
            else
            {
                traceNode = traceNode->a;
            }
        }
        else if (c == 'C')
        {
            if (traceNode->c == NULL)
            {
                traceNode->c = new Node();
                traceNode = traceNode->c;
            }
            else
            {
                traceNode = traceNode->c;
            }
        }
        else if (c == 'G')
        {
            if (traceNode->g == NULL)
            {
                traceNode->g = new Node();
                traceNode = traceNode->g;
            }
            else
            {
                traceNode = traceNode->g;
            }
        }
        else if (c == 'T')
        {
            if (traceNode->t == NULL)
            {
                traceNode->t = new Node();
                traceNode = traceNode->t;
            }
            else
            {
                traceNode = traceNode->t;
            }
        }
        i++;
        if (i == key.size())
        {
            traceNode->key = key;
        }
    }
}
void find(string key)
{
    Node *traceNode = &root;
    for (char c : key)
    {
        if (c == 'A')
        {
            if (traceNode->a == NULL)
            {
                cout << "no" << endl;
                return;
            }
            traceNode = traceNode->a;
        }
        else if (c == 'C')
        {
            if (traceNode->c == NULL)
            {
                cout << "no" << endl;
                return;
            }
            traceNode = traceNode->c;
        }
        else if (c == 'G')
        {
            if (traceNode->g == NULL)
            {
                cout << "no" << endl;
                return;
            }
            traceNode = traceNode->g;
        }
        else if (c == 'T')
        {
            if (traceNode->t == NULL)
            {
                cout << "no" << endl;
                return;
            }
            traceNode = traceNode->t;
        }
    }
    if (traceNode->key == key)
    {
        cout << "yes" << endl;
    }
    else
    {
        cout << "no" << endl;
    }
}
int main()
{
    int num = 0;
    cin >> num;
    string command = "";
    string key = "";
    for (int i = 0; i < num; i++)
    {
        cin >> command;
        if (command == "insert")
        {
            cin >> key;
            insert(key);
        }
        else if (command == "find")
        {
            cin >> key;
            find(key);
        }
    }
}
