//
//  SupermarketApp.swift
//  Supermarket
//
//  Created by cheung gary on 6/2/2025.
//

import SwiftUI

@main
struct SupermarketApp: App {
    let persistenceController = PersistenceController.shared
    
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(\.managedObjectContext, persistenceController.viewContext)
                .accentColor(.blue)
        }
    }
}
