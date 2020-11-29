## schema-provider

Addressing https://github.com/python/typing/issues/182 :
generating type stubs and type validators from a type schema description.

**This project is WIP**. 

### Usage

A type schema description file:

```tex
\scheme MyJSON = {
    "a" : int | str,
     1  : float,
    "recur" : [MyJSON, *int]
}
```

generates a type stub file:

```python
from __future__ import annotations
import typing as __t
import typing_extensions as __te

class MyJSON(__te.Protocol):
    @__t.overload
    def __getitem__(self, key: __te.Literal["a"]) -> __t.Union[int, str]: ...
    @__t.overload    
    def __setitem__(self, key: __te.Literal["a"], value: __t.Union[int, str]) -> None: ...
    @__t.overload
    def __getitem__(self, key: __te.Literal[1]) -> float: ...
    @__t.overload    
    def __setitem__(self, key: __te.Literal[1], value: float) -> None: ...
    @__t.overload    
    def __getitem__(self, key: __te.Literal["recur"]) -> GeneratedType1: ...
    @__t.overload
    def __setitem__(self, key: __te.Literal["recur"], value: GeneratedType1) -> None: ...

def check_MyJSON(_: dict) -> MyJSON: ...
     

class GeneratedType1(__te.Protocol):
    @__t.overload
    def __getitem__(self, item: __te.Literal[0]) -> MyJSON: ...
    @__t.overload
    def __setitem__(self, item: __te.Literal[0], value: MyJSON) -> None: ...
    @__t.overload    
    def __getitem__(self, item: int) -> int: ...
    @__t.overload
    def __setitem__(self, item: int, value: int) -> None: ...
```

and a validation file:

```python
unset = object()
def check_MyJSON(value: dict):
    tmp = value.get("a", unset) 
    if isinstance(tmp, int) or isinstance(tmp, str):
        pass
    else:
        raise SomeExeption(type=MyJSON, path=".a", expect="int | str", got=str(tmp))
    
    ...
```
