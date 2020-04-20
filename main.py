class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None

        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node

            for element in nodes:
                node.next = Node(element)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next

        nodes.append("None")

        return ' -> '.join(str(x) for x in nodes)


def remove_duplicates(head):
    unique_items = {}

    current = head
    previous = None

    while current is not None:
        current_data = current

        if current_data.data[0] in unique_items and current_data.data[1] == unique_items[current_data.data[0]]:
            previous.next = current.next
        else:
            unique_items[current_data.data[0]] = current_data.data[1]
            previous = current

        current = current.next


linked_list = LinkedList([["teste1@live.com", "Olá, teste2"], ["teste2@gmail.com", "Prezado, teste1"],
                          ["teste1@live.com", "Olá, teste2"], ["teste3@live.com", "Olá, teste1 e teste2"],
                          ["teste2@gmail.com", "Prezado, teste1"], ["teste1@live.com", "Olá, teste2"],
                          ["teste2@safada.com", "Prezado, repetiu uns emails"]])
print(linked_list)
remove_duplicates(linked_list.head)
print(linked_list)
