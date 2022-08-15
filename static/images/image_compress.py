from pathlib import Path
import os
legal_suffix_list = [".jpg", ".jpeg", ".JPG", ".JPEG"]
current_path = Path.cwd()
file_paths= [subp for subp in current_path.rglob('*') if subp.suffix in legal_suffix_list]
file_paths.sort()

output_path =  current_path / "processed"
print(output_path)
output_path.mkdir(parents=True, exist_ok=True)


for file_p in file_paths:
    input = str(file_p)
    output = str(  output_path / file_p.name  ) 
    command = f"ffmpeg -i {input} -q:v 10 {output}"
    os.system(command)