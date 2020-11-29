from schema_provider.ts import *
from typing import *
from typing_extensions import *
class S(Protocol):
    @overload
    def __getitem__(self, item: Literal["a"]) -> int:
        ...

    @overload
    def __getitem__(self, item: Literal["b"]) -> int:
        ...

    @overload
    def __getitem__(self, item) -> str: ...



x : S = cast(S, {})

def gen_JType(t: JType):
    if t.targs:
        print(f"class {t.typename}(__te.Protocol[{','.join(t.targs)}]):")
    else:
        print(f"class {t.typename}(__te.Protocol):")

    gen_Shape(t.shape)

def gen_Shape(s: Shape):
    raise NotImplemented
