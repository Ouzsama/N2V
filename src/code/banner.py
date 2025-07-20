

import json  
import os 


confi_path = os.path.join(os.path.dirname(__file__) , ".." ,"config" , "config.json")


def get_banner() :
    

    try : 
         

        with open (confi_path , "r") as file : config = json.load(file)

        banner = rf""" 
                ,--.                       
               ,--.'|    ,----,             
           ,--,|  | |  .'   .' \       ,---.
        ,`--.'`|  | :,----,'    |     /__./|
        |   :  |  | ||    |  .  ;,---.;  | |     {config["Description"]}
        |   |   \ | :|    |.'  //___/ \  | |     
        |   : '  '; |`----'/  ; \   \  \ | |
        |   ' ;.    ;  /  ;  /   \   \  \| |     Developed by {config["Owner"]}
        |   | | \   | /  /  /-,   \   \  ' |     Github : {config["Github"]}
        |   : |  ; .'/  /  /.`|    \   \   |     
        |   | '`--'./__;      |     \   `  |     Follow me for more tools and updates!
        |   : |    |   :    .'       \   \ |
        |   |.'    ;   | .'           '---" 
        '---'      `---'                    

        """ 
    except FileNotFoundError  : 
        banner = rf""" 
                ,--.                       
               ,--.'|    ,----,             
           ,--,|  | |  .'   .' \       ,---.
        ,`--.'`|  | :,----,'    |     /__./|
        |   :  |  | ||    |  .  ;,---.;  | |     
        |   |   \ | :|    |.'  //___/ \  | |     
        |   : '  '; |`----'/  ; \   \  \ | |
        |   ' ;.    ;  /  ;  /   \   \  \| |    
        |   | | \   | /  /  /-,   \   \  ' |
        |   : |  ; .'/  /  /.`|    \   \   |
        |   | '`--'./__;      |     \   `  |
        |   : |    |   :    .'       \   \ |
        |   |.'    ;   | .'           '---" 
        '---'      `---'                    

        """
    print (banner)

