#include "lists.h"

/**
 * check_cycle - check if a singly linked list has a cycle
 * @list: first node (head)
 *
 * Return: 1 if list has a cycle, 0 if list has no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current;
	
	if (list == NULL)
		return (0);
	current = list->next;
	while (current)
	{
		if (current == list)
			return (1);
		current = current->next;
	}
	return (0);
}
