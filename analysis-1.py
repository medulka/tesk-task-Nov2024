#!/usr/bin/env python3

import json

# with open(file="/Users/hanamedova/Documents/Gaia-X/building-blocks/test-task/i4Trust-OIDC.json") as f:
#     data = json.load(f)
    
# with open(file="/Users/hanamedova/Documents/Gaia-X/building-blocks/test-task/GX-swagger-example.json") as f:
#     data = json.load(f)

with open(file="/Users/hanamedova/Documents/Gaia-X/building-blocks/test-task/i4Trust-DID.json") as f:
    data = json.load(f)    

for i in data:
    if i in ['iss', 'issuer']:
        if data[i].startswith("EU.EORI"):
            print("An OIDC identifier. The participant ID cannot be recognised. Please provide DID credentials.")
    if i == "jti":
        print("signed by JSON Web Token")
    if i == "data":
        if data["data"]["issuer"].startswith("did:web"):
            print("DID identifier found.")    
        print(data["data"]["type"][0]) 
        if print(data["data"]["proof"]["type"]).startswith("JsonWebSignature"):
            print("JSON Web Signature used.")
    if i == "payload":
        if data["payload"]["id"].startswith("did:elsi"):
            print("DID identifier found.") 
        if data["payload"]["verificationMethod"][0]["type"].startswith("JsonWebKey"):
            print("JSON Web Key used.") 
    else: 
        pass

print("Check of standards  done. Parsing finished.")





