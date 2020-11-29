from __future__ import annotations

from dataclasses import dataclass
from typing import *

@dataclass
class JType:
    typename: str
    targs: List[str]
    shape: Shape

@dataclass
class JList:
    _: 'List[Shape]'
    tail: Shape

@dataclass
class JGeneric:
    base: str
    type_args: List[Shape]

@dataclass
class JNamed:
    n: str

@dataclass
class JUnion:
    l: Shape
    r: Shape

@dataclass
class JInt:
    _: int

@dataclass
class JStr:
    _: str

@dataclass
class JFloat:
    _: float

Shape = Union[JNamed, JFloat, JInt, JStr, JGeneric, JList, JUnion]
