#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# import getpass
from ast import parse
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

from mod import (
    isModule,
    isInteractive,
    isExpression,
    isFunctionType
)

from stmt import (
    isFunctionDef,
    isAsyncFunctionDef,
    isClassDef,
    isReturn,
    isDelete,
    isAssign,
    isAugAssign,
    isAnnAssign,
    isFor,
    isAsyncFor,
    isWhile,
    isIf,
    isWith,
    isAsyncWith,
    isRaise,
    isTry,
    isAssert,
    isImport,
    isImportFrom,
    isGlobal,
    isNonlocal,
    isExpr,
    isPass,
    isBreak,
    isContinue,
    # isAttributes as isStmtAttributes
)

from expr import (
    isBoolOp,
    isNamedExpr,
    isBinOp,
    isUnaryOp,
    isLambda,
    isIfExp,
    isDict,
    isSet,
    isListComp,
    isSetComp,
    isDictComp,
    isGeneratorExp,
    isAwait,
    isYield,
    isYieldFrom,
    isCompare,
    isCall,
    isFormattedValue,
    isJoinedStr,
    isConstant,
    isAttribute,
    isSubscript,
    isStarred,
    isName,
    isList,
    isTuple,
    isSlice,
    # isAttributes as isExprAttributes
)
from expr_context import (
    isLoad,
    isStore,
    isDel
)

from boolop import (
    isAnd,
    isOr
)

from module_operator import (
    isAdd,
    isSub,
    isMult,
    isMatMult,
    isDiv,
    isMod,
    isPow,
    isLShift,
    isRShift,
    isBitOr,
    isBitXor,
    isBitAnd,
    isFloorDiv
)

from unaryop import (
    isInvert,
    isNot,
    isUAdd,
    isUSub
)

from cmpop import (
    isEq,
    isNotEq,
    isLt,
    isLtE,
    isGt,
    isGtE,
    isIs,
    isIsNot,
    isIn,
    isNotIn
)

from comprehension import (
    isComprehension
)

from excepthandler import (
    isExceptHandler
)

from arguments import (
    isArguments
)

from arg import (
    isArg
)

from module_keyword import (
    isKeyword
)

from alias import (
    isAlias
)

from withitem import (
    isWithitem
)

from type_ignore import (
    isTypeIgnore
)


def parse_nodes(nodes, nest=1):
    nest += 1
    output_dict = {}

    # mod
    isModule(nodes, output_dict, nest, parse_nodes)
    isInteractive(nodes, output_dict, nest, parse_nodes)
    isExpression(nodes, output_dict, nest, parse_nodes)
    isFunctionType(nodes, output_dict, nest, parse_nodes)

    #stmt
    isFunctionDef(nodes, output_dict, nest, parse_nodes)
    isAsyncFunctionDef(nodes, output_dict, nest, parse_nodes)
    isClassDef(nodes, output_dict, nest, parse_nodes)
    isReturn(nodes, output_dict, nest, parse_nodes)
    isDelete(nodes, output_dict, nest, parse_nodes)
    isAssign(nodes, output_dict, nest, parse_nodes)
    isAugAssign(nodes, output_dict, nest, parse_nodes)
    isAnnAssign(nodes, output_dict, nest, parse_nodes)
    isFor(nodes, output_dict, nest, parse_nodes)
    isAsyncFor(nodes, output_dict, nest, parse_nodes)
    isWhile(nodes, output_dict, nest, parse_nodes)
    isIf(nodes, output_dict, nest, parse_nodes)
    isWith(nodes, output_dict, nest, parse_nodes)
    isAsyncWith(nodes, output_dict, nest, parse_nodes)
    isRaise(nodes, output_dict, nest, parse_nodes)
    isTry(nodes, output_dict, nest, parse_nodes)
    isAssert(nodes, output_dict, nest, parse_nodes)
    isImport(nodes, output_dict, nest, parse_nodes)
    isImportFrom(nodes, output_dict, nest, parse_nodes)
    isGlobal(nodes, output_dict, nest, parse_nodes)
    isNonlocal(nodes, output_dict, nest, parse_nodes)
    isExpr(nodes, output_dict, nest, parse_nodes)
    isPass(nodes, output_dict, nest, parse_nodes)
    isBreak(nodes, output_dict, nest, parse_nodes)
    isContinue(nodes, output_dict, nest, parse_nodes)
    # isStmtAttributes(nodes, output_dict, nest, parse_nodes)

    #expr
    isBoolOp(nodes, output_dict, nest, parse_nodes)
    isNamedExpr(nodes, output_dict, nest, parse_nodes)
    isBinOp(nodes, output_dict, nest, parse_nodes)
    isUnaryOp(nodes, output_dict, nest, parse_nodes)
    isLambda(nodes, output_dict, nest, parse_nodes)
    isIfExp(nodes, output_dict, nest, parse_nodes)
    isDict(nodes, output_dict, nest, parse_nodes)
    isSet(nodes, output_dict, nest, parse_nodes)
    isListComp(nodes, output_dict, nest, parse_nodes)
    isSetComp(nodes, output_dict, nest, parse_nodes)
    isDictComp(nodes, output_dict, nest, parse_nodes)
    isGeneratorExp(nodes, output_dict, nest, parse_nodes)
    isAwait(nodes, output_dict, nest, parse_nodes)
    isYield(nodes, output_dict, nest, parse_nodes)
    isYieldFrom(nodes, output_dict, nest, parse_nodes)
    isCompare(nodes, output_dict, nest, parse_nodes)
    isCall(nodes, output_dict, nest, parse_nodes)
    isFormattedValue(nodes, output_dict, nest, parse_nodes)
    isJoinedStr(nodes, output_dict, nest, parse_nodes)
    isConstant(nodes, output_dict, nest, parse_nodes)
    isAttribute(nodes, output_dict, nest, parse_nodes)
    isSubscript(nodes, output_dict, nest, parse_nodes)
    isStarred(nodes, output_dict, nest, parse_nodes)
    isName(nodes, output_dict, nest, parse_nodes)
    isList(nodes, output_dict, nest, parse_nodes)
    isTuple(nodes, output_dict, nest, parse_nodes)
    isSlice(nodes, output_dict, nest, parse_nodes)
    # isExprAttributes(nodes, output_dict, nest, parse_nodes)

    #expr_context
    isLoad(nodes, output_dict, nest, parse_nodes)
    isStore(nodes, output_dict, nest, parse_nodes)
    isDel(nodes, output_dict, nest, parse_nodes)

    # boolop
    isAnd(nodes, output_dict, nest, parse_nodes)
    isOr(nodes, output_dict, nest, parse_nodes)

    # operator
    isAdd(nodes, output_dict, nest, parse_nodes)
    isSub(nodes, output_dict, nest, parse_nodes)
    isMult(nodes, output_dict, nest, parse_nodes)
    isMatMult(nodes, output_dict, nest, parse_nodes)
    isDiv(nodes, output_dict, nest, parse_nodes)
    isMod(nodes, output_dict, nest, parse_nodes)
    isPow(nodes, output_dict, nest, parse_nodes)
    isLShift(nodes, output_dict, nest, parse_nodes)
    isRShift(nodes, output_dict, nest, parse_nodes)
    isBitOr(nodes, output_dict, nest, parse_nodes)
    isBitXor(nodes, output_dict, nest, parse_nodes)
    isBitAnd(nodes, output_dict, nest, parse_nodes)
    isFloorDiv(nodes, output_dict, nest, parse_nodes)

    # unaryop
    isInvert(nodes, output_dict, nest, parse_nodes)
    isNot(nodes, output_dict, nest, parse_nodes)
    isUAdd(nodes, output_dict, nest, parse_nodes)
    isUSub(nodes, output_dict, nest, parse_nodes)

    # cmpop
    isEq(nodes, output_dict, nest, parse_nodes)
    isNotEq(nodes, output_dict, nest, parse_nodes)
    isLt(nodes, output_dict, nest, parse_nodes)
    isLtE(nodes, output_dict, nest, parse_nodes)
    isGt(nodes, output_dict, nest, parse_nodes)
    isGtE(nodes, output_dict, nest, parse_nodes)
    isIs(nodes, output_dict, nest, parse_nodes)
    isIsNot(nodes, output_dict, nest, parse_nodes)
    isIn(nodes, output_dict, nest, parse_nodes)
    isNotIn(nodes, output_dict, nest, parse_nodes)

    # comprehension
    isComprehension(nodes, output_dict, nest, parse_nodes)

    # except_handler
    isExceptHandler(nodes, output_dict, nest, parse_nodes)

    # arguments
    isArguments(nodes, output_dict, nest, parse_nodes)
    
    # arg
    isArg(nodes, output_dict, nest, parse_nodes)

    # keyword
    isKeyword(nodes, output_dict, nest, parse_nodes)

    # alias
    isAlias(nodes, output_dict, nest, parse_nodes)

    # withitem
    isWithitem(nodes, output_dict, nest, parse_nodes)

    # type_ignore
    isTypeIgnore(nodes, output_dict, nest, parse_nodes)

    if isinstance(nodes, list):
        aList = []
        for aNode in nodes:
            aList.append(parse_nodes(aNode, nest))
        return aList
    elif isinstance(nodes, str):
        if ' ' in nodes:
            return nodes.split(' ')
        # print(str)
        return nodes
    elif isinstance(nodes, bool):
        return nodes
    elif isinstance(nodes, int):
        return nodes
    elif nodes == []:
        return []
    elif nodes == ():
        return ()
    return output_dict
