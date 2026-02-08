def infix_to_postfix(expression):
    """
    Convert an infix expression to postfix notation.
    
    Args:
        expression: String containing the infix expression
        
    Returns:
        String containing the postfix expression
    """
    # Define operator precedence (higher value = higher precedence)
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    
    # Stack for operators and output list for result
    stack = []
    postfix = []
    
    # Tokenize the expression (handle multi-character operands and spaces)
    tokens = tokenize(expression)
    
    for token in tokens:
        # If token is an operand (number or variable)
        if is_operand(token):
            postfix.append(token)
        
        # If token is a left parenthesis
        elif token == '(':
            stack.append(token)
        
        # If token is a right parenthesis
        elif token == ')':
            # Pop operators until matching left parenthesis
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            # Remove the left parenthesis
            if stack:
                stack.pop()
        
        # If token is an operator
        elif token in precedence:
            # Pop operators with higher or equal precedence
            while (stack and stack[-1] != '(' and 
                   stack[-1] in precedence and
                   precedence[stack[-1]] >= precedence[token]):
                postfix.append(stack.pop())
            # Push current operator to stack
            stack.append(token)
    
    # Pop remaining operators from stack
    while stack:
        postfix.append(stack.pop())
    
    return ' '.join(postfix)


def tokenize(expression):
    """
    Tokenize the expression into operands and operators.
    
    Args:
        expression: String containing the infix expression
        
    Returns:
        List of tokens
    """
    tokens = []
    current_token = ''
    
    for char in expression:
        if char.isspace():
            if current_token:
                tokens.append(current_token)
                current_token = ''
        elif char in '+-*/()':
            if current_token:
                tokens.append(current_token)
                current_token = ''
            tokens.append(char)
        else:
            current_token += char
    
    if current_token:
        tokens.append(current_token)
    
    return tokens


def is_operand(token):
    """
    Check if a token is an operand (number or variable).
    
    Args:
        token: String token to check
        
    Returns:
        Boolean indicating if token is an operand
    """
    if not token:
        return False
    
    # Check if it's a number (integer or float)
    try:
        float(token)
        return True
    except ValueError:
        # Check if it's a variable (alphanumeric identifier)
        return token.isalnum()


def main():
    """Main function to read input and display postfix conversion."""
    print("Infix to Postfix Converter")
    print("=" * 40)
    
    while True:
        infix_expr = input("\nEnter an infix expression (or 'quit' to exit): ").strip()
        
        if infix_expr.lower() == 'quit':
            print("Goodbye!")
            break
        
        if not infix_expr:
            print("Please enter a valid expression.")
            continue
        
        try:
            postfix_expr = infix_to_postfix(infix_expr)
            print(f"Infix:   {infix_expr}")
            print(f"Postfix: {postfix_expr}")
        except Exception as e:
            print(f"Error: {e}")
            print("Please check your expression syntax.")


if __name__ == "__main__":
    main()
