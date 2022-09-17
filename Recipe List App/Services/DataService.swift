//
//  DataService.swift
//  Recipe List App
//
//  Created by Gennie Newell on 9/14/22.
//

import Foundation


class DataService{
    
    func getLocalData()-> [Recipe] {
        //Parse local json file
        
        //Get url path to json file
        let pathString = Bundle.main.path(forResource: "recipes", ofType: "json")
        guard pathString != nil else {
            return [Recipe]()
        }
        //Create a url obj.
        let url = URL(fileURLWithPath: pathString!)
        
        do {
            //Create a data obj.
            let data = try Data(contentsOf: url)
            
            // Decode the data with a JSON decoder
            let decoder = JSONDecoder()
            
            do{
                
            let recipeData = try decoder.decode([Recipe].self,from:data)
                
            //Add the unique IDs
            for r in recipeData {
                    r.id = UUID()
            }

            //Return the recipes
            return recipeData
                
            }
            catch{
                print(error)
            
            }
           
        }
        catch{
            print(error)
        }
    return [Recipe]()
        
    }
    
}
