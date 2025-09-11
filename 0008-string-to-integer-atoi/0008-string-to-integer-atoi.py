class Solution:
    def myAtoi(self, s: str) -> int:
        # Handle empty string
        if not s:
            return 0
      
        n = len(s)
        index = 0
      
        # Skip leading whitespaces
        while index < n and s[index] == ' ':
            index += 1
      
        # Check if string contains only whitespaces
        if index == n:
            return 0
      
        # Determine sign of the number
        sign = -1 if s[index] == '-' else 1
      
        # Move past sign character if present
        if s[index] in ['-', '+']:
            index += 1
      
        # Initialize result and overflow threshold
        result = 0
        # Maximum value that result can be before multiplying by 10
        # (2^31 - 1) // 10 = 214748364
        overflow_threshold = (2**31 - 1) // 10
      
        # Process digits
        while index < n:
            # Stop if current character is not a digit
            if not s[index].isdigit():
                break
          
            current_digit = int(s[index])
          
            # Check for overflow before updating result
            # If result > overflow_threshold, multiplying by 10 will overflow
            # If result == overflow_threshold and current_digit > 7, 
            # then result * 10 + current_digit > 2^31 - 1 (2147483647)
            if result > overflow_threshold or (result == overflow_threshold and current_digit > 7):
                # Return INT_MAX or INT_MIN based on sign
                return 2**31 - 1 if sign > 0 else -(2**31)
          
            # Update result
            result = result * 10 + current_digit
            index += 1
      
        # Apply sign and return final result
        return sign * result