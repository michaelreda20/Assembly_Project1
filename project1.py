instructions= []
instr = "srA s1, s2, s3"
sp = instr.split(" ")
#print(ins)
ins = sp[0].upper()
#print(ins)
#instructions.append({"Counter": 4, "word" : "ADD", "operands":["s1","s2","s3"], "type" :"R"})
#print(instructions)

rd = sp[1][0:2]
rs2 = sp[2][0:2]
rs1 = sp[3][0:2]
print(rd)  
print(rs2)  
print(rs1)   

print(ins)


if ins == "ADD" or ins == "OR" or ins == "AND" or ins == "SUB" or ins == "SLL" or ins == "SLT" or ins == "SLTU" or ins == "XOR" or ins == "SRL" or ins == "SRA":
    print("This is R-Type Format")
    print("Its opcode is 0110011")
    

    if ins == "ADD":
        print("func3 = 000, func7 = 0000000")
        #print(rs1+rs2)
        rd= rs2+rs1
        instructions.append({"Counter": 0, "word" : "ADD", "operands":[rd,rs2,rs1], "type" :"R"})


    elif ins == "OR":
        print("func3 = 110, func7 = 0000000")
        rd= rs1 or rs2
        instructions.append({"Counter": 0, "word" : "OR", "operands":[rd,rs2,rs1], "type" :"R"})

    elif ins == "AND":
        print("func3 = 111, func7 = 0000000")
        rd= rs1 and rs2
        instructions.append({"Counter": 0, "word" : "AND", "operands":[rd,rs2,rs1], "type" :"R"})

    elif ins == "SUB":
        print("func3 = 000, func7 = 0100000")
        rd= rs2-rs1
        instructions.append({"Counter": 0, "word" : "SUB", "operands":[rd,rs2,rs1], "type" :"R"})

    elif ins == "SLL":
        print("func3 = 001, func7 = 0000000")

        instructions.append({"Counter": 0, "word" : "ADD", "operands":[rd,rs2,rs1], "type" :"R"})

    elif ins == "SLT":
        print("func3 = 010, func7 = 0000000")
        if rs2<rs1:
            rd=1
        else: 
            rd=0
        instructions.append({"Counter": 0, "word" : "SLT", "operands":[rd,rs2,rs1], "type" :"R"})

    elif ins == "SLTU":
        print("func3 = 011, func7 = 0000000")
        if rs2<rs1:
            rd=1
        else: 
            rd=0
        instructions.append({"Counter": 0, "word" : "SLTU", "operands":[rd,rs2,rs1], "type" :"R"})

    elif ins == "XOR":
        print("func3 = 100, func7 = 0000000")
        rd = rs2^rs1
        instructions.append({"Counter": 0, "word" : "XOR", "operands":[rd,rs2,rs1], "type" :"R"})

    elif ins == "SRL":
        print("func3 = 101, func7 = 0000000")
        instructions.append({"Counter": 0, "word" : "SRL", "operands":[rd,rs2,rs1], "type" :"R"})

    elif ins == "SRA":
        print("func3 = 101, func7 = 0100000")
        instructions.append({"Counter": 0, "word" : "SRA", "operands":[rd,rs2,rs1], "type" :"R"})


print(instructions)