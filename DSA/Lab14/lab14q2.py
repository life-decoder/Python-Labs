"""Task scheduling (minimum machines) Greedy implementation.

Given a list of tasks with (start, finish) times, schedule all tasks using the
minimum number of machines. Each machine can run at most one task at a time.

This is the classic interval graph coloring problem. A greedy algorithm that
processes tasks in order of start time and always assigns each task to the
machine that becomes available the earliest produces an optimal schedule.

The module provides:

- schedule_tasks(tasks): returns a list of machines where each machine is a list
  of tasks assigned to it.

Example usage:
    tasks = [
        ("A", 1, 4),
        ("B", 2, 3),
        ("C", 3, 5),
        ("D", 4, 7),
    ]

    machines = schedule_tasks(tasks)
    print(len(machines))
    for i, machine in enumerate(machines, 1):
        print(i, machine)
"""

from __future__ import annotations

import argparse
from typing import Iterable, List, Tuple

Task = Tuple[str, int, int]


def schedule_tasks(tasks: Iterable[Task]) -> List[List[Task]]:
    """Schedule tasks using the minimum number of machines (heap-based).

    This implementation uses a min-heap to efficiently track the next machine
    that becomes available, which gives O(n log n) behavior.

    Args:
        tasks: An iterable of (task_id, start, finish) tuples.

    Returns:
        A list of machines, where each machine is a list of tasks assigned to it.
    """

    from heapq import heappush, heappop

    # Sort by start time; tie-break by finish time (earliest finish first).
    sorted_tasks = sorted(tasks, key=lambda t: (t[1], t[2]))

    # Min-heap to track machine availability: (finish_time, machine_index)
    # A machine is available once its last task finishes.
    free_machines: List[Tuple[int, int]] = []
    machines: List[List[Task]] = []

    for task in sorted_tasks:
        task_id, start, finish = task
        if finish < start:
            raise ValueError(f"Task {task_id} has finish < start ({start} -> {finish})")

        # If there is a machine free before or at the task start, reuse it.
        if free_machines and free_machines[0][0] <= start:
            _, machine_idx = heappop(free_machines)
            machines[machine_idx].append(task)
            heappush(free_machines, (finish, machine_idx))
        else:
            # No existing machine is free; create a new one.
            machine_idx = len(machines)
            machines.append([task])
            heappush(free_machines, (finish, machine_idx))

    return machines


def schedule_tasks_no_heap(tasks: Iterable[Task]) -> List[List[Task]]:
    """Schedule tasks using the minimum number of machines (no heap).

    This implementation scans existing machines to find the earliest one that is
    free for each task. It is O(n*m) in the worst case, where m is the number of
    machines.
    """

    # Sort by start time; tie-break by finish time (earliest finish first).
    sorted_tasks = sorted(tasks, key=lambda t: (t[1], t[2]))

    # Track the tasks assigned to each machine and its current finish time.
    machines: List[List[Task]] = []
    machine_finish: List[int] = []

    for task in sorted_tasks:
        task_id, start, finish = task
        if finish < start:
            raise ValueError(f"Task {task_id} has finish < start ({start} -> {finish})")

        # Find an existing machine that is free by the start time.
        best_idx = -1
        best_finish = None
        for i, ftime in enumerate(machine_finish):
            if ftime <= start:
                # We prefer the machine that became free the earliest.
                if best_finish is None or ftime < best_finish:
                    best_finish = ftime
                    best_idx = i

        if best_idx >= 0:
            machines[best_idx].append(task)
            machine_finish[best_idx] = finish
        else:
            machines.append([task])
            machine_finish.append(finish)

    return machines


def _format_schedule(machines: List[List[Task]]) -> str:
    lines: List[str] = []
    lines.append(f"Number of machines used: {len(machines)}")
    for i, machine in enumerate(machines, start=1):
        lines.append(f"Machine {i}:")
        for task_id, start, finish in machine:
            lines.append(f"  {task_id}: start={start}, finish={finish}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="python lab14q2.py",
        description="Task scheduling example (minimum machines).",
    )
    parser.add_argument(
        "--mode",
        choices=["heap", "no-heap"],
        default="no-heap",
        help="Scheduling strategy (heap: O(n log n); no-heap: O(n*m)).",
    )
    args = parser.parse_args()

    # Example tasks (including equal start times).
    example_tasks: List[Task] = [
        ("T1", 1, 4),
        ("T2", 2, 3),
        ("T3", 3, 5),
        ("T4", 4, 7),
        ("T5", 1, 2),
        ("T6", 2, 5),
        ("T7", 5, 9),
        ("T8", 5, 6),
        ("T9", 5, 8),
        ("T10", 1, 3),
    ]

    if args.mode == "heap":
        machines = schedule_tasks(example_tasks)
    else:
        machines = schedule_tasks_no_heap(example_tasks)

    print(f"Using method: {args.mode}\n")
    print(_format_schedule(machines))


if __name__ == "__main__":
    main()
