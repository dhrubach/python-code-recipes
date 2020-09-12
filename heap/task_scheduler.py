###############################################################
# LeetCode Problem Number : 621
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/task-scheduler/
###############################################################

from collections import Counter
from heapq import heappop, heappush, heapify


class TaskScheduler:
    def leastInterval(self, tasks: [str], n: int) -> int:
        """ create a bag of tasks to identify the most frequent tasks """
        task_count = Counter(tasks)

        """ convert bag of tasks into a heap

            since heapq creates a min-heap by default, multiply each
            value with -1 so that we push the most frequent task upto
            the root node

            input : [A,A,A,B,C,D,E]
            heap  : [(-3, A), (-1, B), (-1, C), (-1, D), (-1, E)]
        """
        heap = [(-task_count[key], key) for key in task_count.keys()]
        heapify(heap)

        """ final answer : time taken to navigate all the tasks including cool off period """
        time_steps = 0

        """ navigate through the heap processing tasks till all
            have been processed
          """
        while heap:
            index, temp = 0, []

            """ run inner loop a maximum of (n + 1) times
                n --> cool off period
                extra 1 iteration --> to pop root node
            """
            while index <= n:
                """ increment time step """
                time_steps += 1

                if heap:
                    """ pop root node to denote a task has been processed.

                        first iteration will pop out the root node.
                        subsequent 'n' iterations will pop out remaining 'n'
                        tasks with a count frequency <= root node count frequency.
                    """
                    timing, taskid = heappop(heap)

                    """ 2 possibilities at this point -
                            poped task has an associated frequency of 1 --> no further action necessary
                            poped task has a frequency > 1 --> insert it into 'temp' with 1 reduced count

                            example : heap node -- (-3, 'A')
                                      this means task 'A' has to be processed 3 times.
                                      current iteration counts for 1 time. push
                                      remaining 2 tasks (-2, 'A') back to temp which will be
                                      transferred back to heap in line 70
                    """
                    if timing != -1:
                        temp.append((timing + 1, taskid))

                """ if both heap and temp are empty, then all tasks have been processed
                """
                if not heap and not temp:
                    break
                else:
                    index += 1

            """ move unprocessed tasks back into heap
                going by above example, move (-2, A) back to heap
            """
            for item in temp:
                heappush(heap, item)

        return time_steps


if __name__ == "__main__":
    tsc = TaskScheduler()
    ans = tsc.leastInterval(["A", "B", "A", "C", "A", "D", "E"], 2)
    print(ans)
