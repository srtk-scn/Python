def outer():
    print("control is in outer function")
    
    def inner():
        print("control is in inner funtion")
        
    
        def ininner():
            print("control is in ininner function")
            print("control is leaving ininner function")
        ininner()
        print("control is leaving inner funtion")   
    inner()
    print("control is leaving outer function")    

outer()