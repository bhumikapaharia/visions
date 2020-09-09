from typing import Sequence

import pandas as pd
from pandas.api import types as pdt

from visions.relations import IdentityRelation, TypeRelation
from visions.types.type import VisionsBaseType


def _get_relations(cls) -> Sequence[TypeRelation]:
    from visions.types import Optional

    relations = [IdentityRelation(cls, Optional)]
    return relations


class TimeDelta(VisionsBaseType):
    """**TimeDelta** implementation of :class:`visions.types.type.VisionsBaseType`.

    Examples:
        >>> x = pd.Series([pd.Timedelta(days=i) for i in range(3)])
        >>> x in visions.Timedelta
        True
    """

    @classmethod
    def get_relations(cls) -> Sequence[TypeRelation]:
        return _get_relations(cls)

    @classmethod
    def contains_op(cls, series: pd.Series, state: dict) -> bool:
        return pdt.is_timedelta64_dtype(series)
