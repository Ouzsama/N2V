

import json  
import os 


confi_path = os.path.join(os.path.dirname(__file__) , ".." ,"config" , "config.json")


def get_banner() :
    

    try : 
         

        with open (confi_path , "r") as file : config = json.load(file)

        banner = f""" 
                ,--.                       
               ,--.'|    ,----,             
           ,--,|  | |  .'   .' \       ,---.
        ,`--.'`|  | :,----,'    |     /__./|
        |   :  |  | ||    |  .  ;,---.;  | |     {config["Description"]}
        |   |   \ | :|    |.'  //___/ \  | |     Version {config["Version"]}
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
        banner = f""" 
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

