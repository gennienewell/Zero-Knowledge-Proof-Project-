//
//  RecipeTabView.swift
//  Recipe List App
//
//  Created by Gennie Newell on 9/19/22.
//

import SwiftUI

struct RecipeTabView: View {
    var body: some View {
        TabView{
            RecipeFeatureView()
                .tabItem{
                    VStack{
                        Image(systemName: "star.fill")
                        Text("Featured")
                    }
                }
            RecipeListView()
                .tabItem{
                    VStack{
                        Image(systemName: "list.bullet")
                        Text("List")
                    }
                    
                }
        }
        .environmentObject(RecipeModel())
    }
}

struct RecipeTabView_Previews: PreviewProvider {
    static var previews: some View {
        RecipeTabView()
    }
}
