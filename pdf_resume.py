import json
import os
from fpdf import FPDF

directory = os.getcwd()
print(directory)
jsonFile = "%s/%s" % (directory, "resume_information.json")
json_data = {}


# Load in json file
with open(jsonFile) as json_file:
    json_data = json.load(json_file)

# Layout Format
pdf = FPDF('P','mm','A4')
pdf.add_page()

# Set json datas
# Personal information
first_name = json_data["First Name"]
last_name = json_data["Last Name"]
address = json_data["Address"]
# objective data
objective1 = json_data["Objective1"]
objective2 = json_data["Objective2"]
# other personal information
age = json_data["Age"]
sex = json_data["Sex"]
civil_status = json_data["Civil Status"]
citizenship = json_data["Citizenship"]
# contact information
contact_number = json_data["Contact Number"]
emailAdd = json_data["Email"]
github_info = json_data["Github"]
# Skills
firstSkill = json_data["Skills"][0]
secondSkill = json_data["Skills"][1]
# Hobbies
myHobby = json_data["Hobbies"][0]
# Education
primaryEduc = json_data["Primary Education"]
secondaryEduc = json_data["Secondary Education"]
tertiaryEduc = json_data["Tertiary Education"]


# Arranging the information of the resume
pdf.set_font("times", "B", 45)
pdf.set_text_color(0,0,0,)
pdf.cell(0,15, "     " + first_name + " " + last_name, ln =1, align="C")
pdf.set_font('times','I',15)
pdf.set_text_color(0,0,0,)
pdf.cell(0,6,"      " + address, align="C", ln=1)
pdf.cell(0,5,"      " + "Cell:" + contact_number + "  ---  " + "Email:" + emailAdd + "  ---  " + "Github:" + github_info,align="C",ln=1)

        # Arrange Objective
pdf.set_font("times","B", 20)
pdf.set_text_color(0,0,0)
pdf.set_fill_color(239,154,154)
pdf.ln(10)
pdf.cell(0,7," " + "Objective",align="L",ln=1,fill="1")
pdf.set_font("times","", 16)
pdf.set_text_color(0,0,0,)
pdf.cell(0,8, objective1, align="L",ln=1)
pdf.cell(0,5, objective2, align="L",ln=1)

        # Arrange personal information
pdf.set_font("times","B", 20)
pdf.set_text_color(0,0,0)
pdf.set_fill_color(239,154,154)
pdf.ln(10)
pdf.cell(0,7,"Personal Information:",align= "L", ln=1, fill="1")
pdf.set_font("times", "", 16)
pdf.cell(0,8, "Age: " +str(age) + "                              " + "Sex:" + sex, align="L", ln=1)
pdf.ln(5)
pdf.cell(0,8,"Civil Status:" + civil_status + "            " + "Citizenship:" + citizenship, align="L",ln=4)

        # Arrange Skills
pdf.set_font("times","B", 20)
pdf.set_text_color(0,0,0)
pdf.set_fill_color(239,154,154)
pdf.ln(10)
pdf.cell(0,7,"Skills:",align= "L",ln=1,fill="1")
pdf.set_font("times", "", 16)
pdf.cell(0,8,firstSkill, align="L", ln=1)
pdf.ln(5)
pdf.cell(0,8,secondSkill, align="L", ln=4)
        # Arrange Hobbies
pdf.set_font("times","B", 20)
pdf.set_text_color(0,0,0)
pdf.set_fill_color(239,154,154)
pdf.ln(10)
pdf.cell(0,7,"Hobbies:",align= "L",ln=1,fill="1")
pdf.set_font("times", "", 16)
pdf.cell(0,8, myHobby, align="L", ln=1)   

        # Arrange Educational Attainment
pdf.set_font("times","B", 20)
pdf.set_text_color(0,0,0)
pdf.set_fill_color(239,154,154)
pdf.ln(10)
pdf.cell(0,7,"Educational Attainment:",align="L",ln=1,fill="1")
pdf.set_font("times","", 16)
pdf.cell(0,8, "Primary Education:" + "  " + primaryEduc, align="L",ln=1)
pdf.ln(5)
pdf.cell(0,8, "Secondary Education:" + "  " + secondaryEduc, align="L",ln=1)
pdf.ln(5)
pdf.cell(0,8, "Tertiary Education:" + "  " + tertiaryEduc, align="L", ln=1)
    

# Make the pdf
pdf.output('Tabaquero,Cath.pdf')