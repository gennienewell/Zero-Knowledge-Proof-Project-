//
//  RecipeDetailView.swift
//  Recipe List App
//
//  Created by Gennie Newell on 9/14/22.
//

import SwiftUI

struct RecipeDetailView: View {
    
    var recipe:Recipe
    
    
    var body: some View {
        ScrollView{
            VStack(alignment: .leading){
                Image(recipe.image)
                    .resizable()
                    .scaledToFill()
                VStack(alignment: .leading){
                    Text("Ingredients").font(.headline)
                        .padding([.bottom, .top],5)
                    
                    ForEach(recipe.ingredients){ item in
                        Text(item.name)
                    }
                }.padding([.leading,.trailing],10)
                
                VStack(alignment:.leading){
                    Text("Directions")
                        .font(.headline)
                        .padding([.bottom, .top],5)
                    
                    ForEach(0..<recipe.directions.count,id:\.self){ i in
                        Text(String(i+1) + ". " + recipe.directions[i])
                            .padding(.bottom,5)
                    }
                    
                }.padding([.leading,.trailing],10)
            }
            
            
        }.navigationBarTitle(recipe.name)
    }
}

struct RecipeDetailView_Previews: PreviewProvider {
    static var previews: some View {
        //dummy reipe
        let model = RecipeModel()
        
        RecipeDetailView(recipe: model.recipes[0])
    }
}
