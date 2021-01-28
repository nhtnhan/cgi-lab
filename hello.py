#!/usr/bin/env python3
import os
import json

# PRINT ENV VARS AS PLAIN TEXT
# print("Content-Type: text/plain")    # plain text
# print()
# print(os.environ)

# PRINT ENV VARS AS JSON 
# print("Content-Type: application/json")    # json is following
# print()
# print(json.dumps(dict(os.environ), indent = 2))

# PRINT QUERY PARAMETER DATA IN HTML
print("Content-Type: text/html")    # HTML is following
print()
print("QUERY_STRING: ",os.getenv("QUERY_STRING"))
print("HTTP_USER_AGENT: ",os.getenv("HTTP_USER_AGENT"))
