#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
* reverse - reverses a singly linked list
* @head: a pointer to the first element
*
* Return: pointer to the first element of the reversed list
*/
listint_t *reverse(listint_t *head)
{
    listint_t *prev = NULL;
    listint_t *next_ptr = NULL;

    while (head != NULL)
    {
        next_ptr = head->next;
        head->next = prev;
        prev = head;
        head = next_ptr;
    }
    return (prev);
}
/**
* is_palindrome - checks if a singly linked list is a palindrome.
* @head: pointer of pointer to the first element of the list
*
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
    if (head == NULL || *head.next == NULL)
        return 1;
    listint_t **slow = head;
    listint_t **fast = head;

    /*find the middle of the list*/
    while (fast->next != NULL && fast->next->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;
    }
    slow->next = reverse(slow->next);
    slow = slow->next;
    /*check if the left half is equall to right half*/
    while (slow != NULL)
    {
        if (head->n != slow->n)
        {
            return (0);
        }
        head = head->next;
        slow = slow->next;
    }
     return (1);
}
