$ find /IXS* -xdev -type f '(' -name "*.py" -o -name "*.sh" ')' | xargs -r grep -i 'xf10id-ca1\|10\.10\.0\.4'

# was looking for: /IXS2/wwatson/Documents/extractData/archAppl.py
