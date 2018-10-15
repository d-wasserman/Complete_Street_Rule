# --------------------------------
# Name: Generate_Altered_Streets.py
# Purpose: Alter parameters of selected shapes based on dictionary of attributes. Copy to new layer, translate based on parameters. 
# Current Owner: David Wasserman
# Last Modified: 6/11/2018
# Copyright:   (c) David Wasserman
# CityEngine Vs: 2015.2
# Python Version:   2.7
# License
# Copyright 2018 David J. Wasserman
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------

# Import Modules

from scripting import *
from itertools import product
import time
# get a CityEngine instance
ce = CE()


# Turn off User Interface updates, or script might take forever.
# @noUIupdate
        
def generate_attribute_product(attr_dict):
    """Takes in a dictionary in the form of {attribute:[value1,value2], and returns ordered keys and combinations of each value1"""
    ordered_keys = sorted(attr_dict.keys())
    value_input = [attr_dict[i] for i in ordered_keys]
    product_obj = product(*value_input)
    return ordered_keys, product_obj

def batch_attribute_alteration(alteration_dict = {},translation=0):
    """ This function will take a dictionary of attributes and use python combinatoric functions to create a copy of a selection in a new layer for every combination possible of those attributes. """
    layers = ce.getObjectsFrom(ce.selection())
    print(
        "There are " + str(len(layers)) + " objects in the current selection.")
    counter = 0
    # Turns off visibility of all layers.
    
    print("Iterating through all attribute combinations.")
    keys, product_obj = generate_attribute_product(alteration_dict)
    for index,row in enumerate(product_obj):
        try:
            
            for index, key in enumerate(keys):
                ce.setAttribute(ce.selection(),key,row[index])
                ce.setAttributeSource(ce.selection(),key, 'OBJECT')
                ce.generateModels(ce.selection())
                ce.waitForUIIdle()
                time.sleep(1)
                    
            print(keys)
            print(row)
        except Exception as e:
            import sys
            print("Could not execute on counter " + str(counter))
            print("Error:", e.args[0])
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            counter += 1
            pass


# Call
if __name__ == '__main__':
    print("Batch Generation script started.")
    # Declare variables
    generation_dict = {"Lane_Distribution":[0,1,.5],"Traffic_Direction":["right-hand","left-hand"]}
    batch_attribute_alteration(generation_dict)
    print("Script completed.")
