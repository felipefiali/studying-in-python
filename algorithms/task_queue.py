def count_cycles_for_task_queue(tasks, cooldown):
    """"
    Given a list of tasks and a cooldown for the same type of task, count the number of cycles needed to execute the queue
    """
    last_execution = {}
    cycle = 0

    for task in tasks:
        if task not in last_execution:
            last_execution[task] = cycle
            cycle += 1
        else:
            cycles_to_add = cooldown - (cycle - last_execution[task] - 1)
            if cycles_to_add > 0:
                cycle += cycles_to_add

            last_execution[task] = cycle
            cycle += 1

    return cycle