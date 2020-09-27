from datetime import timedelta
from functools import singledispatch
from typing import Iterable, Sequence

from visions.backends.python.series_utils import sequence_not_empty
from visions.relations import IdentityRelation, TypeRelation
from visions.types.type import VisionsBaseType


@singledispatch
@sequence_not_empty
def time_delta_contains(sequence: Iterable, state: dict) -> bool:
    return all(isinstance(value, timedelta) for value in sequence)


class TimeDelta(VisionsBaseType):
    """**TimeDelta** implementation of :class:`visions.types.type.VisionsBaseType`.

    Examples:
        >>> x = [timedelta(hours=1), timedelta(hours=3)]
        >>> x in visions.Timedelta
        True
    """

    @classmethod
    def get_relations(cls) -> Sequence[TypeRelation]:
        from visions.types import Generic

        relations = [IdentityRelation(cls, Generic)]
        return relations

    @classmethod
    def contains_op(cls, sequence: Iterable, state: dict) -> bool:
        return time_delta_contains(sequence, state)
