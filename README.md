# SecurityHeadersCheck
This simple script helps to figure out implemented and Not implement server side security headers.

# Help
```python3
"""
Security Headers check v1.0  *-* created by mehran-seiflainia *-*
[Usage]: SecurityHeadersCheck.py              # Run the script normally
         SecurityHeadersCheck --cors          # Run the script with an 'Origin' header in requests.
         SecurityHeadersCheck --cors DOMAIN   # Run the script with an custom 'Origin' header.
"""
```

# Change Log:
* v 1.0.0:
  * Release
* v 1.1.0:
  * Fix pip modules installation
* v 1.5.2:
  * Fix 302 redirection problem
  * Fix HTTPSConnectionPool error
  * Edit display to better view
  * Change "link" variables to dictionary
* v 2.0.0:
  * Add "How to fix" web view
* v 2.0.1:
  * Fix https timeout error
