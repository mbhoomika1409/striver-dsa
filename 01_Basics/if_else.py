"""
Problem: If Else
Platform: Striver A2Z DSA Sheet

Given marks of a student, print:
- Grade A if marks >= 90
- Grade B if marks >= 70
- Grade C if marks >= 50
- Grade D if marks >= 35
- Fail otherwise
"""

class Solution:
    def studentGrade(self, marks):
        if marks >= 90:
            print("Grade A")
        elif marks >= 70:
            print("Grade B")
        elif marks >= 50:
            print("Grade C")
        elif marks >= 35:
            print("Grade D")
        else:
            print("Fail")

