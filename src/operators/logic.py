import random
from types import NoneType

from typing import (
    TYPE_CHECKING,
    Callable,
    Generic,
    List,
    Optional,
    Tuple,
    TypeVar,
    Union,
    get_args,
)
from src import OpCode, Signed, Statement, Unsigned

from src.constants import Constant
from src.operators import BinaryOperatorFuzzMixin, UnaryOperatorFuzzMixin
from src.predicates import HasValidBaseTypeAndSign, IsValidLogicalOperand

if TYPE_CHECKING:
    from src.context import Context
from src.types.abstract_types import (
    NumericalType,
)
from src.types.concrete_types import (
    OpTypeBool,
    OpTypeFloat,
    OpTypeInt,
    OpTypeVector,
    Type,
)

Operand = Statement | Constant

S = TypeVar("S")
D = TypeVar("D")
SC = TypeVar("SC")
DC = TypeVar("DC")


class LogicalOperator(Statement, Generic[S, D, SC, DC]):
    OPERAND_SELECTION_PREDICATE: Callable[
        [Operand], bool
    ] = lambda _, target_type, signed: lambda op: IsValidLogicalOperand(
        op
    ) and HasValidBaseTypeAndSign(
        op, target_type, signed
    )


class UnaryLogicalOperator(LogicalOperator[S, Optional[D], Optional[SC], Optional[DC]]):
    type: Type = None
    operand: Operand = None

    def to_spasm(self, context: "Context") -> str:
        return f"%{self.id} = {self.__class__.__name__} %{context.tvc[self.type]} %{self.operand.id}"


class BinaryLogicalOperator(
    LogicalOperator[S, Optional[D], Optional[SC], Optional[DC]]
):
    type: Type = None
    operand1: Operand = None
    operand2: Operand = None

    def to_spasm(self, context: "Context") -> str:
        return f"%{self.id} = {self.__class__.__name__} %{context.tvc[self.type]} %{self.operand1.id} %{self.operand2.id}"


# class OpAny(UnaryLogicalOperatorFuzzMixin, UnaryLogicalOperator[OpTypeBool]):
#     ...

# class OpAll(UnaryLogicalOperatorFuzzMixin, UnaryLogicalOperator[OpTypeBool]):
#     ...


class OpLogicalEqual(
    BinaryOperatorFuzzMixin, BinaryLogicalOperator[OpTypeBool, OpTypeBool, None, None]
):
    ...


class OpLogicalNotEqual(
    BinaryOperatorFuzzMixin, BinaryLogicalOperator[OpTypeBool, OpTypeBool, None, None]
):
    ...


class OpLogicalOr(
    BinaryOperatorFuzzMixin, BinaryLogicalOperator[OpTypeBool, OpTypeBool, None, None]
):
    ...


class OpLogicalAnd(
    BinaryOperatorFuzzMixin, BinaryLogicalOperator[OpTypeBool, OpTypeBool, None, None]
):
    ...


class OpLogicalNot(
    UnaryOperatorFuzzMixin, UnaryLogicalOperator[OpTypeBool, OpTypeBool, None, None]
):
    ...


class OpIEqual(
    BinaryOperatorFuzzMixin, BinaryLogicalOperator[OpTypeInt, OpTypeBool, None, None]
):
    ...


class OpINotEqual(
    BinaryOperatorFuzzMixin, BinaryLogicalOperator[OpTypeInt, OpTypeBool, None, None]
):
    ...


class OpUGreaterThan(
    BinaryOperatorFuzzMixin,
    BinaryLogicalOperator[OpTypeInt, OpTypeBool, Unsigned, None],
):
    ...


class OpSGreaterThan(
    BinaryOperatorFuzzMixin, BinaryLogicalOperator[OpTypeInt, OpTypeBool, Signed, None]
):
    ...


class OpUGreaterThanEqual(
    BinaryOperatorFuzzMixin,
    BinaryLogicalOperator[OpTypeInt, OpTypeBool, Unsigned, None],
):
    ...


class OpSGreaterThanEqual(
    BinaryOperatorFuzzMixin, BinaryLogicalOperator[OpTypeInt, OpTypeBool, Signed, None]
):
    ...


class OpULessThan(
    BinaryOperatorFuzzMixin,
    BinaryLogicalOperator[OpTypeInt, OpTypeBool, Unsigned, None],
):
    ...


class OpSLessThan(
    BinaryOperatorFuzzMixin, BinaryLogicalOperator[OpTypeInt, OpTypeBool, Signed, None]
):
    ...


class OpULessThanEqual(
    BinaryOperatorFuzzMixin,
    BinaryLogicalOperator[OpTypeInt, OpTypeBool, Unsigned, None],
):
    ...


class OpSLessThanEqual(
    BinaryOperatorFuzzMixin, BinaryLogicalOperator[OpTypeInt, OpTypeBool, Signed, None]
):
    ...


class OpFOrdEqual(
    BinaryOperatorFuzzMixin, BinaryLogicalOperator[OpTypeFloat, OpTypeBool, None, None]
):
    ...


class OpFUnordEqual(
    BinaryOperatorFuzzMixin, BinaryLogicalOperator[OpTypeFloat, OpTypeBool, None, None]
):
    ...


class OpFOrdNotEqual(
    BinaryOperatorFuzzMixin, BinaryLogicalOperator[OpTypeFloat, OpTypeBool, None, None]
):
    ...


class OpFUnordNotEqual(
    BinaryOperatorFuzzMixin, BinaryLogicalOperator[OpTypeFloat, OpTypeBool, None, None]
):
    ...


class OpFOrdLessThan(
    BinaryOperatorFuzzMixin, BinaryLogicalOperator[OpTypeFloat, OpTypeBool, None, None]
):
    ...


class OpFUnordLessThan(
    BinaryOperatorFuzzMixin, BinaryLogicalOperator[OpTypeFloat, OpTypeBool, None, None]
):
    ...


class OpFOrdGreaterThan(
    BinaryOperatorFuzzMixin, BinaryLogicalOperator[OpTypeFloat, OpTypeBool, None, None]
):
    ...


class OpFUnordGreaterThan(
    BinaryOperatorFuzzMixin, BinaryLogicalOperator[OpTypeFloat, OpTypeBool, None, None]
):
    ...


class OpFOrdLessThanEqual(
    BinaryOperatorFuzzMixin, BinaryLogicalOperator[OpTypeFloat, OpTypeBool, None, None]
):
    ...


class OpFUnordLessThanEqual(
    BinaryOperatorFuzzMixin, BinaryLogicalOperator[OpTypeFloat, OpTypeBool, None, None]
):
    ...


class OpFOrdGreaterThanEqual(
    BinaryOperatorFuzzMixin, BinaryLogicalOperator[OpTypeFloat, OpTypeBool, None, None]
):
    ...


class OpFUnordGreaterThanEqual(
    BinaryOperatorFuzzMixin, BinaryLogicalOperator[OpTypeFloat, OpTypeBool, None, None]
):
    ...
