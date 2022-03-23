#include <bits/stdc++.h>
using namespace std;

struct Node
{
    int data;
    Node *left, *right;
};

Node *newNode(int data)
{
    Node *node = (Node *)malloc(sizeof(Node));
    node->data = data;
    node->left = node->right = NULL;
    return (node);
}

// Function to insert nodes in level order
Node *insertLevelOrder(int arr[], Node *root, int i, int n)
{
    // Base case for recursion
    if (i < n)
    {
        Node *temp = newNode(arr[i]);
        root = temp;

        // insert left child
        root->left = insertLevelOrder(arr, root->left, 2 * i + 1, n);

        // insert right child
        root->right = insertLevelOrder(arr, root->right, 2 * i + 2, n);
    }
    return root;
}

// Function to print tree nodes in
// InOrder fashion
void inOrder(Node *root)
{
    if (root != NULL)
    {
        inOrder(root->left);
        cout << char(root->data);
        inOrder(root->right);
    }
}

int main()
{
    int arr[65];
    for (int i = 0; i < 65; i++)
    {
        cin >> arr[i];
    }
    Node *root = insertLevelOrder(arr, root, 0, 65);
    inOrder(root);
}
