"""
This is a module docstring.  

This module is used to examine different documentation styles and tools.
"""

def google_style_do_work(task_id: int, name: str) -> tuple(bool, list):
    """ Perform work with task_id by assigning it to name.

    This doesn't really do anything, but I wanted to establish a short 'first line' description and
    a longer more detailed descriptions.  I'm curious to see if this creates different behavior
    when generating test or when pop-up hints appear in IDEs. 

    Args:
        task_id (int): The unique ID of a task to be performed.
        name (str): The name of the worker to perform the task.

    Returns:
        tuple: a tuple containing:
            - is_successful (bool): True if the work was completed successfully.  False if there was a problem.
            - logs (list of str): Log entries from the worker performing the work.

    Raises:
        RuntimeError: if the task doesn't exist or the worker name doesn't exist.
    """
    
    print(f"assigning task {task_id} to worker {name}.")

    return true, []


def numpy_style_do_work(task_id: int, name: str) -> tuple(bool, list):
    """ Perform work with task_id by assigning it to name.

    This doesn't really do anything, but I wanted to establish a short 'first line' description and
    a longer more detailed descriptions.  I'm curious to see if this creates different behavior
    when generating test or when pop-up hints appear in IDEs. 

    Parameters
    ----------
    task_id : int
        The unique ID of a task to be performed.
    name : str, optional
        The name of the worker to perform the task.

    Returns
    -------
    tuple: a tuple containing:
            - is_successful (bool): True if the work was completed successfully.  False if there was a problem.
            - logs (list of str): Log entries from the worker performing the work.

    Raises
    ------
    RuntimeError
        If the task doesn't exist or the worker name doesn't exist.
    """
    
    print(f"assigning task {task_id} to worker {name}.")

    return true, []

def rst_style_do_work(task_id: int, name: str) -> tuple(bool, list):
    """ Perform work with task_id by assigning it to name.

    This doesn't really do anything, but I wanted to establish a short 'first line' description and
    a longer more detailed descriptions.  I'm curious to see if this creates different behavior
    when generating test or when pop-up hints appear in IDEs. 

    Parameters
    ----------
    task_id : int
        The unique ID of a task to be performed.
    name : str, optional
        The name of the worker to perform the task.

    Returns
    -------
    bool
        True if the work was completed successfully.  False if there was a problem.
    list
        Log entries from the worker performing the work.

    Raises
    ------
    RuntimeError
        If the task doesn't exist or the worker name doesn't exist.

    :param task_id: The unique ID of a task to be performed.
    :type task_id: int
    :param name: The name of the worker to perform the task.
    :type name: str
    :returns: tuple (is_successful, log) 
        WHERE
        bool is_successful is True if the work was completed successfully.  False if there was a problem. 
        list log is the log entries from the worker performing the work. 
    """
    
    print(f"assigning task {task_id} to worker {name}.")

    return true, []


google_style_do_work(3, "Bob")

numpy_style_do_work(712, "Chuck")

rst_style_do_work(432451, "worker-rgn4-cl823-n2354")

