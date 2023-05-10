import numpy as np
import pandas as pd
Labels = []
Labels_map = {}
instructions= []
intructions_tokens = []
instructions_map = {}
memory = {}
pc = 0
registers = {}
RegNames = {}
stack = {}
def binary_to_decimal_unsigned(binary):
    """
    Converts a 32-bit unsigned binary number to its decimal value.
    """
    decimal = 0
    for i in range(31, -1, -1):
        if binary[i] == '1':
            decimal += 2**(31-i)
    return decimal
def binary_to_decimal(bin_str):
    # Convert the binary string to a signed integer using int()
    num = int(bin_str, 2)

    # If the most significant bit (MSB) is 1, the number is negative
    if num & 0x80000000:
        # Convert the number to its two's complement representation
        num = -((num ^ 0xFFFFFFFF) + 1)

    return num
def signed_integer_to_binary(num: int) -> str:
    if num >= 0:
        # Convert positive numbers to binary
        binary = bin(num)[2:].zfill(32)
    else:
        # Convert negative numbers to two's complement binary
        binary = bin((1 << 32) + num)[2:]

    return binary
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
            Labels.append({"Name" : label,"Address" : pc})
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

                intructions_tokens.append({"Counter": inst["Address"], "word": "SB", "operands": [rs1, offset, rs2], "type": "S"})
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
            elif(ins == "ADDI" or ins == "SLTI" or ins == "SLTIU" or ins == "XORI" or ins == "ORI" or ins == "ANDI" or ins == "SLLI" or ins == "SRLI" or ins == "SRAI" ):
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
def read_and_initialize_memory(path):
    file = open(path, 'r')
    lines= file.readlines()
    for l in lines:
        temp = l.split(',', 1)
        binar = signed_integer_to_binary(int(temp[1]))
        base = int(temp[0])
        memory[base] = binar[24:32]
        memory[base+1] = binar[16:24]
        memory[base+2] = binar[8:16]
        memory[base+3] = binar[0:8]
def validate_memory(addr):
    global memory
    if(addr not in memory.keys()):
        memory[addr] = "00000000"
def execute_instructions(starting_address, end_address):
    global memory
    global registers
    inst_address = starting_address
    while(inst_address != end_address):
        instruction = instructions_map[inst_address]
        ins = instruction["word"]
        if(ins == "ADDI" or ins == "SLTI" or ins == "SLTIU" or ins == "XORI" or ins == "ORI" or ins == "ANDI" or ins == "SLLI" or ins == "SRLI" or ins == "SRAI" ):
            rs1 = instruction["operands"][1]
            imm = instruction["operands"][2]
            rd = instruction["operands"][0]
            if (rs1 not in RegNames.keys() or rd not in RegNames.keys()):
                print("Invalid Instruction Format at address " + int(inst_address))
                return
            elif (int(imm) >= 2048 or int(imm) < -2048):
                print("Invalid Instruction Format at address " + str(inst_address))
                return
            else:
                if(instruction["word"] == "ADDI"):
                        result = signed_integer_to_binary( int(registers[RegNames[rs1]]) + int(imm))
                        result = result[len(result)-32:]
                        registers[RegNames[rd]] = binary_to_decimal(result)
                        inst_address += 4
                elif(instruction["word"] =="ANDI"):
                    temp = signed_integer_to_binary(int(imm))
                    temp = temp[len(temp)-12:]
                    immediate = 20*temp[len(temp)-12]+temp
                    comp = binary_to_decimal_unsigned(immediate)
                    result = registers[RegNames[rs1]] & comp
                    registers[RegNames[rd]] = binary_to_decimal(signed_integer_to_binary(result))
                    inst_address += 4
                elif(instruction["word"] == "ORI"):
                    temp = signed_integer_to_binary(int(imm))
                    temp = temp[len(temp) - 12:]
                    immediate = 20 * temp[len(temp) - 12] + temp
                    comp = binary_to_decimal_unsigned(immediate)
                    result = registers[RegNames[rs1]] | comp
                    registers[RegNames[rd]] = binary_to_decimal(signed_integer_to_binary(result))
                    inst_address += 4
                elif(instruction["word"] == "XORI"):
                    temp = signed_integer_to_binary(int(imm))
                    temp = temp[len(temp) - 12:]
                    immediate = 20 * temp[len(temp) - 12] + temp
                    comp = binary_to_decimal_unsigned(immediate)
                    result = registers[RegNames[rs1]] ^ comp
                    registers[RegNames[rd]] = binary_to_decimal(signed_integer_to_binary(result))
                    inst_address += 4
                elif(instruction["word"] == "SLTIU"):
                    if(abs(registers[RegNames[rs1]]) < abs(int(imm))):
                        registers[RegNames[rd]] = 1
                    else:
                        registers[RegNames[rd]] = 0
                    inst_address +=4
                elif(instruction["word"] == "SLTI"):
                    if (registers[RegNames[rs1]] < int(imm)):
                        registers[RegNames[rd]] = 1
                    else:
                        registers[RegNames[rd]] = 0
                    inst_address += 4
                elif(instruction["word"] == "SLLI"):
                    if(int(imm) >= 32):
                        print("Shift amount out of range at instruction at address = "+ str(inst_address))
                    else:
                        content = signed_integer_to_binary(registers[RegNames[rs1]] <<int(imm))
                        content = content[len(content)-32:]
                        registers[RegNames[rd]] = binary_to_decimal(content)
                    inst_address += 4
                elif(instruction["word"] == "SRLI"):
                    if (int(imm) >= 32):
                        print("Shift amount out of range at instruction at address = " + str(inst_address))
                    else:
                        #print(signed_integer_to_binary(registers[RegNames[rs1]]))
                        content = signed_integer_to_binary(registers[RegNames[rs1]])
                        res = '0'*int(imm)+ content[0:len(content)-int(imm)]
                        #print(res)
                        registers[RegNames[rd]] = binary_to_decimal(res)
                        #print(signed_integer_to_binary(registers[RegNames[rd]]))
                    inst_address+= 4
                elif(instruction["word"] == "SRAI"):
                    if (int(imm) >= 32):
                        print("Shift amount out of range at instruction at address = " + str(inst_address))
                    else:
                        registers[RegNames[rd]] = registers[RegNames[rs1]] >> int(imm)
                    inst_address += 4
        elif(ins == "LB" or ins == "LH" or ins == "LW" or ins == "LBU" or ins == "LHU" ):
            rs1 = instruction["operands"][2]
            imm = instruction["operands"][1]
            rd = instruction["operands"][0]
            if (rs1 not in RegNames.keys() or rd not in RegNames.keys()):
                print("Invalid Instruction Format at address " + int(inst_address))
                return
            elif (int(imm) >= 2048 or int(imm) < -2048):
                print("Invalid Instruction Format at address " + str(inst_address))
                return
            else:
                if(instruction["word"] == "LW"):
                    content = ""
                    addr = int(registers[RegNames[rs1]]) + int(imm)
                    validate_memory(addr)
                    validate_memory(addr+1)
                    validate_memory(addr+2)
                    validate_memory(addr+3)
                    content = memory[addr+3] + memory[addr+2] + memory[addr+1] + memory[addr]
                    result = binary_to_decimal(content)
                    #print(content)
                    #print(result)
                    #print(rd)
                    registers[RegNames[rd]] = result
                    inst_address +=4
                elif(instruction["word"] == "LHU"):
                    content = ""
                    addr = int(registers[RegNames[rs1]]) + int(imm)
                    validate_memory(addr)
                    validate_memory(addr + 1)
                    content = "0"*16 + memory[addr + 1] + memory[addr]
                    result = binary_to_decimal(content)
                    registers[RegNames[rd]] = result
                    inst_address += 4
                elif(instruction["word"] == "LBU"):
                    content = ""
                    addr = int(registers[RegNames[rs1]]) + int(imm)
                    validate_memory(addr)
                    content = "0" * 24 + memory[addr]
                    result = binary_to_decimal(content)
                    registers[RegNames[rd]] = result
                    inst_address += 4
                elif(instruction["word"] == "LH"):
                    content = ""
                    addr = int(registers[RegNames[rs1]]) + int(imm)
                    validate_memory(addr)
                    validate_memory(addr + 1)
                    content = memory[addr+1][0] * 16 + memory[addr + 1] + memory[addr]
                    result = binary_to_decimal(content)
                    registers[RegNames[rd]] = result
                    inst_address += 4
                elif(instruction["word"] == "LB"):
                    content = ""
                    addr = int(registers[RegNames[rs1]]) + int(imm)
                    validate_memory(addr)
                    content = memory[addr][0] * 24 + memory[addr]
                    result = binary_to_decimal(content)
                    registers[RegNames[rd]] = result
                    inst_address += 4
        elif(instruction["word"] == "SW"):
            rs1 = instruction["operands"][2].strip()
            imm = instruction["operands"][1].strip()
            rd = instruction["operands"][0].strip()
            imm_bin = signed_integer_to_binary(int(imm))
            if (rs1 not in RegNames.keys() or rd not in RegNames.keys()):
                print("Invalid Instruction Format at address " + str(inst_address))
                return
            elif(int(imm) >= 2048 or int(imm) < -2048 ):
                print("Invalid Instruction Format at address " + str(inst_address))
                return
            else:
                content = signed_integer_to_binary(int(registers[RegNames[rd]]))
                if(len(content) > 32):
                    content = content[len(content)-32:len(content)]
                addr = int(registers[RegNames[rs1]])+ int(imm)
                validate_memory(addr)
                validate_memory(addr+1)
                validate_memory(addr+2)
                validate_memory(addr+3)
                memory[addr] = content[24:32]
                memory[addr + 1] = content[16:24]
                memory[addr + 2] = content[8:16]
                memory[addr + 3] = content[0:8]
            inst_address += 4
        elif (instruction["word"] == "SH"):
            rs1 = instruction["operands"][2].strip()
            imm = instruction["operands"][1].strip()
            rd = instruction["operands"][0].strip()
            # print(int(imm))
            # print(bin(int(imm)))
            imm_bin = signed_integer_to_binary(int(imm))
            if (rs1 not in RegNames.keys() or rd not in RegNames.keys()):
                print("Invalid Instruction Format at address " + str(inst_address))
                return
            elif (int(imm) >= 2048 or int(imm) < -2048):
                print("Invalid Instruction Format at address " + str(inst_address))
                return
            else:
                content = signed_integer_to_binary(int(registers[RegNames[rd]]))
                # print(rd)
                # print(content)
                # print(len(content))
                if (len(content) > 32):
                    content = content[len(content) - 32:len(content)]
                addr = int(registers[RegNames[rs1]]) + int(imm)
                validate_memory(addr)
                validate_memory(addr + 1)
                memory[addr] = content[24:32]
                memory[addr + 1] = content[16:24]
            inst_address += 4
        elif (instruction["word"] == "SB"):
            rs1 = instruction["operands"][2].strip()
            imm = instruction["operands"][1].strip()
            rd = instruction["operands"][0].strip()
            # print(int(imm))
            # print(bin(int(imm)))
            imm_bin = signed_integer_to_binary(int(imm))
            if (rs1 not in RegNames.keys() or rd not in RegNames.keys()):
                print("Invalid Instruction Format at address " + str(inst_address))
                return
            elif (int(imm) >= 2048 or int(imm) < -2048):
                print("Invalid Instruction Format at address " + str(inst_address))
                return
            else:
                content = signed_integer_to_binary(int(registers[RegNames[rd]]))
                # print(rd)
                # print(content)
                # print(len(content))
                if (len(content) > 32):
                    content = content[len(content) - 32:len(content)]
                addr = int(registers[RegNames[rs1]]) + int(imm)
                validate_memory(addr)
                memory[addr] = content[24:32]
            inst_address += 4
        elif (ins == "BEQ"):
            rs1 = instruction["operands"][0].strip()
            rs2 = instruction["operands"][1].strip()
            label = instruction["operands"][2].strip()
            if (rs1 not in RegNames.keys() or rs1 not in RegNames.keys()):
                print("Invalid Instruction Format at address " + str(inst_address))
                return
            elif (label not in Labels_map.keys()):
                print("Invalid Instruction Format at address " + str(inst_address))
                return
            else:
                if(registers[RegNames[rs1]] == registers[RegNames[rs2]]):
                    inst_address = Labels_map[label]
                else:
                    inst_address += 4
        elif(ins == "BNE"):
            rs1 = instruction["operands"][0].strip()
            rs2 = instruction["operands"][1].strip()
            label = instruction["operands"][2].strip()
            if (rs1 not in RegNames.keys() or rs1 not in RegNames.keys()):
                print("Invalid Instruction Format at address " + str(inst_address))
                return
            elif (label not in Labels_map.keys()):
                print("Invalid Instruction Format at address " + str(inst_address))
                return
            else:
                if (registers[RegNames[rs1]] != registers[RegNames[rs2]]):
                    inst_address = Labels_map[label]
                else:
                    inst_address += 4
        elif(ins == "BLT"):
            rs1 = instruction["operands"][0].strip()
            rs2 = instruction["operands"][1].strip()
            label = instruction["operands"][2].strip()
            if (rs1 not in RegNames.keys() or rs1 not in RegNames.keys()):
                print("Invalid Instruction Format at address " + str(inst_address))
                return
            elif (label not in Labels_map.keys()):
                print("Invalid Instruction Format at address " + str(inst_address))
                return
            else:
                if (registers[RegNames[rs1]] < registers[RegNames[rs2]]):
                    inst_address = Labels_map[label]
                else:
                    inst_address += 4
        elif(ins == "BGE"):
            rs1 = instruction["operands"][0].strip()
            rs2 = instruction["operands"][1].strip()
            label = instruction["operands"][2].strip()
            if (rs1 not in RegNames.keys() or rs1 not in RegNames.keys()):
                print("Invalid Instruction Format at address " + str(inst_address))
                return
            elif (label not in Labels_map.keys()):
                print("Invalid Instruction Format at address " + str(inst_address))
                return
            else:
                if (registers[RegNames[rs1]] >= registers[RegNames[rs2]]):
                    inst_address = Labels_map[label]
                else:
                    inst_address += 4
        elif(ins == "BGEU"):
            rs1 = instruction["operands"][0].strip()
            rs2 = instruction["operands"][1].strip()
            label = instruction["operands"][2].strip()
            if (rs1 not in RegNames.keys() or rs1 not in RegNames.keys()):
                print("Invalid Instruction Format at address " + str(inst_address))
                return
            elif (label not in Labels_map.keys()):
                print("Invalid Instruction Format at address " + str(inst_address))
                return
            else:
                if (abs(registers[RegNames[rs1]]) >= abs(registers[RegNames[rs2]])):
                    inst_address = Labels_map[label]
                else:
                    inst_address += 4
        elif(ins == "BLTU"):
            rs1 = instruction["operands"][0].strip()
            rs2 = instruction["operands"][1].strip()
            label = instruction["operands"][2].strip()
            if (rs1 not in RegNames.keys() or rs1 not in RegNames.keys()):
                print("Invalid Instruction Format at address " + str(inst_address))
                return
            elif (label not in Labels_map.keys()):
                print("Invalid Instruction Format at address " + str(inst_address))
                return
            else:
                if (abs(registers[RegNames[rs1]]) < abs(registers[RegNames[rs2]])):
                    inst_address = Labels_map[label]
                else:
                    inst_address += 4
        elif(ins == "ECALL" or ins =="FENCE" or ins == "EBREAK"):
            print("Execution terminated at address "+ str(inst_address))
            return
        elif(ins == "JAL"):
            label = instruction["operands"][1].strip()
            rd = instruction["operands"][0].strip()
            if(label in Labels_map.keys()):
                registers[RegNames[rd]] = inst_address + 4
                inst_address = Labels_map[label]

            elif(int(label) in Labels_map.values()):
                registers[RegNames[rd]] = inst_address+4
                inst_address = int(label)
            else:
                print("Invalid address at instruction address" + str(inst_address))

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
    read_and_initialize_memory("data.txt")
    print(memory)
    starting_address = int(input("Enter the starting address of the program: "))
    addresses = list(instructions_map.keys())
    end_address = addresses[len(addresses)-1]+4
    #print(RegNames)
    #registers["x8"]= 485623644513
    execute_instructions(starting_address, end_address)
    print(registers)
    print(memory)

