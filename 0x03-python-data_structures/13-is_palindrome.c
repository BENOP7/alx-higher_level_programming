#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a linked list of integers is a palindrome
 * @head: the linked list
 *
 * Return: 1 if palindrome 0, otherwise
 */
int is_palindrome(listint_t **head)
{
	int i = 1;
	size_t len = 0;
	listint_t *tmp = NULL;
	listint_t *node = *head;
	int middle = 0;

	while (node)
	{
		node = node->next;
		len++;
	}

	middle = len % 2 == 0 ? len / 2 - 1 : len / 2;
	node = (*head)->next;
	(*head)->next = NULL;
	while (i <= middle)
	{
		tmp = node->next;
		node->next = *head;
		*head = node;
		node = tmp;
		i++;
	}
	if (len % 2 == 1)
	{
		*head = (*head)->next;
	}
	while (*head)
	{
		if ((*head)->n != node->n)
			return (0);
		node = node->next;
		*head = (*head)->next;
	}

	return (1);
}
