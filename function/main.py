import os

def handler(event, ctx):
    name = os.environ.get("NAME", "Dimi")  
    return {
        "message": f"Hello {name}!"
    }