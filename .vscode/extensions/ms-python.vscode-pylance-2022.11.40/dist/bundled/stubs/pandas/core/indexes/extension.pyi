from typing import Literal

from pandas.core.indexes.base import Index

class ExtensionIndex(Index):
    def __iter__(self): ...
    def dropna(self, how: Literal["any", "all"] = ...): ...
    def repeat(self, repeats, axis=...): ...
    def take(
        self, indices, axis: int = ..., allow_fill: bool = ..., fill_value=..., **kwargs
    ): ...
    def unique(self, level=...): ...
    def map(self, mapper, na_action=...): ...
    def astype(self, dtype, copy: bool = ...): ...