instructions= []
instr = "SW    s1 ,0( s2 )"
sp = instr.split(" ")
print(sp[0])
ins = sp[0].upper()
print(ins)
#instructions.append({"Counter": 4, "word" : "ADD", "operands":["s1","s2","s3"], "type" :"R"})
#print(instructions)
rd = sp[1][0:2]  # extract destination register name
rs1 = sp[2][0:2]  # extract source register name
immediate = sp[3]  # extract immediate value
def sign_extend(value, num_bits):

    """Sign-extends the given value to a specified number of bits."""
    sign_bit = 1 << (num_bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)
    
#result=sign_extend(2,12)
#print(result)

if(ins=="ADDI"):

    rd=rs1+immediate
    print(rd)
   
    instructions.append({"Counter":0,"word":"ADDI", "operands" : [rd,rs1, immediate], "type":"I"} )
elif(ins=="SLTI"):
    if(rs1<immediate):
        rd="1"
    else:
        rd="0"
    instructions.append({"Counter":0,"word":"SLTI", "operands" : [rd,rs1, immediate], "type":"I"} )
elif(ins=="SLTIU"):
    if(rs1<immediate):
        rd="1"
    else:
        rd="0"
    instructions.append({"Counter":0,"word":"SLTIU", "operands" : [rd,rs1, immediate], "type":"I"} )
elif(ins=="XORI"):
    rd = rs1 ^ immediate
   
    instructions.append({"Counter":0,"word":"XORI", "operands" : [rd,rs1, immediate], "type":"I"} )
elif(ins=="ORI"):
    rd = rs1 | immediate
    instructions.append({"Counter":0,"word":"ORI", "operands" : [rd,rs1, immediate], "type":"I"} )
elif(ins=="ANDI"):
    rd = rs1 & immediate
    instructions.append({"Counter":0,"word":"ANDI", "operands" : [rd,rs1, immediate], "type":"I"} )
elif(ins=="SLLI"):

    rd=rs1 << immediate
    instructions.append({"Counter":0,"word":"SLLI", "operands" : [rd,rs1, immediate], "type":"I"} )
elif(ins=="SRLI"):
    rd=rs1 >> immediate
    instructions.append({"Counter":0,"word":"SRLI", "operands" : [rd,rs1, immediate], "type":"I"} )
elif(ins=="SRAI"):
    rd=rs1 >> immediate
    shift=-1 << (32 - immediate)
    if(rs1<0):
        rd |= shift
    instructions.append({"Counter":0,"word":"SRAI", "operands" : [rd,rs1, immediate], "type":"I"} )
elif(ins=="JALR"):
  
    instructions.append({"Counter":0,"word":"JALR", "operands" : [rd,rs1, immediate], "type":"I"} )
elif(ins=="LB"):
    immediate_value = sign_extend(int(immediate), 12)
    rd=rs1+immediate_value
    instructions.append({"Counter":0,"word":"LB", "operands" : [rd,rs1, immediate], "type":"I"} )
elif(ins=="LH"):
    offest=""
    rd=rs1+offest
    instructions.append({"Counter":0,"word":"LH", "operands" : [rd,offest, rs1], "type":"I"} )
elif(ins=="LW"):
    offest=""
    rd=rs1+offest
    instructions.append({"Counter":0,"word":"LW", "operands" : [rd,offest, rs1], "type":"I"} )
elif(ins=="LBU"):
    offest=""
    rd=rs1+offest
    instructions.append({"Counter":0,"word":"LBU", "operands" : [rd,offest, rs1], "type":"I"} )
elif(ins=="LHU"):
    offest=""
    rd=rs1+offest
    instructions.append({"Counter":0,"word":"LHU", "operands" : [rd,offest, rs1], "type":"I"} )