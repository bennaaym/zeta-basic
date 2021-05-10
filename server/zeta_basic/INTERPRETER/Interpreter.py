from zeta_basic.LEXER.constants import *
from zeta_basic.DATATYPES.Bool import Bool
from zeta_basic.DATATYPES.Number import Number
from zeta_basic.DATATYPES.String import String
from zeta_basic.DATATYPES.List import List
from .RunTimeResult import RunTimeResult
from zeta_basic.ERRORS.Error import RunTimeError

class Interpreter:

    def visit(self,node,context):
        method = getattr(self, f'visit{type(node).__name__}',self.noVisitMethod)
        return method(node,context)

    def noVisitMethod(self,node,context):
        raise Exception(f'no visit{type(node).__name__} defined')

    def visitBoolNode(self,node,context):
        res = RunTimeResult()      
        return res.success(Bool(node.token.value,node.position,context))

    def visitNumberNode(self,node,context):  
        res = RunTimeResult()      
        return res.success(Number(node.token.value,node.position,context))

    def visitStringNode(self,node,context):
        res = RunTimeResult()      
        return res.success(String(node.token.value,node.position,context))

    def visitBinaryOperationNode(self,node,context):

        res = RunTimeResult()
        leftNode = res.register(self.visit(node.leftNode,context))
        if res.error : return res
        rightNode = res.register(self.visit(node.rightNode,context))
        if res.error : return res


        if node.operationToken.type == TT_PLUS:
            result,error = leftNode + rightNode

        elif node.operationToken.type == TT_MINUS:
            result,error = leftNode - rightNode

        elif node.operationToken.type == TT_MULT:
            result,error = leftNode * rightNode

        elif node.operationToken.type == TT_DIV:
            result,error = leftNode / rightNode
        
        elif node.operationToken.type == TT_POW:
            result,error = leftNode**rightNode

        elif node.operationToken.type == TT_MOD:
            result,error = leftNode % rightNode

        elif node.operationToken.type == TT_FLOORDIV:
            result,error = leftNode // rightNode

        elif node.operationToken.type == TT_EE:
            result,error = leftNode == rightNode

        elif node.operationToken.type == TT_NE:
            result,error = leftNode != rightNode

        elif node.operationToken.type == TT_GE:
            result,error = leftNode >= rightNode

        elif node.operationToken.type == TT_LE:
            result,error = leftNode <= rightNode
        
        elif node.operationToken.type == TT_GT:
            result,error = leftNode > rightNode

        elif node.operationToken.type == TT_LT:
            result,error = leftNode < rightNode

        elif node.operationToken.type == TT_AND:
            result,error = leftNode._and(rightNode)

        elif node.operationToken.type == TT_OR:
            result,error = leftNode._or(rightNode)


        if error : return res.failure(error)

        else : 
            if node.operationToken.type in (TT_PLUS,TT_MINUS,TT_MULT,TT_DIV,TT_FLOORDIV,TT_MOD,TT_POW):
                operandType = type(leftNode).__name__
                if operandType == 'String':
                    return res.success(String(result.value,node.position,context))
                else:
                    return res.success(Number(result.value,node.position,context))

            else:
                return res.success(Bool(result.value,node.position,context))



    def visitUnaryOperationNode(self,node,context):
        res = RunTimeResult()

        rightNode = res.register(self.visit(node.rightNode,context))

        if res.error : return res

        if node.operationToken.type == TT_MINUS:
            rightNode,error = rightNode * Number(-1,node.position,context)
        elif node.operationToken.type == TT_NOT:
            rightNode ,error = rightNode._not() 
        else:
            error = None

        if error : return res.failure(error)

        else : return res.success(Number(rightNode.value,node.position,context))

    
    def visitVarAccessNode(self,node,context):
        res = RunTimeResult()
        varName = node.varToken.value
        value = context.symbolTable.get(varName)

        try:
            if value.value == None :
                 return res.failure(RunTimeError(f'undefined variable : {varName}',node.position,context))
        except: 
             return res.failure(RunTimeError(f'undefined variable : {varName} ',node.position,context))
        
        valueType = type(value).__name__

        if(valueType == 'Number'):
            value = Number(value.value,node.position,context)
        elif(valueType == 'String'):
            value = String(value.value,node.position,context)
        elif(valueType == 'List'):
            value = List(value.value,node.position,context)
        elif(valueType == 'Bool'):
            value = Bool(value.value,node.position,context)
    

        return res.success(value) 


    def visitVarAssignNode(self,node,context):
        res = RunTimeResult()
        varName = node.varToken.value
        value = res.register(self.visit(node.expressionNode, context))
        if res.error : return res

        context.symbolTable.set(varName,value)

        return res.success(value)

    def visitIfNode(self,node,context):
        res = RunTimeResult()

        cond,expr = node.baseCase

        condValue = res.register(self.visit(cond, context))
        if res.error : return res

        if condValue.isTrue():
            exprValue = res.register(self.visit(expr, context))
            if res.error : return res
            return res.success(exprValue)

        if node.elseCase:
            elseValue = res.register(self.visit(node.elseCase, context))
            if res.error: return res
            return res.success(elseValue)

        return res.success(Number.null)

    def visitForNode(self,node,context):
        res = RunTimeResult()
        elements = []


        startValue = res.register(self.visit(node.startValueNode, context))
        if res.error : return res

        endValue = res.register(self.visit(node.endValueNode, context))
        if res.error : return res

        if node.stepValueNode : 
            stepValue = res.register(self.visit(node.stepValueNode, context))
            if res.error : return res
        else:
            stepValue = Number(1,node.position,context)

        i = startValue.value

        if stepValue.value >=0 :
            condition = lambda : i < endValue.value
        else:
            condition = lambda : i > endValue.value

        while condition():

            context.symbolTable.set(node.varName.value,Number(i,node.position,context))
            i += stepValue.value

            elements.append(res.register(self.visit(node.bodyNode, context)))
            if res.error : return res

       
        return res.success(List(elements, node.position, context))

    def visitWhileNode(self,node,context):
        res = RunTimeResult()
        elements = []
        while True:

            condition = res.register(self.visit(node.conditionNode, context))
            if  res.error : return res

            if not condition.isTrue(): break

            elements.append(res.register(self.visit(node.bodyNode, context)))
            if res.error : return res

     

        return res.success(List(elements, node.position, context))


    def visitPrintNode(self,node,context):
        res = RunTimeResult()

        bodyValue = res.register(self.visit(node.bodyNode, context))
        if res.error : return res
        return res.success(bodyValue)

    def visitStringifyNode(self,node,context):
        res = RunTimeResult()
        bodyValue = res.register(self.visit(node.bodyNode, context))
        if res.error : return res
        return res.success(String(bodyValue.toString(),node.position,context))


    def visitSumNode(self,node,context):
        res = RunTimeResult()

        listNode = res.register(self.visit(node.listNode, context))
        if res.error : return res

        if(type(listNode).__name__ == 'List'):
            listValue,error = listNode.sum()
        else:
            return res.failure(RunTimeError('expected a list datatype for function SUM', node.position, context))

        if error : return res.failure(error)
        return res.success(listValue)

    def visitListNode(self,node,context):
        res = RunTimeResult()
        elements = []

        for elementNode in node.elementNodes:
            elements.append(res.register(self.visit(elementNode, context)))
            if res.error : return res

        return res.success(List(elements,node.position,context))