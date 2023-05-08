import numpy as np
import pandas as pd
Labels = []
Labels_map = {}
instructions= []
intructions_tokens = []
instructions_map = {}
memory = {10000:{}}
pc = 0
registers = {}
RegNames = {}
def read_code_file(path):
    file = open(path, "r")
    lines = file.readlines()
    global pc
    global Labels
    global instructions
    #print(lines)
    #print(len(lines))
    for l in lines:
        #print(l)
        if(l == "\n"):
            continue
        if(':' in l):
            testLine = l.split(":")
            label = testLine[0].replace(" ", "")
            #print(label)
            Labels.append({"Name" : label.lower(),"Address" : pc})
            testLine[1] = testLine[1].replace("\n", "")

            if(len(testLine) > 1 and testLine[1] != '' and testLine[1] != testLine[1][0] * len(testLine[1])):
                starting = 0
                for c in testLine[1]:
                    if(c != " "):
                        break
                    else:
                        starting+=1
                instructions.append({"instruction" : testLine[1][starting:], "Address" :pc})
            else:
                pc-=4
        else:
            starting = 0
            for c in l:
                if (c != " "):
                    break
                else:
                    starting += 1
            instructions.append({"instruction": l[starting:], "Address": pc})
        pc += 4
    for ins in instructions:
        ins["instruction"] = ins["instruction"].replace("\t", "").replace("\n", "")
count_instructions= 0
def instruction_tokenization():
    global count_instructions
    try:
        for inst in instructions:
            instr =  inst["instruction"]
            sp = instr.split(" ", 1)
            ins = sp[0].upper()
            if (ins == "LUI"):
                one = instr.strip()
                en = 3
                rd = ""
                for i in range(3, len(one)):
                    if (one[i] != ','):
                        rd = rd + one[i]
                        en += 1
                    else:
                        break
                print(rd)
                immediate = ""
                for i in range(en + 1, len(one)):
                    immediate += one[i]
                print(immediate)
                intructions_tokens.append({"Counter": inst["Address"], "word": "LUI", "operands": [rd, immediate], "type": "U"})
            elif (ins == "AUIPC"):
                one = instr.strip()
                en = 5
                rd = ""
                for i in range(5, len(one)):
                    if (one[i] != ','):
                        rd = rd + one[i]
                        en += 1
                    else:
                        break
                print(rd)
                immediate = ""
                for i in range(en + 1, len(one)):
                    immediate += one[i]
                print(immediate)
                intructions_tokens.append({"Counter": inst["Address"], "word": "AUIPC", "operands": [rd, immediate], "type": "U"})
            elif (ins == "JAL"):
                one = instr.strip()
                en = 3
                rd = ""
                for i in range(3, len(one)):
                    if (one[i] != ','):
                        rd = rd + one[i]
                        en += 1
                    else:
                        break
                print(rd)
                immediate = ""
                for i in range(en + 1, len(one)):
                    immediate += one[i]
                print(immediate)
                intructions_tokens.append({"Counter":inst["Address"], "word": "JAL", "operands": [rd, immediate], "type": "J"})
            elif (ins == "BEQ"):
                one = instr.strip()
                en = 3
                rs1 = ""
                for i in range(3, len(one)):
                    if (one[i] != ','):
                        rs1 = rs1 + one[i]
                        en += 1
                    else:
                        break
                print(rs1)
                rs2 = ""
                en2 = en + 1
                for i in range(en + 1, len(one)):
                    if (one[i] != ','):
                        rs2 = rs2 + one[i]
                        en2 += 1
                    else:
                        break
                label = ""
                for i in range(en2 + 1, len(one)):
                    label = label + one[i]

                intructions_tokens.append({"Counter": inst["Address"], "word": "BEQ", "operands": [rs1, rs2, label], "type": "SB"})
            elif (ins == "BNE"):
                one = instr.strip()
                en = 3
                rs1 = ""
                for i in range(3, len(one)):
                    if (one[i] != ','):
                        rs1 = rs1 + one[i]
                        en += 1
                    else:
                        break
                print(rs1)
                rs2 = ""
                en2 = en + 1
                for i in range(en + 1, len(one)):
                    if (one[i] != ','):
                        rs2 = rs2 + one[i]
                        en2 += 1
                    else:
                        break
                label = ""
                for i in range(en2 + 1, len(one)):
                    label = label + one[i]

                intructions_tokens.append({"Counter": inst["Address"], "word": "BNE", "operands": [rs1, rs2, label], "type": "SB"})
            elif (ins == "BLT"):
                one = instr.strip()
                en = 3
                rs1 = ""
                for i in range(3, len(one)):
                    if (one[i] != ','):
                        rs1 = rs1 + one[i]
                        en += 1
                    else:
                        break
                print(rs1)
                rs2 = ""
                en2 = en + 1
                for i in range(en + 1, len(one)):
                    if (one[i] != ','):
                        rs2 = rs2 + one[i]
                        en2 += 1
                    else:
                        break
                label = ""
                for i in range(en2 + 1, len(one)):
                    label = label + one[i]

                intructions_tokens.append({"Counter": inst["Address"], "word": "BLT", "operands": [rs1, rs2, label], "type": "SB"})
            elif (ins == "BGE"):
                one = instr.strip()
                en = 3
                rs1 = ""
                for i in range(3, len(one)):
                    if (one[i] != ','):
                        rs1 = rs1 + one[i]
                        en += 1
                    else:
                        break
                print(rs1)
                rs2 = ""
                en2 = en + 1
                for i in range(en + 1, len(one)):
                    if (one[i] != ','):
                        rs2 = rs2 + one[i]
                        en2 += 1
                    else:
                        break
                label = ""
                for i in range(en2 + 1, len(one)):
                    label = label + one[i]

                intructions_tokens.append({"Counter": inst["Address"], "word": "BGE", "operands": [rs1, rs2, label], "type": "SB"})
            elif (ins == "BLTU"):
                one = instr.strip()
                en = 4
                rs1 = ""
                for i in range(4, len(one)):
                    if (one[i] != ','):
                        rs1 = rs1 + one[i]
                        en += 1
                    else:
                        break
                print(rs1)
                rs2 = ""
                en2 = en + 1
                for i in range(en + 1, len(one)):
                    if (one[i] != ','):
                        rs2 = rs2 + one[i]
                        en2 += 1
                    else:
                        break
                label = ""
                for i in range(en2 + 1, len(one)):
                    label = label + one[i]

                intructions_tokens.append({"Counter": inst["Address"], "word": "BLTU", "operands": [rs1, rs2, label], "type": "SB"})
            elif (ins == "BGEU"):
                one = instr.strip()
                en = 4
                rs1 = ""
                for i in range(4, len(one)):
                    if (one[i] != ','):
                        rs1 = rs1 + one[i]
                        en += 1
                    else:
                        break
                print(rs1)
                rs2 = ""
                en2 = en + 1
                for i in range(en + 1, len(one)):
                    if (one[i] != ','):
                        rs2 = rs2 + one[i]
                        en2 += 1
                    else:
                        break
                label = ""
                for i in range(en2 + 1, len(one)):
                    label = label + one[i]

                intructions_tokens.append({"Counter": inst["Address"], "word": "BGEU", "operands": [rs1, rs2, label], "type": "SB"})
            elif (ins == "SB"):
                one = instr.strip()
                en = 2
                rs1 = ""
                for i in range(2, len(one)):
                    if (one[i] != ','):
                        rs1 = rs1 + one[i]
                        en += 1
                    else:
                        break
                print(rs1)
                offset = ""
                en2 = en + 1
                for i in range(en + 1, len(one)):
                    if (one[i] != '('):
                        offset = offset + one[i]
                        en2 += 1
                    else:
                        break
                rs2 = ""
                for i in range(en2 + 1, len(one) - 1):
                    rs2 = rs2 + one[i]

                intructions_tokens.append({"Counter": inst["Address"], "word": "SH", "operands": [rs1, offset, rs2], "type": "S"})
            elif (ins == "SH"):
                one = instr.strip()
                en = 2
                rs1 = ""
                for i in range(2, len(one)):
                    if (one[i] != ','):
                        rs1 = rs1 + one[i]
                        en += 1
                    else:
                        break
                print(rs1)
                offset = ""
                en2 = en + 1
                for i in range(en + 1, len(one)):
                    if (one[i] != '('):
                        offset = offset + one[i]
                        en2 += 1
                    else:
                        break
                rs2 = ""
                for i in range(en2 + 1, len(one) - 1):
                    rs2 = rs2 + one[i]

                intructions_tokens.append({"Counter": inst["Address"], "word": "SH", "operands": [rs1, offset, rs2], "type": "S"})
            elif (ins == "SW"):
                one = instr.strip()
                en = 2
                rs1 = ""
                for i in range(2, len(one)):
                    if (one[i] != ','):
                        rs1 = rs1 + one[i]
                        en += 1
                    else:
                        break
                print(rs1)
                offset = ""
                en2 = en + 1
                for i in range(en + 1, len(one)):
                    if (one[i] != '('):
                        offset = offset + one[i]
                        en2 += 1
                    else:
                        break
                rs2 = ""
                for i in range(en2 + 1, len(one) - 1):
                    rs2 = rs2 + one[i]

                intructions_tokens.append({"Counter": inst["Address"], "word": "SW", "operands": [rs1, offset, rs2], "type": "S"})
            elif ins == "ADD" or ins == "OR" or ins == "AND" or ins == "SUB" or ins == "SLL" or ins == "SLT" or ins == "SLTU" or ins == "XOR" or ins == "SRL" or ins == "SRA":
                print("This is R-Type Format")
                print("Its opcode is 0110011")
                test = sp[1].strip()
                registers = test.split(",", 2)
                rd = registers[0].strip()
                rs2 = registers[1].strip()
                rs1 = registers[2].strip()
                if ins == "ADD":
                    print("func3 = 000, func7 = 0000000")
                    #print(rs1+rs2)
                    intructions_tokens.append({"Counter": inst["Address"], "word" : "ADD", "operands":[rd,rs2,rs1], "type" :"R"})


                elif ins == "OR":
                    print("func3 = 110, func7 = 0000000")
                    intructions_tokens.append({"Counter": inst["Address"], "word" : "OR", "operands":[rd,rs2,rs1], "type" :"R"})

                elif ins == "AND":
                    print("func3 = 111, func7 = 0000000")
                    intructions_tokens.append({"Counter": inst["Address"], "word" : "AND", "operands":[rd,rs2,rs1], "type" :"R"})

                elif ins == "SUB":
                    print("func3 = 000, func7 = 0100000")
                    intructions_tokens.append({"Counter": inst["Address"], "word" : "SUB", "operands":[rd,rs2,rs1], "type" :"R"})

                elif ins == "SLL":
                    print("func3 = 001, func7 = 0000000")

                    intructions_tokens.append({"Counter": inst["Address"], "word" : "ADD", "operands":[rd,rs2,rs1], "type" :"R"})

                elif ins == "SLT":
                    print("func3 = 010, func7 = 0000000")

                    intructions_tokens.append({"Counter": inst["Address"], "word" : "SLT", "operands":[rd,rs2,rs1], "type" :"R"})

                elif ins == "SLTU":
                    print("func3 = 011, func7 = 0000000")

                    intructions_tokens.append({"Counter": inst["Address"], "word" : "SLTU", "operands":[rd,rs2,rs1], "type" :"R"})

                elif ins == "XOR":
                    print("func3 = 100, func7 = 0000000")
                    intructions_tokens.append({"Counter": inst["Address"], "word" : "XOR", "operands":[rd,rs2,rs1], "type" :"R"})

                elif ins == "SRL":
                    print("func3 = 101, func7 = 0000000")
                    intructions_tokens.append({"Counter": inst["Address"], "word" : "SRL", "operands":[rd,rs2,rs1], "type" :"R"})

                elif ins == "SRA":
                    print("func3 = 101, func7 = 0100000")
                    intructions_tokens.append({"Counter": inst["Address"], "word" : "SRA", "operands":[rd,rs2,rs1], "type" :"R"})
            elif(ins == "ADDI" or ins == "SLTI" or ins == "SLTIU" or ins == "XORI" or ins == "ORI" or ins == "ANDI" or ins == "SLLI" or ins == "SLRI" or ins == "SRAI" ):
                test = sp[1].strip()
                registers = test.split(",",2)
                rd = registers[0].strip()
                rs1 = registers[1].strip()
                immediate = registers[2].strip()
                if (ins == "ADDI"):
                    intructions_tokens.append({"Counter":inst["Address"], "word": "ADDI", "operands": [rd, rs1, immediate], "type": "I"})
                elif (ins == "SLTI"):

                    intructions_tokens.append({"Counter": inst["Address"], "word": "SLTI", "operands": [rd, rs1, immediate], "type": "I"})
                elif (ins == "SLTIU"):

                    intructions_tokens.append({"Counter": inst["Address"], "word": "SLTIU", "operands": [rd, rs1, immediate], "type": "I"})
                elif (ins == "XORI"):


                    intructions_tokens.append({"Counter": inst["Address"], "word": "XORI", "operands": [rd, rs1, immediate], "type": "I"})
                elif (ins == "ORI"):

                    intructions_tokens.append({"Counter": inst["Address"], "word": "ORI", "operands": [rd, rs1, immediate], "type": "I"})
                elif (ins == "ANDI"):

                    intructions_tokens.append({"Counter": inst["Address"], "word": "ANDI", "operands": [rd, rs1, immediate], "type": "I"})
                elif (ins == "SLLI"):

                    intructions_tokens.append({"Counter": inst["Address"], "word": "SLLI", "operands": [rd, rs1, immediate], "type": "I"})
                elif (ins == "SRLI"):

                    intructions_tokens.append({"Counter": inst["Address"], "word": "SRLI", "operands": [rd, rs1, immediate], "type": "I"})
                elif (ins == "SRAI"):


                    intructions_tokens.append({"Counter": inst["Address"], "word": "SRAI", "operands": [rd, rs1, immediate], "type": "I"})
            elif(ins == "LB" or ins == "LH" or ins == "LW" or ins == "LBU" or ins == "LHU" ):
                test = sp[1].strip()
                registers = test.split(",")
                rd = registers[0].strip()
                temp = registers[1].split("(")
                offset = temp[0].strip()
                rs1 = temp[1].split(")")[0].strip()
                if (ins == "LB"):

                    intructions_tokens.append({"Counter": inst["Address"], "word": "LB", "operands": [rd, offset, rs1], "type": "I"})
                elif (ins == "LH"):

                    intructions_tokens.append({"Counter": inst["Address"], "word": "LH", "operands": [rd, offset, rs1], "type": "I"})
                elif (ins == "LW"):

                    intructions_tokens.append({"Counter": inst["Address"], "word": "LW", "operands": [rd, offset, rs1], "type": "I"})
                elif (ins == "LBU"):

                    intructions_tokens.append({"Counter":inst["Address"], "word": "LBU", "operands": [rd, offset, rs1], "type": "I"})
                elif (ins == "LHU"):

                    intructions_tokens.append({"Counter": inst["Address"], "word": "LHU", "operands": [rd, offset, rs1], "type": "I"})
            elif(ins == "FENCE" or ins == "ECALL" or ins =="EBREAK"):
                intructions_tokens.append(
                    {"Counter": inst["Address"], "word": ins, "operands": [-1], "type": "STOP"})
            count_instructions += 4
            #print(count_instructions)
    except IndexError:
        print("Invalid Instruction format at instruction at address   " + str(count_instructions))
def finalize_instructions_and_labels():
    global instructions_map
    global Labels_map
    for inst in intructions_tokens:
        instructions_map[inst["Counter"]] = inst
    for label in Labels:
        Labels_map[label["Name"]] = label["Address"]
def initialize_registers():
    global registers
    for i in range(0,32):
        registers["x"+str(i)] = 0
        RegNames["x" + str(i)] = "x"+str(i)
    RegNames["zero"] = "x0"
    RegNames["ra"] = "x1"
    RegNames["sp"] = "x2"
    RegNames["gp"] = "x3"
    RegNames["tp"] = "x4"
    RegNames["t0"] = "x5"
    RegNames["t1"] = "x6"
    RegNames["t2"] = "x7"
    RegNames["s0"] = "x8"
    RegNames["s1"] = "x9"
    RegNames["a0"] = "x10"
    RegNames["a1"] = "x11"
    RegNames["a2"] = "x12"
    RegNames["a3"] = "x13"
    RegNames["a4"] = "x14"
    RegNames["a5"] = "x15"
    RegNames["a6"] = "x16"
    RegNames["a7"] = "x17"
    RegNames["s2"] = "x18"
    RegNames["s3"] = "x19"
    RegNames["s4"] = "x20"
    RegNames["s5"] = "x21"
    RegNames["s6"] = "x22"
    RegNames["s7"] = "x23"
    RegNames["s8"] = "x24"
    RegNames["s9"] = "x25"
    RegNames["s10"] = "x26"
    RegNames["s11"] = "x27"
    RegNames["t3"] = "x28"
    RegNames["t4"] = "x29"
    RegNames["t5"] = "x30"
    RegNames["t6"] = "x31"
if __name__ == '__main__':
    path = "code.txt"
    read_code_file(path)
    #print(Labels)
    #print(instructions)
    instruction_tokenization()
    #print(intructions_tokens)
    finalize_instructions_and_labels()
    print(instructions_map)
    print(Labels_map)
    initialize_registers()
    #print(RegNames)
