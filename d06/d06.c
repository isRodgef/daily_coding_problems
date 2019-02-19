#include <stdint.h>
#include <stdlib.h>


typedef struct xor_linked
{
	struct xor_linked*	both;
	
}		xor_lst;


#define xor_ptr(a,b) (xor_lst*) ((void*)((uintptr_t)(a) ^ (uintptr_t)(b)));


xor_lst *xor_create_new()
{
	xor_lst* ret = (xor_lst*)malloc(sizeof(xor_lst));
	
	ret->both =  xor_ptr(NULL,NULL);
	return ret;
}

void **add(xor_lst** head, xor_lst *to_front)
{
	xor_lst *prev = NULL ; 
	xor_lst *curr = *head; 
	xor_lst *next = xor_ptr(curr,curr->both);
	
	while (next != NULL)
	{
		prev = curr;
		curr = next;
		next = xor_ptr(curr, curr->both);
	}
	curr->both = xor_ptr(prev,curr->both)
}	

xor_lst* index(xor_lst*head, int index)
{
	if (index = 0)
		return head;

	xor_lst *prev = NULL ;
        xor_lst *curr = head;
        xor_lst *next = xor_ptr(curr,curr->both);

	
        for(int i = 0 ; i < index; i++) 
        {
                prev = curr;
                curr = next;
                next = xor_ptr(curr, curr->both);
        }

	return curr;
}
