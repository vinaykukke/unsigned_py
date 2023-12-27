import os

def get():
    tools = []
    tools_dir = os.listdir(os.environ.get("UNSIGNED_VEX_PATH"))
    tools_dir.sort()
    
    for t in tools_dir:
        tool_name = ' '.join(word.capitalize() for word in t.split('_'))
        tools.append(t)
        tools.append(tool_name)

    return tools
