//
//  Recipe.swift
//  Recipe List App
//
//  Created by Gennie Newell on 9/14/22.
//

import Foundation

// This Object is used to form a skelton for the jason data.
class Recipe: Identifiable, Decodable{
    
    var id:UUID?
    var name:String
    var featured:Bool
    var image:String
    var description:String
    var prepTime:String
    var cookTime:String
    var totalTime:String
    var servings:Int
    var highlights:[String]
    var ingredients:[Ingredient]
    var directions:[String]
    
    
}

class Ingredient: Identifiable,Decodable{
    var id:UUID?
    var name:String
    var num:Int?
    var denom:Int?
    var unit:String?
    
    
    
    
}
