def format_names(f_name,l_name):
    if f_name == "" or l_name == "":
        return  "You Did Not Provide Valid Input"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    
    return f"{formated_f_name} {formated_l_name}"

print(format_names(input("What is your first name: "), input("What is yout last name: ")))
#print(format_names("SuNIl","SAiNi"))

def fn_1(text):
    return text + text

def fn_2(text):
    return text.title()

output = fn_1("HeLLO")
print(output)
print(fn_2(output))
 