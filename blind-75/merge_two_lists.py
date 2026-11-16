class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values):
    dummy = ListNode(-1)
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next

list1 = create_linked_list([1, 3, 5])
list2 = create_linked_list([2, 4, 6])

def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")



def mergeLinkedList(list1,list2):
    dummy = ListNode(-1)
    current = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
            current = current.next
        
        else:
            current.next = list2
            list2 = list2.next
            current = current.next

    if list1:
        current.next = list1
    else:
        current.next = list2     

    return dummy.next
    


merged = mergeLinkedList(list1, list2)
print_linked_list(merged)