from node import Node
from priority_queue_iterator import PriorityQueueIterator


class PriorityQueue():
    def __init__(self, tasks=[]):
        """
        The function initiates a new PriorityQueue object, creation new Node
        objects for each task on tasks list and putting them on the queue

        :param tasks: list of StringTasks objects, tasks
        :return: None
        """
        self._tasks = tasks
        self._head = None
        self._length = 0
        self._current = None
        self._start = False
        for i in self._tasks:
            # If there are tasks on tasks list, insert each task to the queue
            # using enque()
            self.enque(i)


    def enque(self, task):
        """
        The function insert a new Node with the task to the queue on the right
        position depends on the task's priority

        :param task: StringTask object, new task
        :return: None
        """

        # Add 1 to the length of the queue
        self._length += 1

        if self._head is None:
            # If the queue is empty, just add the task to the queue and set
            # the head to the new task node
            self._head = Node(task)
        elif task.get_priority() > self._head.get_priority():
            # If the queue is not empty and the task priority is larger then
            # the head priority, set the next node of the new task node to the
            # current head and change the head to the new task node
            self._head = Node(task, self._head)
        else:
            # If the queue is not empty and the new task priority is not
            # larger then the head priority
            current_node = self._head
            next_node = current_node.get_next()
            while current_node.has_next():
                if task.get_priority() > next_node.get_priority():
                    # While the current node has a next node, compare the
                    # task priority to the next node priority. If the first
                    # is larger, break the loop
                    break

                # Change the current node to the next node, and the next node
                # to the next-next-node
                current_node = next_node
                next_node = next_node.get_next()

            # Create a new Node for the task pointing to next node (where
            # its priority < the task priority or it is None)
            # and set the next node of the current node (where its priority
            # is >= the task priority to the new task Node
            current_node.set_next(Node(task, next_node))

    def peek(self):
        """
        The function returns the task of the head of queue

        :return: StringTask object, task of head of queue is not empty
                 None if the queue is empty
        """

        if self._head is None:
            # If the queue is empty
            return None
        else:
            # Return the head task without remove it from queue
            return self._head.get_task()

    def deque(self):
        """
        The function returns the task of the head node (if exists) and removes
        the head from queue

        :return: StringTask object, task of head of queue is not empty
                 None if the queue is empty
        """

        if self._head is None:
            # If the queue is empty
            return None
        else:
            # Reduce 1 from the length of the queue
            self._length -= 1

            # Return the head task and remove head from queue
            task = self._head.get_task()
            self._head = self._head.get_next()
            return task

    def get_head(self):
        """

        :return:
        """
        return self._head

    def change_priority(self, old, new):
        """
        The function checks if there is a task Node with priority == old,
        and if so, change its priority to new

        :param old: float, old priority to look for
        :param new: float, new priority to set
        :return: None
        """

        prev = None
        current = self._head

        while current is not None:
            if current.get_priority() == old:
                current.set_priority(new)
                next = current.get_next()
                if prev is None:
                    if next is not None and next.get_priority() > \
                            current.get_priority():
                        self._head = next
                        self.enque(current.get_next())
                else:
                    if prev.get_priority() < current.get_priority() or \
                            next.get_priority() > current.get_priority():
                        prev.set_next(next)
                        self.enque(current.get_task())
                break

            prev = current
            current = current.get_next()

    def __len__(self):
        """
        The function returns the length of the queue

        :return: int, the length of the queue
        """

        return self._length

    def __iter__(self):
        """
        The function returns an PriorityQueueIterator object, used to
        iterate over the queue

        :return: PriorityQueueIterator object
        """

        return PriorityQueueIterator(self)

    def __next__(self):
        """
        The function returns the task of current node on queue

        :return: StringTask object
        """

        if self._start is False:
            # If this is the start of the iteration, set current as head and
            #  set start as True
            self._current = self._head
            self._start = True

        if self._current is None:
            # If the iteration reached the end of queue, stop the iteration
            raise StopIteration
        else:
            # Take the task from current node, set current to the next node,
            #  and return the task
            task = self._current.get_task()
            self._current = self._current.get_next()
            return task

    def __str__(self):
        """
        The function creates and returns a string that looks like [task1,
        task2, task3] where every task is represented by its __str__ function

        :return: string
        """

        queue_str = "["

        for task in self:
            # Add each str(task) to queue_str with ", " at end
            queue_str += repr(task) + ", "

        # Slice the last ", " of queue_str and add "]" to queue_str to make
        # it look as requested
        if len(queue_str) > 1:
            queue_str = queue_str[:len(queue_str)-2]
        queue_str += "]"

        return queue_str

    def __add__(self, other):
        """
        The function returns a new PriorityQueue object with the task nodes
        from the self and other PriorityQueue objects

        :param other: PriorityQueue object
        :return: PriorityQueue object = self + other
        """
        new_queue = PriorityQueue()

        for task in other:
            new_queue.enque(task)

        for task in self:
            new_queue.enque(task)

        return new_queue

    def __eq__(self, other):
        """

        :param other:
        :return:
        """

        if len(self) != len(other):
            return False
        else:
            current = self._head
            for task in other:
                if current.get_task() != task:
                    return False

                current = current.get_next()

            return True