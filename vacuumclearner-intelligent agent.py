def vacuum_world():
      
    goal_state = {'A': '0', 'B': '0'}
    cost = 0

    location_input = input("Enter Location of Vacuum") 
    status_input = input("Enter status of " + location_input) 
    status_input_complement = input("Enter status of other room")
    
    if location_input == 'A':
        
        print("Vacuum is placed in Location A")
        if status_input == '1':
            print("Location A is Dirty.")
           
            goal_state['A'] = '0'
            cost += 1                     
            print("Cost for CLEANING A " + str(cost))
            print("Location A has been Cleaned.")

            if status_input_complement == '1':
                
                print("Location B is Dirty.")
                print("Moving right to the Location B. ")
                cost += 1                       #cost for moving right
                print("COST for moving RIGHT" + str(cost))
              
                goal_state['B'] = '0'
                cost += 1                       
                print("COST for CLEANING " + str(cost))
                print("Location B has been Cleaned. ")
            else:
                print("No action" + str(cost))
               
                print("Location B is already clean.")

        if status_input == '0':
            print("Location A is already clean ")
            if status_input_complement == '1':# if B is Dirty
                print("Location B is Dirty.")
                print("Moving RIGHT to the Location B. ")
                cost += 1                       #cost for moving right
                print("COST for moving RIGHT " + str(cost))
               
                goal_state['B'] = '0'
                cost += 1                       
                print("Cost for CLEANING" + str(cost))
                print("Location B has been Cleaned. ")
            else:
                print("No action " + str(cost))
                print(cost)
                
                print("Location B is already clean.")

    else:
        print("Vacuum is placed in location B")
        # Location B is Dirty.
        if status_input == '1':
            print("Location B is Dirty.")
            
            goal_state['B'] = '0'
            cost += 1  
            print("COST for CLEANING " + str(cost))
            print("Location B has been Cleaned.")

            if status_input_complement == '1':
                # if A is Dirty
                print("Location A is Dirty.")
                print("Moving LEFT to the Location A. ")
                cost += 1  
                print("COST for moving LEFT" + str(cost))
                
                goal_state['A'] = '0'
                cost += 1  
                print("COST for CLEANING " + str(cost))
                print("Location A has been Cleaned.")

        else:
            print(cost)
            
            print("Location B is already clean.")

            if status_input_complement == '1':  # if A is Dirty
                print("Location A is Dirty.")
                print("Moving LEFT to the Location A. ")
                cost += 1  
                print("COST for moving LEFT " + str(cost))
               
                goal_state['A'] = '0'
                cost += 1  
                print("Cost for CLEANING " + str(cost))
                print("Location A has been Cleaned. ")
            else:
                print("No action " + str(cost))
               
                print("Location A is already clean.")

    # done cleaning
    print("GOAL STATE: ")
    print(goal_state)
    print("Total cost: " + str(cost))


vacuum_world()