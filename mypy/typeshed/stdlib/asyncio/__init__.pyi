import sys
from collections.abc import Coroutine, Generator
from typing import Any, TypeVar
from typing_extensions import TypeAlias

# As at runtime, this depends on all submodules defining __all__ accurately.
from .base_events import *
from .coroutines import *
from .events import *
from .futures import *
from .locks import *
from .protocols import *
from .queues import *
from .runners import *
from .streams import *
from .subprocess import *
from .tasks import *
from .transports import *

if sys.version_info >= (3, 8):
    from .exceptions import *

if sys.version_info >= (3, 9):
    from .threads import *

if sys.version_info >= (3, 11):
    from .taskgroups import *
    from .timeouts import *

if sys.platform == "win32":
    from .windows_events import *
else:
    from .unix_events import *

_T = TypeVar("_T")

# Aliases imported by multiple submodules in typeshed
if sys.version_info >= (3, 12):
    _CoroutineLike: TypeAlias = Coroutine[Any, Any, _T]
else:
    _CoroutineLike: TypeAlias = Generator[Any, None, _T] | Coroutine[Any, Any, _T]
