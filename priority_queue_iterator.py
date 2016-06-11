class PriorityQueueIterator():
    def __init__(self, priority_queue):
        """
        The function initiates a new PriorityQueueIterator object, used to
        iterate over given PriorityQueue object

        :param priority_queue: PriorityQueue object
        :return: None
        """

        self._priority_queue = priority_queue
        self._current = self._priority_queue.get_head()

    def __iter__(self):
        """
        The function returns the self object (PriorityQueueIterator) object
        as an iterator

        :return: self
        """

        return self

    def __next__(self):
        """
        The function returns the task of current node on PriorityQueue

        :return: StringTask object
        """
        if not self.has_next():
            # If the iteration has reached the end of priority_queue
            raise StopIteration
        else:
            # Take the task from current node, move to the next node and
            # return the task

            task = self._current.get_task()
            self._current = self._current.get_next()
            return task

    def has_next(self):
        """
        The function check is the current is None, means the iterator has
        reached the end of priority_queue and if there is a next node or not

        :return: True if current is not None
                 False if current is none
        """
        if self._current is not None:
            return True
        else:
            return False