#include <iostream>
#include <math.h>
using namespace std;

// INSERTION IN BST
// 26.7.22

struct Node
{
    int data;
    Node *right;
    Node *left;
};

Node *create(int data)
{
    Node *n = new Node;
    n->data = data;
    n->left = NULL;
    n->right = NULL;

    return n;
}

void linked(Node *root, Node *l, Node *r)
{
    root->left = l;
    root->right = r;
}

void inOrder(Node *root)
{
    if (root != NULL)
    {
        inOrder(root->left);
        cout << " " << root->data;
        inOrder(root->right);
    }
}

// ----------------------------------------------------------
void insertion(Node *root, int key)
{
    Node *prev, *start;
    start = root;
    while (root != NULL)
    {
        prev = root;
        if (root->data == key)
        {
            cout << "insertion is not possible , element already exist " << endl;
            return;
        }

        else if (key > root->data)
        {
            root = root->right;
        }
        else
        {
            root = root->left;
        }
    }
    Node *newNode = new Node; // this is new node for insertion
    newNode = create(key);    // calling the create() function which will create new node
    if (key > prev->data)
    {
        prev->right = newNode;
    }
    else
    {
        prev->left = newNode;
    }

    cout << "inOrder traversing of BST after insertion" << endl;
    inOrder(start);
}
// ___________this is insertion funciton ________________^^^^^^^^^^^______________________


int main()
{
    int n, rows, limit, i, key;
    cout << "enter the number of rows you wants to create in your binary treee :" << endl;
    cin >> rows;

    n = pow(2, rows) - 1;

    Node *nodes[n];
    int data[n];

    cout << " enter " << n << "  data elements for your binary tree: " << endl;
    for (i = 0; i < n; i++)
    {
        cin >> data[i];
    }

    for (i = 0; i < n; i++)
    {
        nodes[i] = create(data[i]);
    }

    limit = n / 2;

    for (i = 0; i < limit; i++)
    {
        linked(nodes[i], nodes[(i * 2) + 1], nodes[(i * 2) + 2]); // ----> most imporatant statement
    }

    cout << " inOrder traversing of the binary tree is : " << endl;
    inOrder(nodes[0]);
loop:
    cout << "\n\n enter the new element for insertion : " << endl;
    cin >> key;
    insertion(nodes[0], key);

    goto loop;
    
}
