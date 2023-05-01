
instructions= []
instr = "SW    s1 ,0( s2 )"
sp = instr.split(" ")
print(sp[0])
ins = sp[0].upper()
print(ins)
#instructions.append({"Counter": 4, "word" : "ADD", "operands":["s1","s2","s3"], "type" :"R"})
#print(instructions)
if(ins == "LUI"):
    one = instr.replace(" ","")
    en = 3
    rd= ""
    for i in range(3, len(one)):
        if(one[i] != ','):
            rd = rd + one[i]
            en+=1
        else:
            break
    print(rd)
    immediate = ""
    for i in range(en+1, len(one)):
        immediate += one[i]
    print(immediate) 
    instructions.append({"Counter":0,"word":"LUI", "operands" : [rd, immediate], "type":"U"} )
elif(ins =="AUIPC"):
    one = instr.replace(" ","")
    en = 5
    rd= ""
    for i in range(5, len(one)):
        if(one[i] != ','):
            rd = rd + one[i]
            en+=1
        else:
            break
    print(rd)
    immediate = ""
    for i in range(en+1, len(one)):
        immediate += one[i]
    print(immediate) 
    instructions.append({"Counter":0,"word":"AUIPC", "operands" : [rd, immediate], "type":"U"} )
elif(ins == "JAL"):
    one = instr.replace(" ","")
    en = 3
    rd= ""
    for i in range(3, len(one)):
        if(one[i] != ','):
            rd = rd + one[i]
            en+=1
        else:
            break
    print(rd)
    immediate = ""
    for i in range(en+1, len(one)):
        immediate += one[i]
    print(immediate) 
    instructions.append({"Counter":0,"word":"JAL", "operands" : [rd, immediate], "type":"J"} )
elif(ins =="BEQ"):
    one = instr.replace(" ","")
    en = 3
    rs1= ""
    for i in range(3, len(one)):
        if(one[i] != ','):
            rs1 = rs1 + one[i]
            en+=1
        else:
            break
    print(rs1)
    rs2 = ""
    en2 = en+1
    for i in range(en+1, len(one)):
        if(one[i] != ','):
            rs2 = rs2 + one[i]
            en2+=1
        else:
            break
    label = ""
    for i in range(en2+1, len(one)):
        label = label + one[i]
          
    instructions.append({"Counter":0,"word":"BEQ", "operands" : [rs1,rs2, label], "type":"SB"} )
elif(ins == "BNE"):
    one = instr.replace(" ","")
    en = 3
    rs1= ""
    for i in range(3, len(one)):
        if(one[i] != ','):
            rs1 = rs1 + one[i]
            en+=1
        else:
            break
    print(rs1)
    rs2 = ""
    en2 = en+1
    for i in range(en+1, len(one)):
        if(one[i] != ','):
            rs2 = rs2 + one[i]
            en2+=1
        else:
            break
    label = ""
    for i in range(en2+1, len(one)):
        label = label + one[i]
          
    instructions.append({"Counter":0,"word":"BNE", "operands" : [rs1,rs2, label], "type":"SB"} )
elif(ins =="BLT"):
    one = instr.replace(" ","")
    en = 3
    rs1= ""
    for i in range(3, len(one)):
        if(one[i] != ','):
            rs1 = rs1 + one[i]
            en+=1
        else:
            break
    print(rs1)
    rs2 = ""
    en2 = en+1
    for i in range(en+1, len(one)):
        if(one[i] != ','):
            rs2 = rs2 + one[i]
            en2+=1
        else:
            break
    label = ""
    for i in range(en2+1, len(one)):
        label = label + one[i]
          
    instructions.append({"Counter":0,"word":"BLT", "operands" : [rs1,rs2, label], "type":"SB"} )
elif(ins =="BGE"):
    one = instr.replace(" ","")
    en = 3
    rs1= ""
    for i in range(3, len(one)):
        if(one[i] != ','):
            rs1 = rs1 + one[i]
            en+=1
        else:
            break
    print(rs1)
    rs2 = ""
    en2 = en+1
    for i in range(en+1, len(one)):
        if(one[i] != ','):
            rs2 = rs2 + one[i]
            en2+=1
        else:
            break
    label = ""
    for i in range(en2+1, len(one)):
        label = label + one[i]
          
    instructions.append({"Counter":0,"word":"BGE", "operands" : [rs1,rs2, label], "type":"SB"} )
elif(ins =="BLTU"):
    one = instr.replace(" ","")
    en = 4
    rs1= ""
    for i in range(4, len(one)):
        if(one[i] != ','):
            rs1 = rs1 + one[i]
            en+=1
        else:
            break
    print(rs1)
    rs2 = ""
    en2 = en+1
    for i in range(en+1, len(one)):
        if(one[i] != ','):
            rs2 = rs2 + one[i]
            en2+=1
        else:
            break
    label = ""
    for i in range(en2+1, len(one)):
        label = label + one[i]
          
    instructions.append({"Counter":0,"word":"BLTU", "operands" : [rs1,rs2, label], "type":"SB"} )
elif(ins =="BGEU"):
    one = instr.replace(" ","")
    en = 4
    rs1= ""
    for i in range(4, len(one)):
        if(one[i] != ','):
            rs1 = rs1 + one[i]
            en+=1
        else:
            break
    print(rs1)
    rs2 = ""
    en2 = en+1
    for i in range(en+1, len(one)):
        if(one[i] != ','):
            rs2 = rs2 + one[i]
            en2+=1
        else:
            break
    label = ""
    for i in range(en2+1, len(one)):
        label = label + one[i]
          
    instructions.append({"Counter":0,"word":"BGEU", "operands" : [rs1,rs2, label], "type":"SB"} )
elif(ins == "SB"):
    one = instr.replace(" ","")
    en = 2
    rs1= ""
    for i in range(2, len(one)):
        if(one[i] != ','):
            rs1 = rs1 + one[i]
            en+=1
        else:
            break
    print(rs1)
    offset = ""
    en2 = en+1
    for i in range(en+1, len(one)):
        if(one[i] != '('):
            offset = offset + one[i]
            en2+=1
        else:
            break
    rs2 = ""
    for i in range(en2+1, len(one)-1):
        rs2 = rs2 + one[i]
          
    instructions.append({"Counter":0,"word":"SH", "operands" : [rs1,offset, rs2], "type":"S"} )
elif(ins == "SH"):
    one = instr.replace(" ","")
    en = 2
    rs1= ""
    for i in range(2, len(one)):
        if(one[i] != ','):
            rs1 = rs1 + one[i]
            en+=1
        else:
            break
    print(rs1)
    offset = ""
    en2 = en+1
    for i in range(en+1, len(one)):
        if(one[i] != '('):
            offset = offset + one[i]
            en2+=1
        else:
            break
    rs2 = ""
    for i in range(en2+1, len(one)-1):
        rs2 = rs2 + one[i]
          
    instructions.append({"Counter":0,"word":"SH", "operands" : [rs1,offset, rs2], "type":"S"} )
elif(ins == "SW"):
    one = instr.replace(" ","")
    en = 2
    rs1= ""
    for i in range(2, len(one)):
        if(one[i] != ','):
            rs1 = rs1 + one[i]
            en+=1
        else:
            break
    print(rs1)
    offset = ""
    en2 = en+1
    for i in range(en+1, len(one)):
        if(one[i] != '('):
            offset = offset + one[i]
            en2+=1
        else:
            break
    rs2 = ""
    for i in range(en2+1, len(one)-1):
        rs2 = rs2 + one[i]
          
    instructions.append({"Counter":0,"word":"SW", "operands" : [rs1,offset, rs2], "type":"S"} )
print(instructions)
        