class BoolNode:

    def __init__(self,token):
        self.token = token
        self.position = token.position
    def __repr__(self):
        return f'{self.token}'

class NumberNode:

    def __init__(self,token):
        self.token = token
        self.position = token.position
    def __repr__(self):
        return f'{self.token}'

class StringNode:

    def __init__(self,token):
        self.token = token
        self.position = token.position
    def __repr__(self):
        return f'{self.token}'
  
class ListNode:

    def __init__(self,elementNodes, position):
        self.elementNodes = elementNodes
        self.position = position
     
class BinaryOperationNode:

    def __init__(self,leftNode,operationToken,rightNode):
        self.leftNode = leftNode
        self.operationToken = operationToken
        self.rightNode = rightNode
        self.position = leftNode.position

    def __repr__(self):
        return f'({self.leftNode},{self.operationToken},{self.rightNode})'


class UnaryOperationNode:
    def __init__(self,operationToken,rightNode):
        self.operationToken = operationToken
        self.rightNode = rightNode
        self.position = operationToken.position

    def __repr__(self):
        return f'({self.operationToken},{self.rightNode})'


class VarAccessNode:
    
    def __init__(self,varToken):
        self.varToken = varToken
        self.position = varToken.position

class VarAssignNode: 

    def __init__(self,varToken,expressionNode):
        self.varToken = varToken
        self.expressionNode = expressionNode
        self.position = varToken.position


class IfNode:

    def __init__(self,baseCase,elseCase):
        self.baseCase = baseCase
        self.elseCase = elseCase
        self.position = baseCase[0].position

class ForNode:

    def __init__(self,varName,startValueNode,endValueNode,stepValueNode ,bodyNode):
        self.varName = varName
        self.startValueNode = startValueNode
        self.endValueNode = endValueNode
        self.stepValueNode = stepValueNode
        self.bodyNode = bodyNode

        self.position = varName.position

class WhileNode:

    def __init__(self,conditionNode,bodyNode):
        self.conditionNode = conditionNode
        self.bodyNode = bodyNode
        self.position = conditionNode.position
      
class PrintNode:
    
    def __init__(self,bodyNode):
        self.bodyNode = bodyNode
        self.position = bodyNode.position

class SumNode:

    def __init__(self,listNode):
        self.listNode = listNode
        self.position = listNode.position

class StringifyNode:
    def __init__(self,bodyNode):
        self.bodyNode = bodyNode
        self.position = bodyNode.position

