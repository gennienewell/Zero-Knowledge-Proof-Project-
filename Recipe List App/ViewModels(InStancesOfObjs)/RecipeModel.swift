//
//  RecipeModel.swift
//  Recipe List App
//
//  Created by Gennie Newell on 9/14/22.
//

import Foundation

class RecipeModel: ObservableObject{
    
    @Published var recipes = [Recipe]()
    
    init(){
        //Create data service obj and retreive data
        let service = DataService()
        self.recipes =  service.getLocalData()
    }
    
    
}
