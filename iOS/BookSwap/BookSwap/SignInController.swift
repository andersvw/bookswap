//
//  SignInController.swift
//  BookSwap
//
//  Created by Proactive Performance Solutions, Inc. on 4/8/15.
//  Copyright (c) 2015 Book Swap. All rights reserved.
//

import UIKit
import Alamofire

class SignInController: UIViewController {
    
    @IBOutlet weak var usernameField: UITextField!
    @IBOutlet weak var passwordField: UITextField!
    
    @IBAction func signIn(sender: UIButton) {
        var username = usernameField.text
        var password = passwordField.text
        
        Alamofire.request(.GET, "http://128.4.26.251/api/users/", parameters: ["username": username, "password": password])
            .responseJSON { (_, _, JSON, _) in
                println(JSON)
        
        }
        
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }
        
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}
