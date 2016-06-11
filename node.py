class Node():
    def __init__(self, task, next=None):
        """
        The function initiates a new Node object that keeps 2 variables:
        task and next.

        :param task: StringTask object, the task saved on this node
        :param next: Node object if there is a Node next on queue
                     None for default (last node on queue)
        :return: None
        """

        self._task = task
        self._next = next

    def get_priority(self):
        """
        The function returns the priority of the task

        :return: float, priority of the task
        """

        # Using get_priority() of StringTask:
        return self._task.get_priority()

    def set_priority(self, new_priority):
        """
        The function change the priority of the task to new_priority

        :param new_priority: float, new priority for the task
        :return: None
        """

        # Using set_priority() of StringTask:
        self._task.set_priority(new_priority)

    def get_task(self):
        """
        The function returns the task

        :return: StringTask object, the task
        """

        return self._task

    def get_next(self):
        """
        The function returns the next node on queue (if exist)

        :return: Node object if there is a node next on queue
                 None if there isn't
        """

        return self._next

    def set_next(self, next_node):
        """
        The function change the next node of this node to next_node

        :param next_node: Node object
        :return: None
        """

        self._next = next_node

    def has_next(self):
        """
        The function checks if there is a node next on queue

        :return: True if next node is a Node object
                 False if next node is None
        """
        if self._next:
            return True
        else:
            return False