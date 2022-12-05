#include <stdio.h>
#include <stdlib.h>

/**
* get_middle - finds a pointer to the middle of the given linked list
* head: a pointer to the first node of the linked list
*
* Return: a pointer to the middle nide of the linked list
* or null if it fails
*/
listint_t* get_middle(listint_t *head)
{
    if (head == NULL)
        {
            return (head);
        }
    listint_t *fast = head; /*to traverse by two step*/
    listint_t *slow = head; /*to traverse by one step*/
    
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        slow = slow->next;
    }
    return (slow);
}

/**
* reverse - reverses the last half of the linked list
* @head: pointer to the first node in the list
*
* Return: a poiter to the first value of the halved list
*/
listint_t* reverse(listint_t *head)
{
    if (head == NULL || head->next == NULL)
    {
        return (head);
    }
    listint_t *temp = reverse(head->next);
    head->next->next = head;
    head->next = NULL;
    return temp;
}

/**
* is_palindrome - checks if a singly linked list is a palindrome.
* @head: pointer of pointer to the first element of the linked list
*
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
    listint_t *mid = get_middle(*head);
    mid = reverse(mid);
    while (mid != NULL)
    {
        if (head->n != mid->n)
            {
                return (0);
            }
        head = head->next;
        mid = mid->next;
    }
    return (1);
}
