from typing import List

# In Python, arguments have integer default values
def spawn(cmd: List[str], search_path: bool = ..., verbose: bool = ...,
           dry_run: bool = ...) -> None: ...
def find_executable(executable: str, path: str = ...) -> str: ...
