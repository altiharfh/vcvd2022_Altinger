import os
import re
import subprocess

#===================
def toBatchEcho(txt, path_out):
    return 'echo ' + txt + ' >> ' + path_out + '\n'

student_id_re = "s\d{10}"
report_file_path = "ws20232024_out.txt"
report_file_path_err = "ws20232024_out_err.txt"
batch_file_path = 'out.bat'

files = [report_file_path, report_file_path_err, batch_file_path]
for cur_file in files:
    if os.path.exists(cur_file):
        os.remove(cur_file)


pyling_cfg_path = "\"C:\\Users\\altihar\\OneDrive - FH OOe\\VCVD\\VCVD_WS2023\\vcvd2022_Altinger\\code_guideline\\googlePyLintSettings.cfg\""
pylint_cmd = "python -m pylint --rcfile " + pyling_cfg_path
#pylint_cmd = ['C:\\windows\\system32\\cmd.exe', '/C', "c:\\proglang\\runtime\\python\\3.11.6\\python.exe" ,"-m pylint", "--rcfile " + pyling_cfg_path]


start_path = './'
dir_in_root = [f for f in os.listdir(start_path) if os.path.isdir(os.path.join(start_path, f))]
dir_in_root.append(start_path)

with open(batch_file_path,'w') as report_file:
    for cur_dir in dir_in_root:
        student_id = None
        
        if cur_dir != start_path:
            student_id = re.findall(student_id_re, cur_dir.lower())
            if len(student_id) > 0:
                student_id = student_id[0]
            else:
                student_id = None
            cur_dir = os.path.join(start_path,cur_dir)
        else:
            cur_dir = start_path
            
        files_in_root = [ f for f in os.listdir(cur_dir) if os.path.isfile(os.path.join(cur_dir, f)) ]
        for cur_file in files_in_root:
            if student_id == None:
                student_id = re.findall(student_id_re, cur_file)
            if len(student_id) > 0:
                if not isinstance(student_id, str):
                    student_id = student_id[0]
                file_parts = cur_file.split('.')
                if len(file_parts) > 1:
                    if file_parts[1] == 'py':
                        
                        pylint_cmd_cur = pylint_cmd + " " + "\"" + os.path.abspath(os.path.join(cur_dir,cur_file)) + "\""
                        #pylint_cmd_cur = pylint_cmd
                        #pylint_cmd_cur.append(cur_file)
                        #print (pylint_cmd_cur)
                        
                        #output = subprocess.check_output(pylint_cmd_cur, universal_newlines=True)
                        #output = subprocess.run(pylint_cmd_cur, stdout=subprocess.PIPE)
                        #return_code = os.popen(pylint_cmd_cur)
                        
                        report_file.write(toBatchEcho("=======================",report_file_path))
                        report_file.write(toBatchEcho(student_id,report_file_path))
                        report_file.write(toBatchEcho(cur_file,report_file_path))
                        report_file.write(toBatchEcho("=======================",report_file_path_err))
                        report_file.write(toBatchEcho(student_id,report_file_path_err))
                        report_file.write(toBatchEcho(cur_file,report_file_path_err))                        
                        report_file.write('call ' + pylint_cmd_cur + ' >> ' + report_file_path + ' 2>> ' + report_file_path_err +'\n')
            else:
                student_id = None            
#os.system(batch_file_path)                        