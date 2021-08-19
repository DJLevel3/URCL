CPU_stats = {
  "REGISTERS":"99999",
  "MEMORY": "99999",
  "DATABUS_WIDTH": "8",
  "RUN_RAM": False,
  "REMOVE_LABELS": False,
  "SHIFT_RAM": False,
  "SP_LOCATION": "0",
  "SP_IS_GPR": True,
  "REVERSED_STACK": False,
  "SP_VALUE": "0",
  "KEEP_SP": False,
  "REG_ONLY": True,
  }
Instruction_table = {
  "ADD":  [1],
  "RSH":  [1],
  "NOR":  [1],
  "IMM":  [1], # <B> will be an immediate
  "LOD":  [1],
  "STR":  [1],
  "BGE":  [1],
  "DW":   [1], # Only for RUN RAM
  "IN":   [1], # <B> will be an immediate (port)
  "OUT":  [1], # <A> will be an immediate (port)

  "SUB":  [1],
  "JMP":  [1],
  "MOV":  [1],
  "NOP":  [1],
  "IMM":  [1],
  "LSH":  [1],
  "INC":  [1],
  "DEC":  [1],
  "NEG":  [1],
  "AND":  [1],
  "OR":   [1],
  "NOT":  [1],
  "XNOR": [1],
  "XOR":  [1],
  "NAND": [1],
  "BRL":  [1],
  "BRG":  [1],
  "BRE":  [1],
  "BNE":  [1],
  "BOD":  [1],
  "BEV":  [1],
  "BLE":  [1],
  "BRZ":  [1],
  "BNZ":  [1],
  "BRN":  [1],
  "BRP":  [1],
  "PSH":  [1],
  "POP":  [1],
  "CAL":  [1],
  "RET":  [1],
  "HLT":  [1],
  "CPY":  [1],
  "BRC":  [1],
  "BNC":  [1],
  }
def RawURCL(a, b):return a, b
def CleanURCL(a, b):return a, b