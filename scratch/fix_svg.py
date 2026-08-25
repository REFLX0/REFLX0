import os

path = r"c:\Users\Asus\OneDrive\Bureau\REFLX0\my-profile\assets\portrait.svg"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Check if already injected
if "<style>" not in content[:500]:
    injection = """<style>
  @media (prefers-color-scheme: light) {
    .bg { fill: #0d1117; }
  }
  @media (prefers-color-scheme: dark) {
    .bg { fill: transparent; }
  }
</style>
<rect class="bg" width="100%" height="100%" rx="3%"/>
"""

    # find where to inject: right after `<svg ...>` closing bracket, usually `><g `
    idx = content.find("><g ")
    if idx != -1:
        new_content = content[:idx+1] + injection + content[idx+1:]
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Successfully injected background into portrait.svg")
    else:
        print("Could not find insertion point")
else:
    print("Already injected")
