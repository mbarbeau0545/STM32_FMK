"""
#  @file        main.py
#  @brief       Template_BriefDescription.
#  @details     TemplateDetailsDescription.\n
#
#  @author      mba
#  @date        jj/mm/yyyy
#  @version     1.0
"""
#------------------------------------------------------------------------------
#                                       IMPORT
#------------------------------------------------------------------------------
import sys, os, json
from PyCodeGene import LoadConfig_FromExcel as LCFE

from FMKCPU_CodeGen import FMKCPU_CodeGen as FMKCPU
from FMKTIM_CodeGen import FMKTIM_CodeGen as FMKTIM
from FMKIO_CodeGen  import FMKIO_CodeGen as FMKIO
from FMKCDA_CodeGen  import FMKCDA_CodeGen as FMKCDA
from FMKCPU_CodeGen  import FMKCPU_CodeGen as FMKCPU
from FMKSRL_CodeGen  import FMKSRL_CodeGen as FMKSRL
from FMKHRT_CodeGen  import FMKHRT_CodeGen as FMKHRT
#------------------------------------------------------------------------------
#                                       CONSTANT
#------------------------------------------------------------------------------
# CAUTION : Automatic generated code section: Start #

# CAUTION : Automatic generated code section: End #
#------------------------------------------------------------------------------
#                                       CLASS
#------------------------------------------------------------------------------
class PythonToolArgError(Exception):
    def __init__(self, message):
        super().__init__(message)

#------------------------------------------------------------------------------
#                             FUNCTION IMPLMENTATION
#------------------------------------------------------------------------------
def main()-> None:
    if not len(sys.argv) == 2:
        raise PythonToolArgError(f"Expected two argument : hardware configuration and software.\n Get {len(sys.argv)} instead")
    hardware_cfg_path = str(sys.argv[1])

    if not (os.path.isfile(hardware_cfg_path)):
        FileNotFoundError("Expected one argument, hardware configuration.")

    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print('Start Python tool with')
    print(f'\tHardware Confiougration Path -> {hardware_cfg_path}')
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    FMKCPU.code_generation(hardware_cfg_path)
    FMKTIM.code_generation(hardware_cfg_path)
    FMKHRT.code_generation(hardware_cfg_path)
    FMKCDA.code_genration(hardware_cfg_path)
    FMKSRL.code_genration(hardware_cfg_path)
    FMKIO.code_generation(hardware_cfg_path)

    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("<<<<<<<<<<<<<<<<<Successfuly made code generation for project>>>>>>>>>>>>>>>>>")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    return
#------------------------------------------------------------------------------
#			                MAIN
#------------------------------------------------------------------------------
if (__name__ == '__main__'):
    main()

#------------------------------------------------------------------------------
#		                    END OF FILE
#------------------------------------------------------------------------------
#--------------------------
# Function_name
#--------------------------

"""
    @brief
    @details

    @params[in]
    @params[out]
    @retval
"""

