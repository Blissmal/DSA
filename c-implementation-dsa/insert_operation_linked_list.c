#include <stdio.h>
#include <stdlib.h>

// Define the structure for a single node
typedef struct Node {
    int data;
    struct Node* next_node;
} Node;

// Function to create a new node
Node* create_node(int data) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->data = data;
    new_node->next_node = NULL;
    return new_node;
}

// Define the structure for the linked list
typedef struct LinkedList {
    Node* head;
} LinkedList;

// Function to create a new linked list
LinkedList* create_linked_list() {
    LinkedList* list = (LinkedList*)malloc(sizeof(LinkedList));
    list->head = NULL;
    return list;
}

// Function to check if the linked list is empty
int is_empty(LinkedList* list) {
    return list->head == NULL;
}

// Function to add a new node containing data at the head of the list
void add(LinkedList* list, int data) {
    Node* new_node = create_node(data);
    new_node->next_node = list->head;
    list->head = new_node;
}

// Function to insert a new node containing data at index position
// Insertion takes O(1) time but finding the node at the
// insertion point takes O(n) time
void insert(LinkedList* list, int data, int index) {
    if (index == 0) {
        add(list, data);
        return;
    }

    Node* new_node = create_node(data);
    Node* current = list->head;

    for (int i = 0; i < index - 1 && current != NULL; i++) {
        current = current->next_node;
    }

    if (current == NULL) {
        printf("Index out of range\n");
        return;
    }

    new_node->next_node = current->next_node;
    current->next_node = new_node;
}

// Function to print the linked list
void print_list(LinkedList* list) {
    Node* current = list->head;
    while (current != NULL) {
        printf("[%d] -> ", current->data);
        current = current->next_node;
    }
    printf("NULL\n");
}

int main() {
    LinkedList* l = create_linked_list();
    add(l, 10);
    add(l, 20);
    add(l, 45);
    add(l, 15);
    insert(l, 30, 2);
    print_list(l);
    return 0;
}
