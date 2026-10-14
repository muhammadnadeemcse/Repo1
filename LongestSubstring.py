{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ac4e494a",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "class Solution:\n",
    "    def longestPalindrome(self, s: str) -> str:\n",
    "        res = \"\"\n",
    "        resLen = 0\n",
    "\n",
    "        for i in range(len(s)):\n",
    "            # Odd-length palindrome\n",
    "            l, r = i, i\n",
    "            while l >= 0 and r < len(s) and s[l] == s[r]:\n",
    "                if (r - l + 1) > resLen:\n",
    "                    res = s[l:r + 1]\n",
    "                    resLen = r - l + 1\n",
    "                l -= 1\n",
    "                r += 1\n",
    "\n",
    "            # Even-length palindrome\n",
    "            l, r = i, i + 1\n",
    "            while l >= 0 and r < len(s) and s[l] == s[r]:\n",
    "                if (r - l + 1) > resLen:\n",
    "                    res = s[l:r + 1]\n",
    "                    resLen = r - l + 1\n",
    "                l -= 1\n",
    "                r += 1\n",
    "\n",
    "        return res\n",
    "\n",
    "\n",
    "# Example usage\n",
    "obj = Solution()\n",
    "\n",
    "s = input(\"Enter a string: \")\n",
    "print(\"Longest palindromic substring:\", obj.longestPalindrome(s))\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
